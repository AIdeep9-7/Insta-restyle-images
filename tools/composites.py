"""
Composite templates built from ONE photo (refs 8, 10, 11, 12).
All deterministic — no AI, no credits, face never drifts.
    python3 tools/composites.py photos/photo-A.jpg
"""
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import numpy as np, sys, os, random

def _mono(im, contrast=1.18, bright=1.0, grain=0):
    a=np.asarray(im.convert("RGB")).astype(np.float32)
    l=a.mean(axis=2,keepdims=True); im=Image.fromarray(np.clip(np.repeat(l,3,2),0,255).astype(np.uint8))
    im=ImageEnhance.Contrast(im).enhance(contrast); im=ImageEnhance.Brightness(im).enhance(bright)
    if grain:
        a=np.asarray(im).astype(np.float32)+np.random.default_rng(4).normal(0,grain,im.size[::-1])[...,None]
        im=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    return im

def _fit(im,W,H,cx=0.5,cy=0.42):
    w,h=im.size; tar=W/H
    if w/h>tar:
        nw=int(h*tar); x=int(cx*w-nw/2); x=max(0,min(w-nw,x)); im=im.crop((x,0,x+nw,h))
    else:
        nh=int(w/tar); y=int(cy*h-nh/2); y=max(0,min(h-nh,y)); im=im.crop((0,y,w,y+nh))
    return im.resize((W,H),Image.LANCZOS)

def _torn(w, amp=13, seed=1, step=17):
    """y-offsets for a ragged torn-paper edge."""
    r=random.Random(seed); pts=[]; x=0; y=r.uniform(-amp,amp)
    while x<w:
        pts.append((x,y)); x+=r.randint(step//2,step); y+=r.uniform(-amp*0.7,amp*0.7)
        y=max(-amp,min(amp,y))
    pts.append((w,y)); return pts

# ---------- REF 11 : three torn strips, colour middle ----------
def torn_strips(src,out,W=1080,hs=(500,470,500),border=26):
    heights=list(hs); gap=0
    inner=Image.new("RGB",(W,sum(heights)),(248,248,248))
    y=0
    for i,h in enumerate(heights):
        cy=[0.30,0.42,0.55][i]
        panel=_fit(src,W,h,cy=cy)
        panel = panel if i==1 else _mono(panel,1.16,1.02,5)
        if i==1:
            panel=ImageEnhance.Color(panel).enhance(1.30); panel=ImageEnhance.Brightness(panel).enhance(1.05)
        inner.paste(panel,(0,y)); y+=h
    # torn white edges between strips
    d=ImageDraw.Draw(inner)
    for i in range(1,len(heights)):
        yb=sum(heights[:i])
        pts=_torn(W,amp=15,seed=i*7)
        poly=[(x,yb+dy) for x,dy in pts]+[(W,yb+34),(0,yb+34)]
        d.polygon(poly,fill=(252,252,252))
        poly2=[(x,yb+dy-30) for x,dy in pts]+[(W,yb),(0,yb)]
        d.polygon(poly2,fill=(252,252,252))
    canvas=Image.new("RGB",(W+border*2,sum(heights)+border*2),(236,236,236))
    canvas.paste(inner,(border,border)); canvas.save(out,quality=93); return canvas.size

# ---------- REF 10 : hard colour block on B&W ----------
def colour_block(src,out,W=1080,H=1500,bx=(0.09,0.92),by=(0.27,0.55)):
    base=_mono(_fit(src,W,H,cy=0.40),1.22,1.03,9)
    x0,x1=int(W*bx[0]),int(W*bx[1]); y0,y1=int(H*by[0]),int(H*by[1])
    block=_fit(src,x1-x0,y1-y0,cy=0.34)
    block=ImageEnhance.Color(block).enhance(1.35); block=ImageEnhance.Contrast(block).enhance(1.06)
    block=ImageEnhance.Brightness(block).enhance(1.06)
    base.paste(block,(x0,y0))
    base.save(out,quality=94); return base.size

# ---------- REF 8 : blurred bg + rounded inset card + flower ----------
def inset_card(src,out,W=1080,H=1500):
    bg=_fit(src,W,H,cy=0.30).filter(ImageFilter.GaussianBlur(26))
    bg=ImageEnhance.Color(bg).enhance(0.55); bg=ImageEnhance.Brightness(bg).enhance(1.06)
    a=np.asarray(bg).astype(np.float32)
    a[...,0]*=1.03; a[...,2]*=0.86           # warm khaki cast
    bg=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    cw,chh=int(W*0.62),int(H*0.50); cx,cy=int(W*0.33),int(H*0.44)
    card=_fit(src,cw,chh,cy=0.40)
    card=ImageEnhance.Contrast(card).enhance(1.06); card=ImageEnhance.Color(card).enhance(1.08)
    mask=Image.new("L",(cw,chh),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,cw-1,chh-1],radius=int(min(cw,chh)*0.075),fill=255)
    sh=Image.new("RGBA",(cw+40,chh+40),(0,0,0,0))
    ImageDraw.Draw(sh).rounded_rectangle([20,20,cw+19,chh+19],radius=int(min(cw,chh)*0.075),fill=(0,0,0,70))
    sh=sh.filter(ImageFilter.GaussianBlur(14)); bg.paste(sh,(cx-20,cy-20),sh)
    bg.paste(card,(cx,cy),mask)
    try:
        sys.path.insert(0,"tools"); from sunflower import sunflower
        fl=sunflower(int(W*0.20)).rotate(-18,resample=Image.BICUBIC,expand=True)
        bg.paste(fl,(int(cx-fl.width*0.62),int(cy-fl.height*0.42)),fl)
    except Exception as e: print("flower skipped:",e)
    bg.save(out,quality=94); return bg.size

