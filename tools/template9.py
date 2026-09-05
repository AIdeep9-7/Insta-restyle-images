"""Template 9 — Vintage Sepia + Eye Band + Sunflower stickers. Pure code, zero AI."""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw
import numpy as np, sys
sys.path.insert(0,"tools")
from sunflower import sunflower

def build(src_path, out_path, eye_cy_frac, eye_dx_frac, band_pad=0.055):
    src=Image.open(src_path).convert("RGB"); W,H=src.size
    eye_cy=eye_cy_frac*H; eye_dx=eye_dx_frac*W
    band_h=int(eye_dx*0.90); top=int(eye_cy-band_h*0.52); bot=top+band_h
    bx0=int(W*band_pad); bx1=int(W*(1-band_pad))

    # ---- sepia base ----
    b=src.copy()
    b=ImageEnhance.Color(b).enhance(0.12)
    b=ImageEnhance.Contrast(b).enhance(1.02)
    b=ImageEnhance.Brightness(b).enhance(0.74)
    a=np.asarray(b).astype(np.float32)
    lum=a.mean(axis=2,keepdims=True)
    sep=np.concatenate([lum*1.14+10, lum*0.95+2, lum*0.68-4],axis=2)
    sep=np.clip(sep,0,255)
    sep=sep*0.86+18                      # lifted milky blacks
    rng=np.random.default_rng(11)
    sep=sep+rng.normal(0,13,sep.shape[:2])[...,None]
    sep=np.clip(sep,0,255).astype(np.uint8)
    base=Image.fromarray(sep)
    # vertical scratches
    d=ImageDraw.Draw(base,"RGBA")
    for x,al in [(0.17,52),(0.38,34),(0.63,60),(0.79,30),(0.91,44)]:
        d.line([(int(W*x),0),(int(W*x)+rng.integers(-3,4),H)],fill=(255,246,224,al),width=1)
    for y,al in [(0.22,26),(0.71,20)]:
        d.line([(0,int(H*y)),(W,int(H*y)+rng.integers(-2,3))],fill=(250,238,214,al),width=1)
    base=base.filter(ImageFilter.GaussianBlur(0.4))

    # ---- eye band: original pixels, warmer + brighter ----
    band=src.crop((bx0,top,bx1,bot))
    band=ImageEnhance.Brightness(band).enhance(1.16)
    band=ImageEnhance.Color(band).enhance(0.62)
    ab=np.asarray(band).astype(np.float32)
    ab[...,0]=np.clip(ab[...,0]*1.24+18,0,255)
    ab[...,1]=np.clip(ab[...,1]*1.02+4,0,255)
    ab[...,2]=np.clip(ab[...,2]*0.70,0,255)
    band=Image.fromarray(np.clip(ab,0,255).astype(np.uint8))
    band=ImageEnhance.Contrast(band).enhance(1.14)
    band=band.filter(ImageFilter.UnsharpMask(radius=2,percent=70,threshold=2))

    out=base.copy(); out.paste(band,(bx0,top))

    # ---- sunflower stickers ----
    fl=sunflower(int(W*0.235))
    f2=sunflower(int(W*0.155),seed=8).rotate(-24,resample=Image.BICUBIC,expand=True)
    f3=sunflower(int(W*0.135),seed=21).rotate(37,resample=Image.BICUBIC,expand=True)
    out.paste(fl,(int(W*-0.035), int(top-fl.height*0.70)), fl)         # hugs left edge
    out.paste(f2,(int(W*0.125), int(top-f2.height*0.86)), f2)          # partner bloom, above band
    out.paste(f3,(int(W*0.865), int(bot-f3.height*0.30)), f3)          # right edge
    out.save(out_path,quality=95)
    return out.size

if __name__=="__main__":
    # Photo A eye metrics measured earlier: cy=344/1434, eye spacing=132/1080
    print(build("uploads/IMG_20260603_213949_951.jpg","results/T9-sepia-sunflower-A.jpg",
                344.3/1434, 132.0/1080))
