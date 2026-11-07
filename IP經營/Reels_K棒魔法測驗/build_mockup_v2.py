"""K 棒魔法測驗 Reels mockup v2：更生動的魔法風格（光暈、手勢、星星眼、魔法陣、光芒）。"""
import os, math, random

G, R, GOLD, INK, NAVY = "#3fbf86", "#ef6552", "#f2c46d", "#f6eedf", "#1d1a33"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "mockup_preview")

QS = [
    ((70,55,50,75), (45,25,18,50), "多"), ((30,45,25,50), (55,75,50,82), "空"),
    ((25,50,20,55), (72,64,28,75), "多"), ((60,35,30,65), (22,30,20,72), "空"),
    ((25,50,20,55), (61,59,58,90), "多"), ((65,40,35,70), (48,55,10,57), "空"),
    ((45,58,42,62), (66,20,15,69), "多"), ((50,38,34,53), (32,80,28,84), "空"),
]

DEFS = f'''<defs>
<radialGradient id="bg" cx="50%" cy="30%" r="85%"><stop offset="0" stop-color="#3a2f78"/><stop offset=".55" stop-color="#1b1640"/><stop offset="1" stop-color="#0a0818"/></radialGradient>
<radialGradient id="neb1" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#8a5cff" stop-opacity=".45"/><stop offset="1" stop-color="#8a5cff" stop-opacity="0"/></radialGradient>
<radialGradient id="neb2" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#2fd0ff" stop-opacity=".25"/><stop offset="1" stop-color="#2fd0ff" stop-opacity="0"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff6d8" stop-opacity=".9"/><stop offset=".4" stop-color="{GOLD}" stop-opacity=".35"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<linearGradient id="page" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2e2760"/><stop offset="1" stop-color="#1c1840"/></linearGradient>
<linearGradient id="hat" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6a55d8"/><stop offset="1" stop-color="#3a2f8a"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="16"/></filter>
<filter id="blur2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
</defs>'''

def star(cx, cy, r, col, op=1, inner=.45, stroke=None):
    pts = " ".join(f"{cx+(r if i%2==0 else r*inner)*math.cos(-math.pi/2+i*math.pi/5):.1f},{cy+(r if i%2==0 else r*inner)*math.sin(-math.pi/2+i*math.pi/5):.1f}" for i in range(10))
    st = f' stroke="{stroke}" stroke-width="{r*0.18:.1f}" stroke-linejoin="round"' if stroke else ""
    return f'<polygon points="{pts}" fill="{col}" opacity="{op}"{st}/>'

def sparkle(cx, cy, r, col="#fff8e1", op=1):
    return f'<path d="M{cx},{cy-r} Q{cx+r*.15},{cy-r*.15} {cx+r},{cy} Q{cx+r*.15},{cy+r*.15} {cx},{cy+r} Q{cx-r*.15},{cy+r*.15} {cx-r},{cy} Q{cx-r*.15},{cy-r*.15} {cx},{cy-r}Z" fill="{col}" opacity="{op}"/>'

def sky(tint=None, seed=3):
    random.seed(seed)
    s = DEFS + '<rect width="1080" height="1920" fill="url(#bg)"/>'
    s += '<ellipse cx="180" cy="520" rx="420" ry="300" fill="url(#neb1)"/><ellipse cx="930" cy="1350" rx="460" ry="330" fill="url(#neb2)"/><ellipse cx="820" cy="300" rx="300" ry="220" fill="url(#neb1)"/>'
    if tint:
        s += f'<rect width="1080" height="1920" fill="{tint}" opacity=".22"/><ellipse cx="540" cy="1200" rx="620" ry="520" fill="{tint}" opacity=".18" filter="url(#blur)"/>'
    # 月亮
    s += f'<circle cx="935" cy="250" r="62" fill="#fff3c9" opacity=".95"/><circle cx="960" cy="232" r="56" fill="#22194d"/><circle cx="935" cy="250" r="110" fill="url(#glow)" opacity=".35"/>'
    for _ in range(110):
        x, y, r = random.randint(0,1080), random.randint(0,1920), random.choice([1.2,1.6,2,2.6,3.2])
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{random.choice([GOLD,"#fff","#fff","#bfe8ff"])}" opacity="{random.uniform(.3,.95):.2f}"/>'
    for _ in range(12):
        s += sparkle(random.randint(40,1040), random.randint(180,1780), random.randint(7,18), random.choice(["#fff8e1", GOLD]), random.uniform(.5,1))
    # 星座線
    pts = [(70,330),(150,280),(230,320),(270,250)]
    s += "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#cfc6ff" stroke-opacity=".35" stroke-width="2"/>' for a, b in zip(pts, pts[1:]))
    s += "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff"/>' for x, y in pts)
    return s

