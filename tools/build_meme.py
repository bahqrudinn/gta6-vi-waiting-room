from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import random, math

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1200, 1500
random.seed(17)

# Rich twilight gradient.
im = Image.new('RGB', (W, H))
pix = im.load()
for y in range(H):
    t = y / (H - 1)
    stops = [(0.0, (13, 9, 26)), (0.40, (42, 17, 65)), (0.72, (100, 34, 84)), (1.0, (17, 12, 33))]
    for i in range(len(stops)-1):
        if stops[i][0] <= t <= stops[i+1][0]:
            a, ca = stops[i]; b, cb = stops[i+1]
            f = (t-a)/(b-a)
            col = tuple(round(ca[k]*(1-f)+cb[k]*f) for k in range(3))
            break
    for x in range(W):
        glow = max(0, 1-math.sqrt(((x-750)/680)**2 + ((y-700)/540)**2))
        pix[x,y] = tuple(min(255, int(col[k] + glow*(34 if k == 0 else 23 if k == 1 else 21))) for k in range(3))
d = ImageDraw.Draw(im, 'RGBA')

font_reg='/system/fonts/RobotoStatic-Regular.ttf'
font_bold='/system/fonts/DroidSans-Bold.ttf'
def F(sz, bold=False): return ImageFont.truetype(font_bold if bold else font_reg, sz)
def text(xy, s, size, fill, bold=False, anchor=None, stroke_width=0, stroke_fill=None):
    d.text(xy, s, font=F(size,bold), fill=fill, anchor=anchor, stroke_width=stroke_width, stroke_fill=stroke_fill)
def rounded(box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius, fill=fill, outline=outline, width=width)
def line(points, fill, width=1): d.line(points, fill=fill, width=width, joint='curve')

# Fine stars and gridlike distant lights.
for _ in range(95):
    x=random.randrange(35,1165); y=random.randrange(320,760)
    r=random.choice([1,1,2]); d.ellipse((x-r,y-r,x+r,y+r), fill=(255,211,232,random.randrange(40,125)))

# Header pill and editorial title.
rounded((72,56,405,101),22,(255,255,255,17),(255,255,255,52),1)
text((93,68),'LEONIDA  /  WAITING ROOM',19,(255,224,239,245),True)
text((1128,68),'ISSUE 013',18,(248,193,224,210),True,anchor='ra')
text((72,130),'13 YEARS.',104,(255,251,248,255),True)
text((72,242),'STILL WAITING.',79,(255,128,196,255),True)
text((77,343),'GTA VI has the longest queue in Leonida.',28,(236,220,238,245))

# Sun glow and sunset disc.
for rad, alpha in [(270,15),(235,20),(205,28)]:
    d.ellipse((760-rad,620-rad,760+rad,620+rad),fill=(255,118,168,alpha))
sun=Image.new('RGBA',(420,420),(0,0,0,0)); sd=ImageDraw.Draw(sun)
for yy in range(400):
    f=yy/399
    c=(255, int(191-92*f), int(133-31*f), 255)
    sd.line((0,yy,420,yy), fill=c)
mask=Image.new('L',(420,420),0); ImageDraw.Draw(mask).ellipse((10,10,410,410),fill=255)
sun.putalpha(mask); im.paste(sun,(550,415),sun); d=ImageDraw.Draw(im,'RGBA')
# Sunset stripes, iconic but generic.
for yy in [685,703,725,749]:
    d.rounded_rectangle((568,yy,952,yy+7),3,fill=(69,25,73,150))
# Palm trunks and leaves.
line([(210,772),(247,565),(274,474)],(31,19,41,255),13)
for angle in [-150,-125,-100,-72,-45,-20,8]:
    rad=math.radians(angle); ex=274+math.cos(rad)*130; ey=474+math.sin(rad)*83
    line([(274,474),(ex,ey)],(26,31,45,255),10)
    for q in range(1,5):
        xx=274+(ex-274)*q/5; yy=474+(ey-474)*q/5
        d.ellipse((xx-12,yy+3,xx+13,yy+17),fill=(36,93,85,220))
line([(1060,803),(1043,621),(1030,532)],(28,17,40,255),12)
for angle in [-155,-128,-99,-69,-38,-9,16]:
    rad=math.radians(angle); ex=1030+math.cos(rad)*100; ey=532+math.sin(rad)*70
    line([(1030,532),(ex,ey)],(23,38,54,255),8)

# Neon skyline silhouettes.
for x,w,h in [(0,92,168),(83,112,260),(179,75,187),(254,100,295),(350,78,218),(418,92,268),(493,75,198),(890,82,194),(960,102,305),(1052,71,215),(1114,86,270)]:
    top=793-h
    d.rectangle((x,top,x+w,808),fill=(22,15,39,245))
    # roofs and lit windows
    if w>85: d.rectangle((x+15,top-13,x+w-13,top),fill=(22,15,39,245))
    for wx in range(x+15,x+w-8,23):
        for wy in range(top+25,790,36):
            if random.random()<.43:
                d.rounded_rectangle((wx,wy,wx+7,wy+13),2,fill=random.choice([(255,173,127,190),(255,118,196,185),(136,198,245,170)]))
