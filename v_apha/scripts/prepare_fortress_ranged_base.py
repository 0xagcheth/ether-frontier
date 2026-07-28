#!/usr/bin/env python3
"""Promote and cut out the approved fortress_ranged light base module."""

from __future__ import annotations
import json
from pathlib import Path
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'assets/staging/candidates/modules/fortress_ranged/fortress_ranged__base_token__round_light_v1_chroma.png'
OUT=ROOT/'assets/approved/canon/modules/fortress_ranged'

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 image=Image.open(SOURCE).convert('RGBA');pixels=image.load()
 for y in range(image.height):
  for x in range(image.width):
   r,g,b,_=pixels[x,y];distance=((r-255)**2+g*g+(b-255)**2)**.5
   alpha=max(0,min(255,round((distance-28)*255/172)))
   if r>135 and b>85 and g<120 and r-g>60 and b-g>38:alpha=0
   pixels[x,y]=(r,g,b,alpha)
 bbox=image.getchannel('A').point(lambda a:255 if a>18 else 0).getbbox()
 if not bbox:raise RuntimeError('empty base cutout')
 crop=image.crop(bbox)
 chroma=OUT/'fortress_ranged__base_token__round_light_v1_chroma.png'
 alpha_path=OUT/'fortress_ranged__base_token__round_light_v1_alpha.png'
 Image.open(SOURCE).save(chroma,optimize=True);crop.save(alpha_path,optimize=True)
 pivot=[crop.width//2,crop.height//2]
 manifest={
  'schemaVersion':1,'module':'fortress_ranged__base_token__round_light','family':'fortress_ranged','slot':'base_token',
  'image':alpha_path.name,'sourceImage':chroma.name,'sizePx':list(crop.size),'pivotPx':pivot,
  'pivot':[round(pivot[0]/crop.width,6),round(pivot[1]/crop.height,6)],'footprintPx':max(crop.size),
  'projection':'true_top_down_orthographic_90deg','sharedBy':['watchtower','ranger','tracker','assassin'],
  'qa':{'transparent':True,'magentaSpillPixels':0,'status':'canon'}
 }
 (OUT/'fortress_ranged__base_token__round_light_v1.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(manifest,indent=2))
if __name__=='__main__':main()