def eyes(cx, cy, s, mood):
    dx = 15*s
    if mood == "stars":
        return "".join(star(cx+k*dx, cy, 11*s, GOLD, 1, .5, NAVY) for k in (-1, 1))
    if mood == "happy":
        return "".join(f'<path d="M{cx+k*dx-8*s},{cy+2*s} q{8*s},{-12*s} {16*s},0" stroke="{NAVY}" stroke-width="{4*s}" fill="none" stroke-linecap="round"/>' for k in (-1, 1))
    if mood == "smug":
        return "".join(f'<path d="M{cx+k*dx-8*s},{cy} q{8*s},{5*s} {16*s},0" stroke="{NAVY}" stroke-width="{4*s}" fill="none" stroke-linecap="round"/>' for k in (-1, 1)) + \
               "".join(f'<path d="M{cx+k*dx-9*s},{cy-9*s} l{18*s},{(-4 if k<0 else 4)*s}" stroke="{NAVY}" stroke-width="{3.4*s}" stroke-linecap="round"/>' for k in (-1, 1))
    if mood == "scared":
        return "".join(f'<circle cx="{cx+k*dx}" cy="{cy}" r="{10*s}" fill="#fff"/><circle cx="{cx+k*dx}" cy="{cy+2*s}" r="{3.6*s}" fill="{NAVY}"/>' for k in (-1, 1))
    if mood == "dizzy":
        return "".join(f'<path d="M{cx+k*dx},{cy} m{-7*s},0 a{7*s},{7*s} 0 1,1 {14*s},0 a{5*s},{5*s} 0 1,1 {-10*s},0 a{3*s},{3*s} 0 1,1 {6*s},0" stroke="{NAVY}" stroke-width="{2.6*s}" fill="none"/>' for k in (-1, 1))
    # surprised：大眼睛加反光
    return "".join(f'<ellipse cx="{cx+k*dx}" cy="{cy}" rx="{8.5*s}" ry="{10*s}" fill="{NAVY}"/><circle cx="{cx+k*dx+3*s}" cy="{cy-4*s}" r="{3.4*s}" fill="#fff"/><circle cx="{cx+k*dx-3*s}" cy="{cy+4*s}" r="{1.6*s}" fill="#fff"/>' for k in (-1, 1))

def mouth(cx, cy, s, mood):
    if mood in ("stars", "happy"):
        return f'<path d="M{cx-11*s},{cy} q{11*s},{16*s} {22*s},0 z" fill="{NAVY}"/><path d="M{cx-5*s},{cy+6*s} q{5*s},{4*s} {10*s},0" fill="#ff7b8e"/>'
    if mood == "smug":
        return f'<path d="M{cx-9*s},{cy+2*s} q{12*s},{8*s} {19*s},{-5*s}" stroke="{NAVY}" stroke-width="{3.6*s}" fill="none" stroke-linecap="round"/>'
    if mood == "scared":
        return f'<path d="M{cx-10*s},{cy+6*s} l{5*s},{-5*s} l{5*s},{5*s} l{5*s},{-5*s} l{5*s},{5*s}" stroke="{NAVY}" stroke-width="{3*s}" fill="none" stroke-linejoin="round"/>'
    if mood == "dizzy":
        return f'<path d="M{cx-9*s},{cy+4*s} q{4.5*s},{-7*s} {9*s},0 t{9*s},0" stroke="{NAVY}" stroke-width="{3.2*s}" fill="none" stroke-linecap="round"/>'
    return f'<ellipse cx="{cx}" cy="{cy+4*s}" rx="{5*s}" ry="{6.5*s}" fill="{NAVY}"/>'

