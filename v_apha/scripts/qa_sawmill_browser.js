const fs = require("fs");
const { chromium } = require("/Users/agch/.codex/skills/develop-web-game/node_modules/playwright");

(async () => {
  const building = process.argv[2] || "sawmill";
  const action = process.argv[3] || "destroy";
  const browser = await chromium.launch({
    headless: true,
    args: ["--use-gl=angle", "--use-angle=swiftshader"],
  });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  const errors = [];
  page.on("console", (msg) => {
    if (msg.type() === "error") errors.push({ type: "console.error", text: msg.text() });
  });
  page.on("pageerror", (err) => errors.push({ type: "pageerror", text: String(err) }));

  await page.goto("http://127.0.0.1:4173/sprite-lab/", { waitUntil: "domcontentloaded" });
  await page.click(`[data-building="${building}"]`);
  await page.click(`[data-building-action="${action}"]`);
  await page.waitForTimeout(action === "destroy" ? 2100 : 900);

  fs.mkdirSync("output/web-game", { recursive: true });
  await page.screenshot({ path: `output/web-game/${building}-${action}.png`, fullPage: false });
  const state = await page.evaluate(() => window.render_game_to_text && window.render_game_to_text());
  fs.writeFileSync(`output/web-game/${building}-${action}-state.json`, state || "null");
  if (errors.length) {
    fs.writeFileSync(`output/web-game/${building}-${action}-errors.json`, JSON.stringify(errors, null, 2));
  }
  await browser.close();
})();
