#!/usr/bin/env python3
"""Extract and pack the post-reset Watchtower component sheet."""

from __future__ import annotations
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'assets/source/watchtower/watchtower_layered_source_v1_chroma.png'
OUT=ROOT/'assets/runtime/atlases/watchtower'
LAYERS=OUT/'layers'

REGIONS={
 'base_stone_wood_platform':(18,18,590,575),
 'central_rotation_socket':(620,120,865,360),
 'crossbow_rotatable':(900,15,1510,555),
 'pennant_mount':(630,380,785,530),
 'flag_pennant_01':(395,545,670,690),'flag_pennant_02':(675,545,960,690),
 'flag_pennant_03':(965,545,1235,690),'flag_pennant_04':(1235,545,1500,690),
 'lantern_housing_topdown':(25,690,205,865),
 'lantern_glow_01':(225,700,365,855),'lantern_glow_02':(350,700,500,855),
 'lantern_glow_03':(495,700,645,855),'lantern_glow_04':(625,690,790,860),
 'muzzle_flash_01':(895,725,1005,840),'muzzle_flash_02':(1010,715,1145,840),
 'muzzle_flash_03':(1150,700,1320,845),'muzzle_flash_04':(1315,690,1515,850),
 'projectile_bolt':(45,875,415,1005),
 'destroy_debris_01':(445,870,565,1010),'destroy_debris_02':(565,875,680,1010),
 'destroy_debris_03':(680,880,795,1010),'destroy_debris_04':(790,875,955,1010),
 'destroy_debris_05':(945,885,1045,1010),'destroy_debris_06':(1035,875,1140,1010),
 'destroy_debris_07':(1125,875,1245,1010),'destroy_debris_08':(1235,875,1350,1010),
 'destroy_debris_09':(1340,870,1435,1010),'destroy_debris_10':(1420,875,1515,1010),
}

def key(image):
 image=image.convert('RGBA'); px=image.load()
 for y in range(image.height):
  for x in range(image.width):
   r,g,b,_=px[x,y]; dist=((r-255)**2+g*g+(b-255)**2)**.5
   a=max(0,min(255,round((dist-30)*255/170)))
   if r>135 and b>85 and g<120 and r-g>60 and b-g>38:a=0
   px[x,y]=(r,g,b,a)
 return image

def largest(image, threshold=20):
 alpha=image.getchannel('A');p=alpha.load();seen=set();best=[]
 for y in range(image.height):
  for x in range(image.width):
   if p[x,y]<threshold or (x,y) in seen:continue
   stack=[(x,y)];seen.add((x,y));points=[]
   while stack:
    qx,qy=stack.pop();points.append((qx,qy))
    for nx,ny in ((qx+1,qy),(qx-1,qy),(qx,qy+1),(qx,qy-1)):
     if 0<=nx<image.width and 0<=ny<image.height and (nx,ny) not in seen and p[nx,ny]>=threshold:
      seen.add((nx,ny));stack.append((nx,ny))
   if len(points)>len(best):best=points
 xs=[q[0] for q in best];ys=[q[1] for q in best];box=(min(xs),min(ys),max(xs)+1,max(ys)+1)
 out=Image.new('RGBA',(box[2]-box[0],box[3]-box[1]),(0,0,0,0));src=image.load();dst=out.load()
 for x,y in best:dst[x-box[0],y-box[1]]=src[x,y]
 return out

def crop(source,box):
 im=source.crop(box);bbox=im.getchannel('A').point(lambda a:255 if a>18 else 0).getbbox()
 if not bbox:raise ValueError(box)
 return largest(im.crop(bbox))