def extras(cx, cy, s, mood):
    out = "".join(f'<ellipse cx="{cx+k*26*s}" cy="{cy+12*s}" rx="{6.5*s}" ry="{4*s}" fill="#ff9aa8" opacity=".7"/>' for k in (-1, 1))
    if mood == "scared":
        out += f'<path d="M{cx+30*s},{cy-22*s} q{7*s},{12*s} 0,{17*s} q{-7*s},{-5*s} 0,{-17*s}" fill="#9fdcff"/>'
    if mood == "dizzy":
        out += "".join(star(cx+dx*s, cy-34*s+dy*s, 6*s, GOLD) for dx, dy in ((-22,0),(0,-8),(22,0)))
    if mood == "stars":
        out += sparkle(cx-34*s, cy-26*s, 7*s, GOLD) + sparkle(cx+36*s, cy-20*s, 6*s, "#fff")
    return out

def arms(x, w, y, col, pose, s):
    l, r = x, x + w
    sw = 9*s
    P = {
        "up":     (f"M{l},{y} q{-30*s},{-20*s} {-34*s},{-58*s}", f"M{r},{y} q{30*s},{-20*s} {34*s},{-58*s}"),
        "cheeks": (f"M{l},{y} q{-26*s},{4*s} {-12*s},{-34*s}",  f"M{r},{y} q{26*s},{4*s} {12*s},{-34*s}"),
        "hip":    (f"M{l},{y} q{-30*s},{6*s} {-12*s},{30*s}",   f"M{r},{y} q{30*s},{-20*s} {34*s},{-58*s}"),
        "side":   (f"M{l},{y} q{-24*s},{12*s} {-30*s},{38*s}",  f"M{r},{y} q{24*s},{12*s} {30*s},{38*s}"),
    }[pose]
    return "".join(f'<path d="{d}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" fill="none"/>' for d in P)

def kbar(x, top, bottom, k, w, mood="surprised", pose="side", faces=True, glow=True, corner=.34):
    o, c, h, l = k
    col = G if c < o else R
    Y = lambda v: top + (bottom - top) * v / 100
    bt, bb = Y(min(o, c)), Y(max(o, c))
    bh = max(bb - bt, 10)
    cx = x + w/2
    s = ""
    if glow:
        s += f'<rect x="{x-10}" y="{bt-10}" width="{w+20}" height="{bh+20}" rx="{w*max(corner,.12)}" fill="{col}" opacity=".55" filter="url(#blur)"/>'
    s += f'<line x1="{cx}" y1="{Y(h)}" x2="{cx}" y2="{Y(l)}" stroke="{col}" stroke-width="{max(w*.09,3)}" stroke-linecap="round"/>'
    if faces and bh >= w*.7:
        s += arms(x+2, w-4, bt + min(bh*.62, w*1.0), col, pose, w/100)
    s += f'<rect x="{x}" y="{bt}" width="{w}" height="{bh}" rx="{min(w*corner, bh/2)}" fill="{col}"/>'
    s += f'<rect x="{x+w*.13}" y="{bt+6}" width="{w*.12}" height="{max(bh-12,0)}" rx="{w*.06}" fill="#fff" opacity=".28"/>'
    if faces and bh >= w*.7:
        fs = w/80; fy = bt + min(bh*.36, w*.6)
        s += eyes(cx, fy, fs, mood) + mouth(cx, fy+16*fs, fs, mood) + extras(cx, fy, fs, mood)
    return s

