"""K 棒魔法測驗 Reels 的靜態 mockup（1080×1920）。"""
import os, random

G, R, GOLD, INK = "#3fbf86", "#e8604f", "#e9b95a", "#f4ecdc"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mockup")

# 8 題：(第 1 根, 第 2 根, 答案)，K 棒 = (開, 收, 高, 低)，0 在上、100 在下
QS = [
    ((70,55,50,75), (45,25,18,50), "多"),
    ((30,45,25,50), (55,75,50,82), "空"),
    ((25,50,20,55), (72,64,28,75), "多"),
    ((60,35,30,65), (22,30,20,72), "空"),
    ((25,50,20,55), (61,59,58,90), "多"),
    ((65,40,35,70), (48,55,10,57), "空"),
    ((45,58,42,62), (66,20,15,69), "多"),
    ((50,38,34,53), (32,80,28,84), "空"),
]

def face(cx, cy, s, mood):
    """畫表情：s 是比例。"""
    e = 7*s; dx = 13*s
    if mood == "happy":
        eyes = "".join(f'<path d="M{cx+k*dx-e},{cy} q{e},{-e*1.3} {2*e},0" stroke="#1d1a33" stroke-width="{3.2*s}" fill="none" stroke-linecap="round"/>' for k in (-1, 1))
        mouth = f'<path d="M{cx-7*s},{cy+10*s} q{7*s},{9*s} {14*s},0" stroke="#1d1a33" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>'
    elif mood == "scared":
        eyes = "".join(f'<circle cx="{cx+k*dx}" cy="{cy}" r="{e}" fill="#fff"/><circle cx="{cx+k*dx}" cy="{cy+1.5*s}" r="{e*0.55}" fill="#1d1a33"/>' for k in (-1, 1))
        mouth = f'<ellipse cx="{cx}" cy="{cy+13*s}" rx="{4*s}" ry="{5*s}" fill="#1d1a33"/><path d="M{cx+24*s},{cy-14*s} q{5*s},{9*s} 0,{13*s} q{-5*s},{-4*s} 0,{-13*s}" fill="#9fd8ff"/>'
    elif mood == "dizzy":
        eyes = "".join(f'<path d="M{cx+k*dx-e},{cy-e} l{2*e},{2*e} m0,{-2*e} l{-2*e},{2*e}" stroke="#1d1a33" stroke-width="{3*s}" stroke-linecap="round"/>' for k in (-1, 1))
        mouth = f'<path d="M{cx-8*s},{cy+13*s} q{4*s},{-5*s} {8*s},0 t{8*s},0" stroke="#1d1a33" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>'
    elif mood == "smug":
        eyes = "".join(f'<path d="M{cx+k*dx-e},{cy+1*s} h{2*e}" stroke="#1d1a33" stroke-width="{3.5*s}" stroke-linecap="round"/>' for k in (-1, 1))
        mouth = f'<path d="M{cx-6*s},{cy+11*s} q{8*s},{6*s} {13*s},{-3*s}" stroke="#1d1a33" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>'
    else:  # surprised
        eyes = "".join(f'<circle cx="{cx+k*dx}" cy="{cy}" r="{e*0.95}" fill="#1d1a33"/><circle cx="{cx+k*dx+2*s}" cy="{cy-2.5*s}" r="{e*0.35}" fill="#fff"/>' for k in (-1, 1))
        mouth = f'<circle cx="{cx}" cy="{cy+12*s}" r="{3.5*s}" fill="#1d1a33"/>'
    blush = "".join(f'<ellipse cx="{cx+k*21*s}" cy="{cy+8*s}" rx="{5*s}" ry="{3*s}" fill="#ff9aa8" opacity=".55"/>' for k in (-1, 1))
    return eyes + mouth + blush