def pivot(name,size):
 w,h=size
 if name.startswith('flag_pennant'):return [0,h//2]
 if name.startswith('muzzle_flash'):return [0,h//2]
 return [w//2,h//2]

def main():
 OUT.mkdir(parents=True,exist_ok=True);LAYERS.mkdir(exist_ok=True)
 alpha=key(Image.open(SOURCE));alpha.save(OUT/'watchtower_layered_source_v1_alpha.png',optimize=True)
 parts={n:crop(alpha,b) for n,b in REGIONS.items()}
 for name,im in parts.items():im.save(LAYERS/f'{name}.png',optimize=True)
 width=1536;pad=8;x=y=pad;row=0;positions={}
 for name in sorted(parts,key=lambda n:(-parts[n].height,-parts[n].width,n)):
  im=parts[name]
  if x+im.width+pad>width:x=pad;y+=row+pad;row=0
  positions[name]=(x,y);x+=im.width+pad;row=max(row,im.height)
 atlas=Image.new('RGBA',(width,y+row+pad),(0,0,0,0));sprites={}
 for name,im in parts.items():
  x,y=positions[name];atlas.alpha_composite(im,(x,y));p=pivot(name,im.size)
  sprites[name]={'file':f'layers/{name}.png','rect':{'x':x,'y':y,'w':im.width,'h':im.height},'pivotPx':p,'pivot':[round(p[0]/im.width,5),round(p[1]/im.height,5)]}
 runtime=OUT/'watchtower_layered_runtime.png';atlas.save(runtime,optimize=True)
 names=list(parts);cols=4;cw,ch=390,260;rows=(len(names)+cols-1)//cols
 review=Image.new('RGBA',(cols*cw,rows*ch),(38,30,42,255));d=ImageDraw.Draw(review);font=ImageFont.load_default()
 for i,name in enumerate(names):
  ox=(i%cols)*cw;oy=(i//cols)*ch;d.rectangle((ox,oy,ox+cw-1,oy+ch-1),outline=(135,105,145,255),width=2);d.text((ox+9,oy+9),name,font=font,fill=(255,232,170,255))
  im=parts[name];scale=min(1,(cw-24)/im.width,(ch-44)/im.height);shown=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
  px=ox+(cw-shown.width)//2;py=oy+30+(ch-35-shown.height)//2;review.alpha_composite(shown,(px,py));p=pivot(name,im.size);cx=px+round(p[0]*scale);cy=py+round(p[1]*scale);d.line((cx-7,cy,cx+7,cy),fill='cyan',width=2);d.line((cx,cy-7,cx,cy+7),fill='cyan',width=2)
 review.save(OUT/'watchtower_layered_review_grid.png',optimize=True)
 manifest={'schemaVersion':2,'object':'watchtower','pipeline':'layered-object-v2-restart','image':runtime.name,'atlasSize':list(atlas.size),'sourceImage':'../../source/watchtower/watchtower_layered_source_v1_chroma.png','sprites':sprites,'anchors':{'objectCenter':{'parent':'base_stone_wood_platform','normalized':[.5,.5]},'weaponSocket':{'parent':'central_rotation_socket','normalized':[.5,.5]},'flagMount':{'parent':'pennant_mount','normalized':[.5,.5]},'lanternCore':{'parent':'lantern_housing_topdown','normalized':[.5,.5]},'muzzle':{'parent':'crossbow_rotatable','normalized':[1,.5]}},'drawOrder':['base_stone_wood_platform','central_rotation_socket','pennant_mount','flag_pennant_*','lantern_housing_topdown','lantern_glow_*','crossbow_rotatable','muzzle_flash_*'],'animations':{'idle':{'flagFrames':[f'flag_pennant_{i:02d}' for i in range(1,5)],'glowFrames':[f'lantern_glow_{i:02d}' for i in range(1,5)],'frameDurationMs':160,'loop':True},'attack':{'flashFrames':[f'muzzle_flash_{i:02d}' for i in range(1,5)],'frameDurationMs':80,'loop':False},'destroy':{'pieces':[f'destroy_debris_{i:02d}' for i in range(1,11)],'loop':False},'projectile':{'sprite':'projectile_bolt','rotation':'alongTrajectory'}},'runtimeTransforms':{'crossbow_rotatable':{'rotation':'towardTarget','anchor':'weaponSocket'},'flag_pennant_*':{'anchor':'flagMount'},'lantern_glow_*':{'anchor':'lanternCore'},'muzzle_flash_*':{'anchor':'muzzle','inheritRotation':True}},'qa':{'oneObjectFamily':True,'transparentRuntime':True,'bakedCompositeFrames':False,'fileSizeBytes':runtime.stat().st_size,'under5MB':runtime.stat().st_size<5_000_000}}
 (OUT/'watchtower_layered_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'atlas':str(runtime),'size':atlas.size,'bytes':runtime.stat().st_size,'sprites':len(parts)},indent=2))
if __name__=='__main__':main()
