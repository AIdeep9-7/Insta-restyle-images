"""
SINGLE-SOURCE MULTI-PANEL BUILDER
=================================
Problem: Type B references (refs 2, 4, 5, 6, 11) are 3-4 stills from a VIDEO.
If you only have ONE photo, you cannot get different poses.

Solution: stop trying to fake different poses. Instead build the panel set from
DIFFERENT CROPS of the same photo, at different scales and grades. Real editors do
exactly this — refs 2 and 6 are largely crop-variation, not pose-variation.

Three strategies:
  ZOOM   : wide -> medium -> tight on the same subject (a 'push in')
  DETAIL : eyes band / lips band / jewellery band  (macro study, like ref 2)
  MIXED  : portrait, eyes-only band, portrait (like ref 6)
"""
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def _grade(im, warm=1.0, sat=1.0, bright=1.0, contrast=1.0, grain=0, bw=False, blur=0):
    if bw:
        a=np.asarray(im.convert("RGB")).astype(np.float32)
        l=a.mean(axis=2,keepdims=True)
        im=Image.fromarray(np.clip(np.repeat(l,3,axis=2),0,255).astype(np.uint8))
    im=ImageEnhance.Color(im).enhance(sat)
    im=ImageEnhance.Brightness(im).enhance(bright)
    im=ImageEnhance.Contrast(im).enhance(contrast)
    if warm!=1.0:
        a=np.asarray(im).astype(np.float32)
        a[...,0]=np.clip(a[...,0]*warm,0,255); a[...,2]=np.clip(a[...,2]*(2-warm),0,255)
        im=Image.fromarray(a.astype(np.uint8))
    if blur: im=im.filter(ImageFilter.GaussianBlur(blur))
    if grain:
        a=np.asarray(im).astype(np.float32)
        a=a+np.random.default_rng(5).normal(0,grain,a.shape[:2])[...,None]
        im=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    return im

def _crop(src, cx, cy, zoom, W, H):
    """cx,cy fractional centre; zoom 1.0 = full height."""
    sw,sh=src.size; tar=W/H
    ch=sh/zoom; cw=ch*tar
    if cw>sw: cw=sw; ch=cw/tar
    x=cx*sw-cw/2; y=cy*sh-ch/2
    x=max(0,min(sw-cw,x)); y=max(0,min(sh-ch,y))
    return src.crop((int(x),int(y),int(x+cw),int(y+ch))).resize((W,H),Image.LANCZOS)

def build(src_path, out_path, strategy="zoom", face=(0.47,0.24), eyes=0.24,
          lips=0.33, W=1080, panel_h=560, gap=5, gap_col=(12,10,9), sharpen=True):
    src=Image.open(src_path).convert("RGB")
    fx,fy=face
    if strategy=="zoom":
        specs=[ (fx,fy+0.22,1.05, dict(warm=1.06,sat=1.05,bright=1.02,contrast=1.05,grain=5)),
                (fx,fy+0.02,2.10, dict(warm=1.08,sat=1.08,bright=1.05,contrast=1.07,grain=5)),
                (fx,fy-0.02,4.20, dict(warm=1.05,sat=1.02,bright=1.04,contrast=1.11,grain=6)) ]
    elif strategy=="detail":
        # extreme macro — each panel is a genuinely different feature
        specs=[ (fx+0.012,eyes-0.004, 9.5, dict(bw=True,contrast=1.34,bright=1.06,grain=10)),  # one eye
                (fx-0.055,eyes+0.030, 7.0, dict(bw=True,contrast=1.28,bright=1.00,grain=10)),  # ear + earring
                (fx+0.020,lips+0.012, 8.0, dict(bw=True,contrast=1.26,bright=1.02,grain=10)),  # lips
                (fx-0.010,lips+0.085, 5.2, dict(bw=True,contrast=1.22,bright=0.96,grain=9)) ]  # jaw/neck
    else: # mixed
        specs=[ (fx,fy+0.02, 1.55,dict(warm=1.05,sat=1.04,bright=1.04,contrast=1.04,grain=5)),
                (fx,eyes,    6.8, dict(warm=1.04,sat=1.02,bright=1.09,contrast=1.12,grain=5)),
                (fx,fy-0.01, 2.30,dict(warm=1.05,sat=1.04,bright=1.02,contrast=1.05,grain=5)) ]
    ims=[]
    for cx,cy,z,g in specs:
        im=_crop(src,cx,cy,z,W,panel_h)
        im=_grade(im,**g)
        if sharpen: im=im.filter(ImageFilter.UnsharpMask(radius=2,percent=55,threshold=3))
        ims.append(im)
    n=len(ims)
    out=Image.new("RGB",(W,panel_h*n+gap*(n-1)),gap_col)
    for i,im in enumerate(ims): out.paste(im,(0,i*(panel_h+gap)))
    out.save(out_path,quality=94)
    return out.size

if __name__=="__main__":
    A="uploads/IMG_20260603_213949_951.jpg"
    print("zoom  ",build(A,"results/T-stack-zoom-A.jpg","zoom",  face=(0.47,0.245),eyes=0.240,lips=0.330))
    print("detail",build(A,"results/T-stack-detail-A.jpg","detail",face=(0.47,0.245),eyes=0.240,lips=0.330,panel_h=430))
    print("mixed ",build(A,"results/T-stack-mixed-A.jpg","mixed", face=(0.47,0.245),eyes=0.240,lips=0.330))