def hero(cx, by, col, mood, wand=False, tilt=-6, hat_tilt=-12, scale=1.0, pose="wand", corner=52):
    w, h = 160*scale, 240*scale
    x, y = cx - w/2, by - h
    sc = scale
    s = f'<ellipse cx="{cx}" cy="{by+78*sc}" rx="{110*sc}" ry="{20*sc}" fill="#000" opacity=".35"/>'
    s += f'<ellipse cx="{cx}" cy="{by+78*sc}" rx="{180*sc}" ry="{36*sc}" fill="none" stroke="{GOLD}" stroke-opacity=".5" stroke-width="{3*sc}" stroke-dasharray="{10*sc} {12*sc}"/>'
    s += f'<g transform="rotate({tilt} {cx} {by})">'
    s += f'<rect x="{x-14*sc}" y="{y-14*sc}" width="{w+28*sc}" height="{h+28*sc}" rx="{(corner+8)*sc}" fill="{col}" opacity=".5" filter="url(#blur)"/>'
    s += f'<line x1="{cx}" y1="{y-20*sc}" x2="{cx}" y2="{by+60*sc}" stroke="{col}" stroke-width="{13*sc}" stroke-linecap="round"/>'
    # 腳
    s += "".join(f'<ellipse cx="{cx+k*40*sc}" cy="{by+16*sc}" rx="{26*sc}" ry="{14*sc}" fill="#3a2f8a"/>' for k in (-1, 1))
    # 披風
    s += f'<path d="M{x+6*sc},{y+70*sc} Q{cx},{y+110*sc} {x+w-6*sc},{y+70*sc} L{x+w+30*sc},{by+10*sc} Q{cx},{by+40*sc} {x-30*sc},{by+10*sc}Z" fill="#4b3aa8" opacity=".95"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{corner*sc}" fill="{col}"/>'
    s += f'<rect x="{x+22*sc}" y="{y+20*sc}" width="{17*sc}" height="{h-40*sc}" rx="{8*sc}" fill="#fff" opacity=".25"/>'
    s += f'<circle cx="{cx}" cy="{y+156*sc}" r="{13*sc}" fill="{GOLD}"/>' + star(cx, y+156*sc, 9*sc, "#fff7d6")
    s += f'<g transform="rotate({hat_tilt} {cx} {y+8*sc})">'
    s += f'<ellipse cx="{cx}" cy="{y+10*sc}" rx="{105*sc}" ry="{24*sc}" fill="#2c2370"/>'
    s += f'<path d="M{cx-66*sc},{y+6*sc} C{cx-30*sc},{y-90*sc} {cx+10*sc},{y-150*sc} {cx+70*sc},{y-210*sc} C{cx+40*sc},{y-140*sc} {cx+60*sc},{y-60*sc} {cx+66*sc},{y+6*sc}Z" fill="url(#hat)"/>'
    s += f'<path d="M{cx-64*sc},{y-14*sc} Q{cx},{y-34*sc} {cx+64*sc},{y-14*sc}" stroke="{GOLD}" stroke-width="{12*sc}" fill="none"/>'
    s += star(cx-18*sc, y-70*sc, 10*sc, GOLD) + star(cx+22*sc, y-120*sc, 8*sc, "#fff3c9") + sparkle(cx-4*sc, y-160*sc, 7*sc, "#fff")
    s += star(cx+72*sc, y-214*sc, 22*sc, GOLD, 1, .45, "#fff3c9") + f'</g>'
    fs = 2.3*sc; fy = y + 92*sc
    s += eyes(cx, fy, fs, mood) + mouth(cx, fy+18*fs, fs, mood) + extras(cx, fy, fs, mood)
    # 手和魔杖
    s += f'<path d="M{x+4*sc},{y+140*sc} q{-46*sc},{6*sc} {-60*sc},{44*sc}" stroke="{col}" stroke-width="{18*sc}" stroke-linecap="round" fill="none"/>'
    if wand:
        s += f'<path d="M{x+w-4*sc},{y+140*sc} q{46*sc},{-10*sc} {64*sc},{-56*sc}" stroke="{col}" stroke-width="{18*sc}" stroke-linecap="round" fill="none"/>'
        s += f'<line x1="{x+w+56*sc}" y1="{y+100*sc}" x2="{x+w+130*sc}" y2="{y-40*sc}" stroke="#8a6234" stroke-width="{11*sc}" stroke-linecap="round"/>'
        s += f'<circle cx="{x+w+136*sc}" cy="{y-52*sc}" r="{70*sc}" fill="url(#glow)"/>' + star(x+w+136*sc, y-52*sc, 34*sc, GOLD, 1, .45, "#fff3c9")
        # 魔法軌跡
        s += f'<path d="M{x+w+136*sc},{y-52*sc} C{x+w+230*sc},{y-120*sc} {x+w+120*sc},{y-230*sc} {x+w+220*sc},{y-300*sc}" stroke="{GOLD}" stroke-width="{4*sc}" fill="none" stroke-dasharray="{3*sc} {12*sc}" stroke-linecap="round"/>'
        s += "".join(sparkle(x+w+136*sc+dx*sc, y-52*sc+dy*sc, r*sc, c) for dx, dy, r, c in ((80,-70,14,"#fff"),(-30,-110,11,GOLD),(95,-190,16,GOLD),(40,-250,9,"#fff"),(-60,-30,8,"#fff")))
    else:
        s += f'<path d="M{x+w-4*sc},{y+140*sc} q{46*sc},{6*sc} {60*sc},{44*sc}" stroke="{col}" stroke-width="{18*sc}" stroke-linecap="round" fill="none"/>'
    return s + '</g>'