# ---------- REF 12 : full editorial IG-post poster ----------
MONT="/usr/lib/R/library/grDevices/fonts/Montserrat/static/Montserrat-%s.ttf"
def _f(style,size):
    from PIL import ImageFont
    for p in (MONT%style, MONT%"Medium", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try: return ImageFont.truetype(p,size)
        except Exception: continue
    return ImageFont.load_default()

def cutout(src_path, out_png="results/cutout.png", model="u2netp"):
    """Subject cut-out via rembg (light model, fits in 2GB RAM)."""
    from rembg import remove, new_session
    im=Image.open(src_path).convert("RGB"); w,h=im.size
    o=remove(im, session=new_session(model)).resize((w,h),Image.LANCZOS)
    o.save(out_png); return o

def poster(src,out,W=1080,H=1560,cut=None,handle="yourname_",song="Now playing",
           bigtext="RUKMINI",sig="signature",footer="W O M E N   A E S T H E T I C S"):
    from PIL import ImageFont
    # 1. blurred greyscale wall
    bg=_fit(src,W,H,cy=0.22).filter(ImageFont and ImageFilter.GaussianBlur(34))
    bg=_mono(bg,0.95,1.22,0)
    a=np.asarray(bg).astype(np.float32); a=a*0.80+52
    bg=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    d=ImageDraw.Draw(bg)

    # 2. the mock Instagram post
    pw=int(W*0.62); px=int(W*0.19)
    barh=int(H*0.052); py=int(H*0.155); ph=int(H*0.545)
    d.rectangle([px,py,px+pw,py+barh],fill=(12,12,12))                # header
    inner=_fit(src,pw,ph,cy=0.55).filter(ImageFilter.GaussianBlur(16))
    inner=ImageEnhance.Color(inner).enhance(0.22)
    inner=ImageEnhance.Brightness(inner).enhance(1.10)
    ia=np.asarray(inner).astype(np.float32)
    ia[...,0]=ia[...,0]*0.92+38; ia[...,1]=ia[...,1]*0.86+26; ia[...,2]=ia[...,2]*0.86+30
    inner=Image.fromarray(np.clip(ia,0,255).astype(np.uint8))          # blush wash
    bg.paste(inner,(px,py+barh))
    footh=int(H*0.050); fy=py+barh+ph
    d.rectangle([px,fy,px+pw,fy+footh],fill=(12,12,12))                # action bar

    # header text
    av=_fit(src,int(barh*0.62),int(barh*0.62),cy=0.24)
    m=Image.new("L",av.size,0); ImageDraw.Draw(m).ellipse([0,0,av.size[0]-1,av.size[1]-1],fill=255)
    bg.paste(av,(px+int(barh*0.22),py+int(barh*0.19)),m)
    d.text((px+int(barh*1.05),py+int(barh*0.16)),handle,font=_f("Bold",int(barh*0.32)),fill=(245,245,245))
    nf=_f("Medium",int(barh*0.26))
    d.text((px+int(barh*1.05)+int(barh*0.30),py+int(barh*0.58)),song,font=nf,fill=(205,205,205))
    # note glyph drawn, not typed
    nx,ny=px+int(barh*1.06),py+int(barh*0.62); r=max(2,int(barh*0.075))
    d.ellipse([nx,ny+r*2,nx+r*2,ny+r*4],fill=(205,205,205))
    d.rectangle([nx+r*2-1,ny,nx+r*2+1,ny+r*3],fill=(205,205,205))
    # kebab menu
    kx=px+pw-int(barh*0.42); dr=max(2,int(barh*0.045))
    for t in range(3):
        ky=py+barh*0.34+t*dr*2.6
        d.ellipse([kx,ky,kx+dr,ky+dr],fill=(235,235,235))

    # action bar: heart, comment+count, share+count, bookmark
    cy_=fy+footh//2; fs=int(footh*0.32); fnt=_f("Medium",fs)
    W_=max(2,int(footh*0.055))
    # heart (two circles + triangle)
    hx=px+int(footh*0.55); hs=int(footh*0.30); R=(230,42,60)
    d.ellipse([hx,cy_-hs*0.85,hx+hs,cy_+hs*0.15],fill=R)
    d.ellipse([hx+hs*0.80,cy_-hs*0.85,hx+hs*1.80,cy_+hs*0.15],fill=R)
    d.polygon([(hx-hs*0.02,cy_-hs*0.18),(hx+hs*1.82,cy_-hs*0.18),(hx+hs*0.90,cy_+hs*1.05)],fill=R)
    # comment bubble
    cx2=hx+int(footh*1.30)
    d.ellipse([cx2,cy_-hs*0.80,cx2+hs*1.7,cy_+hs*0.70],outline=(235,235,235),width=W_)
    d.polygon([(cx2+hs*0.35,cy_+hs*0.55),(cx2+hs*0.85,cy_+hs*0.55),(cx2+hs*0.30,cy_+hs*1.15)],fill=(235,235,235))
    d.text((cx2+hs*2.1,cy_-fs*0.55),"2,211",font=fnt,fill=(235,235,235))
    # repost arrows
    sx=cx2+int(footh*2.45)
    d.line([(sx,cy_-hs*0.35),(sx+hs*1.5,cy_-hs*0.35)],fill=(235,235,235),width=W_)
    d.polygon([(sx+hs*1.5,cy_-hs*0.70),(sx+hs*1.5,cy_),(sx+hs*1.95,cy_-hs*0.35)],fill=(235,235,235))
    d.line([(sx+hs*0.45,cy_+hs*0.55),(sx+hs*1.95,cy_+hs*0.55)],fill=(235,235,235),width=W_)
    d.polygon([(sx+hs*0.45,cy_+hs*0.20),(sx+hs*0.45,cy_+hs*0.90),(sx,cy_+hs*0.55)],fill=(235,235,235))
    d.text((sx+hs*2.5,cy_-fs*0.55),"880",font=fnt,fill=(235,235,235))
    # bookmark
    bxx=px+pw-int(footh*0.95)
    d.polygon([(bxx,cy_-hs*0.85),(bxx+hs*1.1,cy_-hs*0.85),(bxx+hs*1.1,cy_+hs*0.95),
               (bxx+hs*0.55,cy_+hs*0.35),(bxx,cy_+hs*0.95)],outline=(235,235,235),width=W_)

    # 3. big semi-transparent type BEHIND the subject
    tl=Image.new("RGBA",(W,H),(0,0,0,0)); td=ImageDraw.Draw(tl)
    bt=(bigtext or "").upper(); half=(len(bt)+1)//2
    bf=_f("Bold",int(W*0.125))
    for n,ln in enumerate((bt[:half],bt[half:])):
        if not ln: continue
        lw=td.textlength(ln,font=bf)
        td.text((min(int(W*0.72),W-lw-int(W*0.02)),int(H*(0.345+n*0.078))),ln,font=bf,fill=(255,255,255,145))
    bg=Image.alpha_composite(bg.convert("RGBA"),tl).convert("RGB")
    _sig_layer=(sig,)

    # 4. the subject cut out, BREAKING OUT of the post frame
    if cut is not None:
        # trim to the alpha bounding box so scaling is about the SUBJECT, not the canvas
        bb=cut.split()[3].getbbox()
        if bb: cut=cut.crop(bb)
        ch=int(H*0.66); cwd=int(cut.width*ch/cut.height)
        if cwd>int(W*0.56):
            cwd=int(W*0.56); ch=int(cut.height*cwd/cut.width)
        c=cut.resize((cwd,ch),Image.LANCZOS)
        ca=np.asarray(c).astype(np.float32)
        ca[...,0]=np.clip(ca[...,0]*1.04+6,0,255); ca[...,2]=np.clip(ca[...,2]*0.97,0,255)
        c=Image.fromarray(ca.astype(np.uint8),"RGBA")
        sh=Image.new("RGBA",(cwd+60,ch+60),(0,0,0,0))
        sh.paste(Image.new("RGBA",(cwd,ch),(0,0,0,110)),(30,30),c.split()[3])
        sh=sh.filter(ImageFilter.GaussianBlur(22))
        cx3=int(W*0.58-cwd*0.50); cy3=int(H*0.295)
        bg.paste(sh,(cx3-30,cy3-30),sh)
        bg.paste(c,(cx3,cy3),c)

    # 5. signature script, on top, bottom-left and always inside the frame
    if sig:
        sl=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(sl)
        sf=_f("BoldItalic",int(W*0.058))
        sw2=sd.textlength(sig,font=sf)
        sd.text((max(int(W*0.06),min(int(W*0.20),W-sw2-int(W*0.06))),int(H*0.845)),
                sig,font=sf,fill=(25,20,24,150))
        bg=Image.alpha_composite(bg.convert("RGBA"),sl).convert("RGB")

    # 6. three eye strips ON TOP
    sw,shh=int(W*0.235),int(H*0.033)
    w0,h0=src.size; ew=int(w0*0.30); eh=max(1,int(ew*shh/sw))
    ex0=max(0,min(w0-ew,int(w0*0.47-ew/2))); ey0=max(0,min(h0-eh,int(h0*0.240-eh/2)))
    eyes=_mono(src.crop((ex0,ey0,ex0+ew,ey0+eh)).resize((sw,shh),Image.LANCZOS),1.36,0.94,0)
    for ex,ey in [(int(W*0.035),int(H*0.300)),(int(W*0.735),int(H*0.470)),(int(W*0.020),int(H*0.560))]:
        fr=Image.new("RGB",(sw+10,shh+10),(10,10,10)); fr.paste(eyes,(5,5))
        bg.paste(fr,(ex,ey))

    # 7. footer
    d=ImageDraw.Draw(bg)
    ff=_f("Medium",int(W*0.021))
    tw=d.textlength(footer,font=ff)
    d.text(((W-tw)/2,int(H*0.955)),footer,font=ff,fill=(238,238,238))
    bg.save(out,quality=94); return bg.size

if __name__=="__main__":
    src_path=sys.argv[1] if len(sys.argv)>1 else "photos/photo-A.jpg"
    src=Image.open(src_path).convert("RGB")
    os.makedirs("out_composites",exist_ok=True)
    print("torn strips ",torn_strips(src,"out_composites/torn-strips.jpg"))
    print("colour block",colour_block(src,"out_composites/colour-block.jpg"))
    print("inset card  ",inset_card(src,"out_composites/inset-card.jpg"))
    try:
        cut=cutout(src_path,"out_composites/_cutout.png")
    except Exception as e:
        print("cutout unavailable (pip install rembg onnxruntime):",e); cut=None
    print("poster      ",poster(src,"out_composites/poster.jpg",cut=cut))