def kbar(x, top, bottom, k, w, mood="surprised", faces=True):
    """在 x（左緣）、價格區間 top～bottom 的畫布上畫一根有表情的 K 棒。"""
    o, c, h, l = k
    col = G if c < o else R
    Y = lambda v: top + (bottom - top) * v / 100
    bt, bb = Y(min(o, c)), Y(max(o, c))
    bh = max(bb - bt, 8)
    cx = x + w / 2
    s = f'<line x1="{cx}" y1="{Y(h)}" x2="{cx}" y2="{Y(l)}" stroke="{col}" stroke-width="{max(w*0.09,3)}" stroke-linecap="round"/>'
    s += f'<rect x="{x}" y="{bt}" width="{w}" height="{bh}" rx="{min(w*0.32, bh/2)}" fill="{col}"/>'
    s += f'<rect x="{x+w*0.14}" y="{bt+4}" width="{w*0.12}" height="{max(bh-8,0)}" rx="{w*0.06}" fill="#fff" opacity=".22"/>'
    if faces and bh >= w * 0.75:
        s += face(cx, bt + min(bh*0.38, w*0.62), w/80, mood)
    return s

def hero(cx, by, col, mood, wand=False, hat_tilt=-12, scale=1.0):
    """大尺寸 K 棒小法師（開場、結尾用）：尖帽、星星、小手、魔杖。"""
    w, h = 150*scale, 230*scale
    x, y = cx - w/2, by - h
    s = f'<line x1="{cx}" y1="{y-30*scale}" x2="{cx}" y2="{by+60*scale}" stroke="{col}" stroke-width="{12*scale}" stroke-linecap="round"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{48*scale}" fill="{col}"/>'
    s += f'<rect x="{x+20*scale}" y="{y+18*scale}" width="{16*scale}" height="{h-36*scale}" rx="{8*scale}" fill="#fff" opacity=".22"/>'
    # 尖帽
    s += (f'<g transform="rotate({hat_tilt} {cx} {y+8*scale})">'
          f'<path d="M{cx-95*scale},{y+12*scale} Q{cx},{y-8*scale} {cx+95*scale},{y+12*scale} Q{cx},{y+30*scale} {cx-95*scale},{y+12*scale}Z" fill="#3a2f7a"/>'
          f'<path d="M{cx-62*scale},{y+8*scale} L{cx+8*scale},{y-190*scale} Q{cx+30*scale},{y-170*scale} {cx+62*scale},{y+8*scale}Z" fill="#4a3d99"/>'
          f'<path d="M{cx-60*scale},{y-8*scale} Q{cx},{y-28*scale} {cx+60*scale},{y-8*scale}" stroke="{GOLD}" stroke-width="{10*scale}" fill="none"/>'
          f'{star(cx+8*scale, y-195*scale, 26*scale, GOLD)}</g>')
    s += face(cx, y + 92*scale, 2.1*scale, mood)
    # 小手
    s += f'<path d="M{x+4*scale},{y+150*scale} q{-40*scale},{10*scale} {-52*scale},{40*scale}" stroke="{col}" stroke-width="{16*scale}" stroke-linecap="round" fill="none"/>'
    if wand:
        s += f'<path d="M{x+w-4*scale},{y+150*scale} q{40*scale},{-10*scale} {58*scale},{-50*scale}" stroke="{col}" stroke-width="{16*scale}" stroke-linecap="round" fill="none"/>'
        s += f'<line x1="{x+w+50*scale}" y1="{y+108*scale}" x2="{x+w+110*scale}" y2="{y-10*scale}" stroke="#7a5a2e" stroke-width="{10*scale}" stroke-linecap="round"/>'
        s += star(x+w+116*scale, y-24*scale, 30*scale, GOLD)
        s += "".join(sparkle(x+w+116*scale+dx*scale, y-24*scale+dy*scale, 10*scale) for dx, dy in ((60,-30),(-40,-70),(70,40)))
    else:
        s += f'<path d="M{x+w-4*scale},{y+150*scale} q{40*scale},{10*scale} {52*scale},{40*scale}" stroke="{col}" stroke-width="{16*scale}" stroke-linecap="round" fill="none"/>'
    return s

def star(cx, cy, r, col, op=1):
    import math
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = -math.pi/2 + i * math.pi/5
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{col}" opacity="{op}"/>'

def sparkle(cx, cy, r, col=GOLD):
    return f'<path d="M{cx},{cy-r} Q{cx},{cy} {cx+r},{cy} Q{cx},{cy} {cx},{cy+r} Q{cx},{cy} {cx-r},{cy} Q{cx},{cy} {cx},{cy-r}Z" fill="{col}"/>'