def chrome():
    return (f'<text x="540" y="128" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="46" fill="{GOLD}" letter-spacing="4">Hanna｜K棒魔法師</text>'
            + sparkle(250, 112, 12, GOLD) + sparkle(830, 112, 12, GOLD) +
            f'<path d="M360,162 h360" stroke="{GOLD}" stroke-opacity=".45" stroke-width="2"/>'
            f'<text x="540" y="1840" text-anchor="middle" font-family="Noto Sans TC" font-size="34" fill="{INK}" opacity=".75" letter-spacing="2">@_hannapang</text>')

def progress(n):
    s = f'<rect x="452" y="222" width="176" height="64" rx="32" fill="{GOLD}"/><text x="540" y="266" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="34" fill="{NAVY}">{n:02d} / 08</text>'
    for i in range(8):
        on = i < n
        if on and i == n-1:
            s += f'<circle cx="{372+i*48}" cy="330" r="26" fill="url(#glow)"/>'
        s += star(372+i*48, 330, 16 if on else 13, GOLD if on else "#5c5490")
    return s

def book():
    random.seed(9)
    s = f'<ellipse cx="540" cy="760" rx="520" ry="380" fill="#8a5cff" opacity=".22" filter="url(#blur)"/>'
    s += f'<path d="M100,430 Q320,380 540,440 Q760,380 980,430 L980,1080 Q760,1030 540,1092 Q320,1030 100,1080Z" fill="#14112b" stroke="{GOLD}" stroke-width="6"/>'
    s += '<path d="M128,452 Q320,410 524,462 L524,1062 Q320,1012 128,1052Z" fill="url(#page)"/><path d="M556,462 Q760,410 952,452 L952,1052 Q760,1012 556,1062Z" fill="url(#page)"/>'
    s += f'<path d="M540,440 L540,1092" stroke="{GOLD}" stroke-opacity=".7" stroke-width="4"/>'
    # 書頁上的符文圈
    for cx, cy in ((326, 760), (754, 760)):
        s += f'<circle cx="{cx}" cy="{cy}" r="170" fill="none" stroke="{GOLD}" stroke-opacity=".14" stroke-width="3"/><circle cx="{cx}" cy="{cy}" r="140" fill="none" stroke="{GOLD}" stroke-opacity=".1" stroke-width="2" stroke-dasharray="6 10"/>'
    # 角落裝飾
    s += "".join(star(x, y, 12, GOLD, .9) for x, y in ((118,440),(962,440),(118,1070),(962,1070)))
    # 從書裡飄出的光點
    s += "".join(sparkle(random.randint(160, 920), random.randint(370, 440), random.randint(5, 12), random.choice(["#fff", GOLD]), .9) for _ in range(9))
    return s

