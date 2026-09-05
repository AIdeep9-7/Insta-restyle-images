from PIL import Image, ImageDraw
import math, random

def sunflower(size=400, seed=3):
    S=size*4
    im=Image.new("RGBA",(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    cx=cy=S/2
    r_in=S*0.155           # centre disc radius
    R=S*0.485              # petal tip radius
    def petals(n, rot, col, tip, width, length):
        for i in range(n):
            a=math.radians(i*360.0/n+rot)
            ca,sa=math.cos(a),math.sin(a)
            pts=[]; steps=26
            L=r_in*0.9+(length-r_in*0.9)
            for k in range(steps+1):
                s=k/steps
                rad=r_in*0.85+(L-r_in*0.85)*s
                # narrow at base, widest ~40%, pointed tip
                w=width*(math.sin(math.pi*min(s*1.12,1.0))**0.62)*(1-s*0.25)
                pts.append((cx+rad*ca-w*sa, cy+rad*sa+w*ca))
            pts.append((cx+tip*ca, cy+tip*sa))
            for k in range(steps,-1,-1):
                s=k/steps
                rad=r_in*0.85+(L-r_in*0.85)*s
                w=width*(math.sin(math.pi*min(s*1.12,1.0))**0.62)*(1-s*0.25)
                pts.append((cx+rad*ca+w*sa, cy+rad*sa-w*ca))
            d.polygon(pts,fill=col)
    petals(13, 13.8, (231,150,22), R*0.93, S*0.058, R*0.93)   # back
    petals(13, 0.0,  (250,193,44), R,      S*0.062, R)        # front
    d.ellipse([cx-r_in,cy-r_in,cx+r_in,cy+r_in],fill=(96,60,28))
    d.ellipse([cx-r_in*0.88,cy-r_in*0.88,cx+r_in*0.88,cy+r_in*0.88],fill=(72,44,20))
    rnd=random.Random(seed)
    for i in range(230):
        aa=rnd.random()*math.pi*2; rr=math.sqrt(rnd.random())*r_in*0.80
        x=cx+rr*math.cos(aa); y=cy+rr*math.sin(aa); s=S*0.0075
        d.ellipse([x-s,y-s,x+s,y+s],fill=(126,84,36))
    return im.resize((size,size),Image.LANCZOS)

if __name__=="__main__":
    sunflower(400).save("tools/sunflower.png"); print("ok")