def sky(tint=None):
    random.seed(3)
    s = ('<defs><radialGradient id="bg" cx="50%" cy="35%" r="80%"><stop offset="0" stop-color="#2b2556"/>'
         '<stop offset="1" stop-color="#0d0b1e"/></radialGradient>'
         '<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff" stop-opacity=".5"/>'
         '<stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1080" height="1920" fill="url(#bg)"/>')
    if tint:
        s += f'<rect width="1080" height="1920" fill="{tint}" opacity=".16"/>'
    for _ in range(70):
        x, y, r = random.randint(0,1080), random.randint(0,1920), random.choice([1.2,1.6,2.2,3])
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{random.choice([GOLD,"#fff","#fff"])}" opacity="{random.uniform(.25,.8):.2f}"/>'
    for _ in range(6):
        s += sparkle(random.randint(60,1020), random.randint(200,1700), random.randint(8,14), "#fff8e1")
    return s

def chrome():
    return (f'<text x="540" y="128" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="44" fill="{GOLD}" letter-spacing="4">Hanna｜K棒魔法師</text>'
            f'<line x1="380" y1="160" x2="700" y2="160" stroke="{GOLD}" stroke-opacity=".35" stroke-width="2"/>'
            f'<text x="540" y="1830" text-anchor="middle" font-family="Noto Sans TC" font-size="34" fill="{INK}" opacity=".7" letter-spacing="2">@_hannapang</text>')

def progress(n):
    s = f'<rect x="460" y="230" width="160" height="58" rx="29" fill="{GOLD}"/><text x="540" y="271" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="32" fill="#1d1a33">{n:02d} / 08</text>'
    s += "".join(star(372 + i*48, 330, 14, GOLD if i < n else "#5b5488") for i in range(8))
    return s

def book(inner):
    s = ('<g><path d="M120,420 Q330,380 540,430 Q750,380 960,420 L960,1060 Q750,1020 540,1070 Q330,1020 120,1060Z" fill="#1c1838" stroke="#e9b95a" stroke-width="4"/>'
         '<path d="M540,430 L540,1070" stroke="#e9b95a" stroke-opacity=".5" stroke-width="3"/>'
         '<path d="M150,450 Q330,415 520,455 L520,1040 Q330,1000 150,1030Z" fill="#241f47"/>'
         '<path d="M560,455 Q750,415 930,450 L930,1030 Q750,1000 560,1040Z" fill="#241f47"/></g>')
    return s + inner

def question(i, answered):
    k1, k2, ans = QS[i]
    tint = (G if ans == "多" else R) if answered else None
    m1 = m2 = "surprised"
    if answered:
        m1, m2 = ("scared", "happy") if ans == "多" else ("scared", "smug")
        if ans == "多" and k1[1] < k1[0]: m1 = "happy"
        if ans == "空" and k1[1] > k1[0]: m1 = "dizzy"
    s = sky(tint) + chrome() + progress(i+1)
    lo, hi = min(k1[2], k2[2]), max(k1[3], k2[3])
    norm = lambda k: tuple((v - lo) / (hi - lo) * 100 for v in k)
    s += book(kbar(270, 520, 990, norm(k1), 120, m1) + kbar(690, 520, 990, norm(k2), 120, m2))
    if answered:
        col = G if ans == "多" else R
        label = "▲ 做多" if ans == "多" else "▼ 做空"
        s += (f'<ellipse cx="540" cy="1245" rx="300" ry="70" fill="none" stroke="{col}" stroke-width="4" opacity=".8"/>'
              f'<ellipse cx="540" cy="1245" rx="250" ry="52" fill="none" stroke="{GOLD}" stroke-width="2" stroke-dasharray="8 10" opacity=".9"/>'
              f'<circle cx="540" cy="1220" r="210" fill="url(#glow)" opacity=".35"/>')
        s += "".join(sparkle(540+dx, 1210+dy, r) for dx, dy, r in ((-300,-60,16),(290,-80,20),(-220,60,10),(250,50,12),(0,-120,14)))
        s += f'<text x="540" y="1250" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="120" fill="{col}" stroke="#0d0b1e" stroke-width="3" paint-order="stroke">{label}</text>'
    s += (f'<text x="540" y="1470" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="72" fill="{INK}">'
          f'<tspan fill="{G}">做多</tspan>還是<tspan fill="{R}">做空</tspan>？</text>')
    return s

