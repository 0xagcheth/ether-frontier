from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

SCRIPT_DIR = Path(__file__).resolve().parents[1]
ROOT = SCRIPT_DIR.parents[0]
sys.path.insert(0, str(SCRIPT_DIR))

from build_layered_atlas import expand_sprites, pack_shelves, write_geometry_template
from build_layered_review import build_composite, build_review_grid
from promote_watchtower_projection_master import validate_review
from validate_layered_atlas import validate_common, validate_production
from validate_source_call_plan import validate as validate_source_plan


MANIFEST_TEMPLATE = (
    ROOT
    / "assets/staging/candidates/watchtower/watchtower_layered_manifest_template_v1.json"
)
SOURCE_PLAN = ROOT / "assets/staging/prompts/watchtower_source_call_plan_v1.json"
REVIEW_TEMPLATE = (
    ROOT
    / "assets/staging/candidates/watchtower/watchtower_projection_review_template_v1.json"
)


class LayeredPipelineTests(unittest.TestCase):
    def load_json(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_manifest_template_expands_to_133_runtime_sprites(self):
        template = self.load_json(MANIFEST_TEMPLATE)
        errors: list[str] = []
        expanded = validate_common(template, errors)
        self.assertEqual(errors, [])
        self.assertEqual(len(expanded), 133)
        self.assertEqual(len(expand_sprites(template["sprites"])), 133)

    def test_manifest_template_is_rejected_as_production(self):
        template = self.load_json(MANIFEST_TEMPLATE)
        errors: list[str] = []
        validate_common(template, errors)
        validate_production(template, MANIFEST_TEMPLATE, errors)
        self.assertGreaterEqual(len(errors), 100)
        self.assertTrue(any("atlas PNG does not exist" in item for item in errors))
        self.assertTrue(any("master.approved must be true" in item for item in errors))
        self.assertTrue(any("production manifest must expand" in item for item in errors))

    def test_source_call_plan_is_ordered_and_gated(self):
        plan = self.load_json(SOURCE_PLAN)
        self.assertEqual(validate_source_plan(plan), [])
        self.assertEqual(len(plan["calls"]), 14)
        self.assertEqual(plan["calls"][0]["unit"], "assembled_projection_master")
        self.assertIn("human_projection_approval", plan["calls"][1]["dependsOn"])

    def test_packer_is_deterministic_and_non_overlapping(self):
        sizes = [
            ("stone_02", 18, 21),
            ("body", 40, 30),
            ("stone_01", 18, 21),
            ("bolt", 9, 32),
        ]
        first = pack_shelves(sizes, max_width=128)
        second = pack_shelves(list(reversed(sizes)), max_width=128)
        self.assertEqual(first, second)
        _, _, placements = first
        rects = list(placements.values())
        for index, (ax, ay, aw, ah) in enumerate(rects):
            for bx, by, bw, bh in rects[index + 1 :]:
                overlaps = ax < bx + bw and ax + aw > bx and ay < by + bh and ay + ah > by
                self.assertFalse(overlaps)

    def test_geometry_template_stays_unapproved(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "geometry.json"
            write_geometry_template(MANIFEST_TEMPLATE, output, 1024, 1024)
            geometry = self.load_json(output)
        self.assertEqual(geometry["status"], "draft_geometry")
        self.assertFalse(geometry["master"]["approved"])
        self.assertEqual(len(geometry["layers"]), 133)
        self.assertTrue(all(value is None for value in geometry["anchors"].values()))
        self.assertTrue(
            all(item["masterPivotPx"] is None for item in geometry["layers"].values())
        )

    def test_review_builder_keeps_labels_out_of_composite(self):
        atlas = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        atlas.alpha_composite(Image.new("RGBA", (6, 8), (220, 120, 40, 255)), (2, 3))
        manifest = {
            "master": {"width": 24, "height": 24},
            "sprites": {
                "test_layer": {
                    "rect": [2, 3, 6, 8],
                    "pivotPx": [3, 4],
                    "masterPivotPx": [12, 12],
                    "drawOrder": 1,
                    "defaultVisible": True,
                }
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            review_path = Path(directory) / "review.png"
            composite_path = Path(directory) / "composite.png"
            build_review_grid(manifest, atlas, review_path, 64, 1)
            build_composite(manifest, atlas, composite_path)
            review = Image.open(review_path).convert("RGBA")
            composite = Image.open(composite_path).convert("RGBA")
            self.assertEqual(review.size, (64, 98))
            self.assertEqual(composite.size, (24, 24))
            self.assertEqual(composite.getbbox(), (9, 8, 15, 16))
            self.assertGreater(review.getbbox()[2], composite.getbbox()[2])

    def test_pending_visual_review_cannot_promote(self):
        review = self.load_json(REVIEW_TEMPLATE)
        errors, alpha_path, intake = validate_review(review)
        self.assertGreaterEqual(len(errors), 35)
        self.assertIsNone(alpha_path)
        self.assertIsNone(intake)
        self.assertTrue(any("userConfirmed must be true" in item for item in errors))
        self.assertTrue(any("trueTopDownOrthographic90 must be PASS" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