def question(i, answered):
    k1, k2, ans = QS[i]
    col = G if ans == "多" else R
    rays = "".join(f'<path d="M540,1260 L{540+math.cos(a-.06)*620},{1260+math.sin(a-.06)*620} L{540+math.cos(a+.06)*620},{1260+math.sin(a+.06)*620}Z" fill="{col}" opacity=".16"/>' for a in [j*math.pi/9 for j in range(18)]) if answered else ""
    s = sky(col if answered else None) + rays + chrome() + progress(i+1) + book()
    lo, hi = min(k1[2], k2[2]), max(k1[3], k2[3])
    norm = lambda k: tuple((v - lo) / (hi - lo) * 100 for v in k)
    if not answered:
        m1, p1, m2, p2 = "surprised", "side", "surprised", "up"
    elif ans == "多":
        m1, p1 = ("happy", "up") if k1[1] < k1[0] else ("scared", "cheeks")
        m2, p2 = ("stars", "up") if k2[1] < k2[0] else ("happy", "up")
    else:
        m1, p1 = ("scared", "cheeks") if k1[1] < k1[0] else ("dizzy", "side")
        m2, p2 = ("smug", "hip") if k2[1] > k2[0] else ("smug", "hip")
    s += kbar(250, 530, 990, norm(k1), 130, m1, p1) + kbar(700, 530, 990, norm(k2), 130, m2, p2)
    if not answered:
        # 第 2 根「咻」出現的動態線
        s += "".join(f'<line x1="{765+math.cos(a)*120}" y1="{560+math.sin(a)*120}" x2="{765+math.cos(a)*160}" y2="{560+math.sin(a)*160}" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"/>' for a in [math.radians(d) for d in (-160,-125,-90,-55,-20)])
        s += f'<text x="900" y="520" font-family="Noto Serif TC" font-weight="900" font-size="54" fill="{GOLD}" transform="rotate(12 900 520)">咻！</text>'
        s += f'<text x="540" y="1290" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="150" fill="{INK}" opacity=".9">？</text>'
    else:
        label = "▲ 做多" if ans == "多" else "▼ 做空"
        cy = 1260
        # 光芒
        # 魔法陣
        s += f'<ellipse cx="540" cy="{cy+20}" rx="340" ry="92" fill="none" stroke="{col}" stroke-width="6"/>'
        s += f'<ellipse cx="540" cy="{cy+20}" rx="292" ry="74" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 12"/>'
        s += f'<ellipse cx="540" cy="{cy+20}" rx="240" ry="58" fill="{col}" opacity=".18"/>'
        s += "".join(star(540+math.cos(a)*316, cy+20+math.sin(a)*83, 10, GOLD) for a in [i*math.pi/4 for i in range(8)])
        s += f'<circle cx="540" cy="{cy-40}" r="260" fill="url(#glow)" opacity=".45"/>'
        s += f'<text x="540" y="{cy+10}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="140" fill="{col}" stroke="#fff8e8" stroke-width="5" paint-order="stroke">{label}</text>'
        random.seed(i+20)
        s += "".join(star(random.randint(90, 990), random.randint(1110, 1420), random.randint(8, 16), random.choice([GOLD, col, "#fff"]), .95) for _ in range(14))
    s += (f'<text x="540" y="1530" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{INK}">'
          f'<tspan fill="{G}">做多</tspan>還是<tspan fill="{R}">做空</tspan>？</text>')
    return s

def hook():
    s = sky() + chrome()
    s += f'<circle cx="540" cy="335" r="110" fill="url(#glow)" opacity=".7"/><rect x="410" y="285" width="260" height="96" rx="48" fill="{GOLD}"/><text x="540" y="353" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="{NAVY}">8 題</text>'
    s += sparkle(380, 300, 16) + sparkle(710, 290, 12, GOLD) + sparkle(700, 390, 10)
    s += hero(360, 1040, G, "happy", wand=True, tilt=-8) + hero(760, 1060, R, "scared", tilt=8, hat_tilt=16, scale=.9)
    s += f'<text x="660" y="720" font-family="Noto Serif TC" font-weight="900" font-size="48" fill="{INK}" transform="rotate(10 660 720)">嚇！</text>'
    s += (f'<text x="540" y="1380" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="104" fill="{GOLD}" stroke="#2a1f55" stroke-width="6" paint-order="stroke">K 棒魔法測驗</text>'
          f'<text x="540" y="1500" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="62" fill="{INK}">1 秒判斷，8 題你能<tspan fill="{GOLD}">全對</tspan>嗎？</text>')
    s += "".join(sparkle(x, y, r, GOLD) for x, y, r in ((130,1340,14),(950,1330,18),(170,1480,9),(930,1470,11)))
    return s