def hook():
    s = sky() + chrome()
    s += f'<rect x="420" y="300" width="240" height="84" rx="42" fill="{GOLD}"/><text x="540" y="360" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="#1d1a33">8 題</text>'
    s += hero(390, 1020, G, "happy", wand=True) + hero(700, 1040, R, "scared", hat_tilt=14, scale=0.92)
    s += (f'<text x="540" y="1340" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="96" fill="{GOLD}">K 棒魔法測驗</text>'
          f'<text x="540" y="1460" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="60" fill="{INK}">1 秒判斷，8 題你能<tspan fill="{GOLD}">全對</tspan>嗎？</text>')
    return s

def cards():
    s = sky() + chrome()
    s += (f'<text x="540" y="300" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="78" fill="{GOLD}">K 棒咒語卡</text>'
          f'<text x="540" y="380" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="44" fill="{INK}">8 種一次帶走</text>')
    for i, (k1, k2, ans) in enumerate(QS):
        cx, cy = 90 + (i % 4) * 232, 460 + (i // 4) * 420
        col = G if ans == "多" else R
        s += f'<rect x="{cx}" y="{cy}" width="208" height="380" rx="22" fill="#1c1838" stroke="{GOLD}" stroke-opacity=".6" stroke-width="3"/>'
        s += star(cx+28, cy+30, 11, GOLD)
        s += kbar(cx+42, cy+60, cy+290, k1, 52, faces=False) + kbar(cx+114, cy+60, cy+290, k2, 52, faces=False)
        s += f'<text x="{cx+104}" y="{cy+350}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{col}">{"▲ 做多" if ans == "多" else "▼ 做空"}</text>'
    s += (f'<text x="540" y="1420" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="66" fill="{INK}">📌 先收藏！</text>'
          f'<text x="540" y="1510" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="{GOLD}">看盤前打開對一遍</text>')
    # 發光收藏書籤＋魔杖指向右下
    s += f'<circle cx="930" cy="1690" r="90" fill="url(#glow)"/><path d="M900,1640 h60 v100 l-30,-24 l-30,24Z" fill="{GOLD}"/>'
    s += f'<line x1="700" y1="1610" x2="850" y2="1670" stroke="#7a5a2e" stroke-width="9" stroke-linecap="round"/>' + star(860, 1675, 22, GOLD)
    s += "".join(sparkle(x, y, r) for x, y, r in ((820,1610,10),(990,1610,12),(1000,1760,9)))
    return s

def ending():
    s = sky() + chrome()
    s += "".join(star(520+dx, 640+dy, r, GOLD, op) for dx, dy, r, op in ((180,-120,20,.9),(230,-230,16,.7),(280,-330,13,.5),(330,-420,10,.35)))
    s += hero(480, 1000, G, "happy", wand=True, scale=1.05)
    s += (f'<text x="540" y="1300" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="70" fill="{GOLD}">錯了幾題？留言告訴我</text>'
          f'<text x="540" y="1420" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="46" fill="{INK}">看不懂也沒關係</text>'
          f'<text x="540" y="1490" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="48" fill="{INK}"><tspan fill="{GOLD}">3+1 指標</tspan>直接告訴你做多還是做空</text>'
          f'<rect x="250" y="1560" width="580" height="100" rx="50" fill="{GOLD}"/>'
          f'<text x="540" y="1625" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="46" fill="#1d1a33">方法放在主頁 Portaly 👆</text>')
    return s

frames = [("01_開場", hook()), ("02_題目_未揭曉", question(0, False)), ("03_題目_做多", question(0, True)),
          ("04_題目_做空", question(7, True)), ("05_咒語卡_收藏", cards()), ("06_結尾_導流", ending())]
html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&display=block" rel="stylesheet">'
        '<style>body{margin:0;background:#000}svg{display:block;margin-bottom:10px}</style></head><body>'
        + "".join(f'<svg id="{n}" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">{f}</svg>' for n, f in frames)
        + '<script>document.fonts.ready.then(()=>{document.body.dataset.ready="1"})</script></body></html>')
open(os.path.join(OUT, "mockup.html"), "w", encoding="utf-8").write(html)
print([n for n, _ in frames])