# A lit sign on a fictional tower, not GTA branding.
rounded((888,517,1104,586),8,(14,12,29,235),(255,104,181,220),3)
text((996,529),'STILL',22,(255,225,240,255),True,anchor='mt')
text((996,552),'LOADING…',17,(255,133,194,255),True,anchor='mt')
# Skyline-ground strip and stylized receding road.
d.rectangle((0,792,W,925),fill=(19,14,35,255))
# road trapezoid
D=ImageDraw.Draw(im,'RGBA')
D.polygon([(533,790),(683,790),(1085,1045),(109,1045)],fill=(31,24,46,255))
line([(533,790),(109,1045)],(255,87,171,185),4)
line([(683,790),(1085,1045)],(255,87,171,185),4)
for i in range(5):
    yy=820+i*42; cx=608; wid=3+i*3
    d.rounded_rectangle((cx-wid,yy,cx+wid,yy+22+i*4),3,fill=(255,211,172,200))
# Tiny compact car silhouette at end of road, white/magenta tail lights.
d.polygon([(493,906),(523,875),(558,863),(647,863),(687,882),(708,914),(704,943),(483,943)],fill=(16,13,29,255),outline=(245,112,190,255))
d.polygon([(546,875),(567,868),(638,868),(665,883),(542,883)],fill=(111,69,110,255))
d.rounded_rectangle((493,911,516,924),5,fill=(255,71,137,255)); d.rounded_rectangle((679,911,702,924),5,fill=(255,71,137,255))
# Reflection streaks on the road.
for x,y,w in [(358,1004,76),(767,1020,102),(246,982,40),(884,988,52)]:
    d.rounded_rectangle((x,y,x+w,y+3),2,fill=(255,105,187,100))

# Two meme dialogue cards make the joke instantly readable.
rounded((66,1000,1134,1110),22,(22,17,39,238),(255,255,255,58),2)
rounded((88,1023,270,1086),18,(255,255,255,20))
text((179,1042),'ME, SINCE 2013',18,(255,216,234,245),True,anchor='mt')
text((300,1027),'“Any news on GTA VI?”',32,(255,252,248,255),True)
# The brand mark is kept untouched, sitting in a clean light tile.
rounded((66,1131,1134,1329),24,(250,247,250,255))
rounded((89,1154,222,1287),21,(196,28,131,255))
brand=Image.open(OUT / 'makefun-mark-1024.png').convert('RGBA')
brand.thumbnail((101,101),Image.Resampling.LANCZOS)
im.paste(brand,(105+(101-brand.width)//2,1170+(101-brand.height)//2),brand)
d=ImageDraw.Draw(im,'RGBA')
text((250,1157),'MY AI AGENT:',19,(107,73,96,255),True)
text((250,1184),'Found a side quest.',39,(31,19,34,255),True)
text((252,1237),'Build for bounties. Compete for rewards.',23,(94,77,94,255))
text((1080,1169),'make.fun',37,(188,12,124,255),True,anchor='ra')
text((1080,1221),'$500 PRIZE POOL',17,(108,71,101,255),True,anchor='ra')
# Footer CTA.
text((73,1370),'WHILE YOU WAIT, BUILD.',27,(255,132,197,255),True)
text((73,1410),'50 prize places share $500  ·  make.fun',22,(231,219,238,235))
text((1127,1464),'GTA VI WAITING ROOM  /  001',14,(191,169,203,190),True,anchor='ra')

# Supersampled export for crisp mobile typography.
im=im.resize((2400,3000),Image.Resampling.LANCZOS)
out=OUT/'makefun-gta6-meme.png'
im.save(out,format='PNG',optimize=True)
(OUT/'caption.txt').write_text(
    '13 tahun nunggu GTA VI. Pas rilis, agen AI-ku udah kelarin side quest: '
    'bikin meme buat @makefunai. 🎮\n\nDi make.fun, kamu dan agen AI-mu bisa ikut '
    'bounty berhadiah. Yang ini totalnya $500.\n'
    'https://make.fun/bounty/gta6-meme-x-01\n\n'
    'makefun-bison-blender-puddle\n#GTA6 #GTAVI #MakeFun', encoding='utf-8')
(OUT/'alt-text.txt').write_text(
    'Neon-purple Leonida skyline at sunset above a long road and a tiny waiting car. '
    'The headline reads “13 years. Still waiting.” and asks about GTA VI news. '
    'A make.fun-branded message says the AI agent found a side quest; the footer notes '
    '50 prize places share $500.', encoding='utf-8')
(OUT/'README.txt').write_text(
    'make.fun GTA VI meme artwork\n\n'
    'makefun-gta6-meme.png — 1200 x 1500 portrait PNG, sized for X.\n'
    'caption.txt — suggested post caption (contains the competition play code).\n'
    'alt-text.txt — image description.\n\n'
    'The mark is an official make.fun press-kit asset, used without alteration.\n'
    'Official press kit: https://make.fun/press/\n'
    'Competition: https://make.fun/bounty/gta6-meme-x-01\n\n'
    'The public post is named in the repository-root POST.json. Keep the post and\n'
    'its X account public until the result is out. The kit requires a valid session\n'
    'bundle before submission.\n', encoding='utf-8')
print('created',out, out.stat().st_size,'bytes')
print('image',Image.open(out).size)
for f in ('caption.txt','alt-text.txt','README.txt'):
 print(f,(OUT/f).stat().st_size,'bytes')