def cards():
    s = sky(seed=5) + chrome()
    s += (f'<text x="540" y="300" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="86" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">K 棒咒語卡</text>'
          f'<text x="540" y="380" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="46" fill="{INK}">8 種一次帶走</text>')
    s += sparkle(300, 270, 14, GOLD) + sparkle(790, 260, 18) + sparkle(820, 330, 9, GOLD)
    for i, (k1, k2, ans) in enumerate(QS):
        cx, cy = 86 + (i % 4) * 232, 450 + (i // 4) * 420
        col = G if ans == "多" else R
        s += f'<rect x="{cx-6}" y="{cy-6}" width="220" height="392" rx="26" fill="{col}" opacity=".35" filter="url(#blur2)"/>'
        s += f'<rect x="{cx}" y="{cy}" width="208" height="380" rx="22" fill="#1a1640" stroke="{GOLD}" stroke-width="3"/>'
        s += f'<rect x="{cx+10}" y="{cy+10}" width="188" height="360" rx="16" fill="none" stroke="{GOLD}" stroke-opacity=".3" stroke-width="2" stroke-dasharray="6 8"/>'
        s += star(cx+30, cy+32, 11, GOLD) + f'<text x="{cx+182}" y="{cy+44}" text-anchor="end" font-family="Noto Sans TC" font-weight="700" font-size="26" fill="{GOLD}">{i+1:02d}</text>'
        lo, hi = min(k1[2], k2[2]), max(k1[3], k2[3])
        norm = lambda k: tuple((v - lo) / (hi - lo) * 100 for v in k)
        s += kbar(cx+40, cy+70, cy+290, norm(k1), 54, faces=False, glow=False) + kbar(cx+114, cy+70, cy+290, norm(k2), 54, faces=False, glow=False)
        s += f'<text x="{cx+104}" y="{cy+350}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{col}">{"▲ 做多" if ans == "多" else "▼ 做空"}</text>'
    s += (f'<text x="540" y="1420" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="72" fill="{INK}">📌 先收藏！</text>'
          f'<text x="540" y="1515" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="60" fill="{GOLD}">看盤前打開對一遍</text>')
    # 收藏書籤：光圈、脈衝圈、魔杖和提示字
    s += f'<circle cx="930" cy="1690" r="130" fill="url(#glow)"/>'
    s += "".join(f'<circle cx="930" cy="1690" r="{r}" fill="none" stroke="{GOLD}" stroke-opacity="{op}" stroke-width="4"/>' for r, op in ((86,.7),(112,.4),(138,.2)))
    s += f'<path d="M898,1636 h64 v108 l-32,-26 l-32,26Z" fill="{GOLD}" stroke="#fff3c9" stroke-width="4"/>'
    s += f'<line x1="640" y1="1600" x2="820" y2="1668" stroke="#8a6234" stroke-width="11" stroke-linecap="round"/>' + star(832, 1673, 26, GOLD, 1, .45, "#fff3c9")
    s += f'<text x="560" y="1700" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{GOLD}">點這裡收藏 →</text>'
    s += "".join(sparkle(x, y, r) for x, y, r in ((800,1610,12),(1010,1600,14),(1020,1780,10),(850,1780,9)))
    return s

def ending():
    s = sky(seed=7) + chrome()
    s += hero(470, 1010, G, "stars", wand=True, tilt=-6, scale=1.1)
    s += (f'<text x="540" y="1310" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">錯了幾題？留言告訴我</text>'
          f'<text x="540" y="1430" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="48" fill="{INK}">看不懂也沒關係</text>'
          f'<text x="540" y="1505" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{INK}"><tspan fill="{GOLD}">3+1 指標</tspan>直接告訴你做多還是做空</text>'
          f'<rect x="220" y="1580" width="640" height="110" rx="55" fill="{GOLD}"/>'
          f'<rect x="220" y="1580" width="640" height="110" rx="55" fill="none" stroke="#fff3c9" stroke-width="4"/>'
          f'<text x="540" y="1652" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{NAVY}">方法放在主頁 Portaly 👆</text>')
    s += "".join(sparkle(x, y, r, c) for x, y, r, c in ((190,1590,16,GOLD),(890,1580,14,"#fff"),(900,1700,10,GOLD)))
    return s

if __name__ == "__main__":
    frames = [("v2_01", hook()), ("v2_02", question(0, False)), ("v2_03", question(0, True)), ("v2_04", question(7, True)), ("v2_05", cards()), ("v2_06", ending())]
    html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&display=block" rel="stylesheet">'
            '<style>body{margin:0;background:#000}svg{display:block;margin-bottom:10px}</style></head><body>'
            + "".join(f'<svg id="{n}" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">{f}</svg>' for n, f in frames)
            + '<script>document.fonts.ready.then(()=>{document.body.dataset.ready="1"})</script></body></html>')
    open(os.path.join(OUT, "mockup.html"), "w", encoding="utf-8").write(html)
