"""K 棒魔法測驗 Ep.2「這根 K 棒是誰贏？」mockup。沿用 Ep.1 的魔法風格元件。"""
import os, sys, math, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Reels_K棒魔法測驗"))
from build_mockup_v2 import G, R, GOLD, INK, NAVY, star, sparkle, kbar, hero, chrome, book, sky

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "mockup_preview")

# 單根 K 棒（開, 收, 高, 低），0 在上；答案、顏色、解析、揭曉表情
QS = [
    ((88, 12,  8, 92), "買方贏",     G,    "從頭漲到尾",       "stars"),
    ((12, 88,  8, 92), "賣方贏",     R,    "從頭跌到尾",       "smug"),
    ((93, 73,  6, 95), "賣方佔上風", R,    "雖然收紅，但漲上去又被賣下來", "scared"),
    ((30, 10,  7, 93), "買方贏",     G,    "跌下去又被買回來", "happy"),
    ((50, 50, 14, 86), "平手",       GOLD, "多空在猶豫，先別急", None),
]
TRAP = 2

def doji(cx, top, bottom, k, w):
    o, c, h, l = k
    Y = lambda v: top + (bottom - top) * v / 100
    return (f'<line x1="{cx}" y1="{Y(h)}" x2="{cx}" y2="{Y(l)}" stroke="{GOLD}" stroke-width="{max(w*.09,3)}" stroke-linecap="round"/>'
            f'<rect x="{cx-w/2}" y="{Y(o)-max(w*.06,3)}" width="{w}" height="{max(w*.12,6)}" rx="{max(w*.06,3)}" fill="{GOLD}"/>')

def header(n, trap=False):
    s = chrome()
    s += f'<text x="540" y="212" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{INK}"><tspan fill="{GOLD}">Ep.2</tspan>｜這根 K 棒是誰贏？</text>'
    pill = R if trap else GOLD
    s += f'<rect x="452" y="248" width="176" height="62" rx="31" fill="{pill}"/><text x="540" y="291" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="34" fill="{NAVY if not trap else "#fff"}">{n:02d} / 05</text>'
    for i in range(5):
        on = i < n
        s += star(444 + i*48, 350, 16 if on else 13, (R if trap and i == n-1 else GOLD) if on else "#5c5490")
    return s

def save_hint():
    return (f'<rect x="300" y="1690" width="480" height="70" rx="35" fill="#1a1640" stroke="{GOLD}" stroke-width="3"/>'
            f'<text x="540" y="1738" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="36" fill="{GOLD}">📌 最後有 5 張咒語卡</text>')

def question(i, answered):
    k, verdict, col, why, mood = QS[i]
    trap = i == TRAP
    s = sky(col if answered else (R if trap else None))
    if answered:
        s += "".join(f'<path d="M540,1250 L{540+math.cos(a-.06)*640},{1250+math.sin(a-.06)*640} L{540+math.cos(a+.06)*640},{1250+math.sin(a+.06)*640}Z" fill="{col}" opacity=".16"/>' for a in [j*math.pi/9 for j in range(18)])
    s += header(i+1, trap) + book()
    if i == 4:
        s += f'<rect x="440" y="740" width="200" height="60" rx="30" fill="{GOLD}" opacity=".45" filter="url(#blur)"/>' + doji(540, 500, 1040, k, 200)
    else:
        s += kbar(540-75, 500, 1040, k, 150, (mood or "surprised") if answered else "surprised", "up" if answered and col == G else ("cheeks" if answered and trap else ("hip" if answered and col == R else "side")))
    if i == 4:  # 十字線沒有臉，用問號表現猶豫
        s += "".join(f'<text x="{x}" y="{y}" font-family="Noto Serif TC" font-weight="900" font-size="{sz}" fill="{GOLD}" transform="rotate({r} {x} {y})">?</text>' for x, y, sz, r in ((640,690,70,15),(400,760,56,-15),(650,880,44,10)))
    if trap:
        s += (f'<g transform="rotate(-8 880 470)"><rect x="770" y="430" width="230" height="74" rx="18" fill="{R}"/>'
              f'<text x="885" y="481" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="#fff">⚠️ 陷阱題</text></g>')
    if not answered:
        s += f'<text x="540" y="1290" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="150" fill="{INK}" opacity=".9">？</text>'
        s += (f'<text x="540" y="1480" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="66" fill="{INK}">'
              f'<tspan fill="{G}">買方贏</tspan>？還是<tspan fill="{R}">賣方贏</tspan>？</text>')
        if i == 0:
            s += (f'<rect x="250" y="1550" width="580" height="84" rx="42" fill="{GOLD}"/>'
                  f'<text x="540" y="1606" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{NAVY}">第 3 題，最多人答錯</text>')
    else:
        cy = 1250
        s += (f'<ellipse cx="540" cy="{cy+20}" rx="360" ry="92" fill="none" stroke="{col}" stroke-width="6"/>'
              f'<ellipse cx="540" cy="{cy+20}" rx="310" ry="74" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 12"/>'
              f'<circle cx="540" cy="{cy-40}" r="260" fill="url(#glow)" opacity=".45"/>')
        s += "".join(star(540+math.cos(a)*336, cy+20+math.sin(a)*83, 10, GOLD) for a in [j*math.pi/4 for j in range(8)])
        size = 120 if len(verdict) <= 3 else 104
        s += f'<text x="540" y="{cy+10}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{size}" fill="{col}" stroke="#fff8e8" stroke-width="5" paint-order="stroke">{verdict}</text>'
        random.seed(i + 40)
        s += "".join(star(random.randint(90, 990), random.randint(1110, 1400), random.randint(8, 15), random.choice([GOLD, col, "#fff"]), .9) for _ in range(12))
        s += (f'<rect x="120" y="1420" width="840" height="110" rx="26" fill="#1a1640" fill-opacity=".85" stroke="{col}" stroke-width="3"/>'
              f'<text x="540" y="1492" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{46 if len(why) <= 10 else 40}" fill="{INK}">{why}</text>')
    return s + save_hint()

def cards():
    s = sky(seed=5) + chrome()
    s += (f'<text x="540" y="290" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="84" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">K 棒咒語卡 Ep.2</text>'
          f'<text x="540" y="370" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="46" fill="{INK}">這根 K 棒是誰贏？5 種一次帶走</text>')
    pos = [(60, 440), (390, 440), (720, 440), (225, 920), (555, 920)]
    for i, ((k, verdict, col, why, _), (x, y)) in enumerate(zip(QS, pos)):
        s += f'<rect x="{x-6}" y="{y-6}" width="312" height="452" rx="28" fill="{col}" opacity=".3" filter="url(#blur2)"/>'
        s += f'<rect x="{x}" y="{y}" width="300" height="440" rx="24" fill="#1a1640" stroke="{GOLD}" stroke-width="3"/>'
        s += f'<rect x="{x+10}" y="{y+10}" width="280" height="420" rx="18" fill="none" stroke="{GOLD}" stroke-opacity=".3" stroke-width="2" stroke-dasharray="6 8"/>'
        s += star(x+32, y+34, 11, GOLD) + f'<text x="{x+270}" y="{y+46}" text-anchor="end" font-family="Noto Sans TC" font-weight="700" font-size="26" fill="{GOLD if i != TRAP else R}">{"⚠️ " if i == TRAP else ""}{i+1:02d}</text>'
        s += doji(x+150, y+64, y+290, k, 70) if i == 4 else kbar(x+122, y+64, y+290, k, 56, faces=False, glow=False)
        s += f'<text x="{x+150}" y="{y+350}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{44 if len(verdict) <= 3 else 38}" fill="{col}">{verdict}</text>'
        short = why if len(why) <= 9 else "漲上去又被賣下來"
        s += f'<text x="{x+150}" y="{y+400}" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="28" fill="{INK}" opacity=".85">{short}</text>'
    s += (f'<text x="540" y="1480" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="70" fill="{INK}">📌 先收藏！</text>'
          f'<text x="540" y="1570" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="{GOLD}">看盤時打開對一遍</text>')
    s += f'<circle cx="930" cy="1700" r="130" fill="url(#glow)"/>'
    s += "".join(f'<circle cx="930" cy="1700" r="{r}" fill="none" stroke="{GOLD}" stroke-opacity="{op}" stroke-width="4"/>' for r, op in ((86,.7),(112,.4),(138,.2)))
    s += f'<path d="M898,1646 h64 v108 l-32,-26 l-32,26Z" fill="{GOLD}" stroke="#fff3c9" stroke-width="4"/>'
    s += f'<line x1="640" y1="1620" x2="820" y2="1680" stroke="#8a6234" stroke-width="11" stroke-linecap="round"/>' + star(832, 1684, 26, GOLD, 1, .45, "#fff3c9")
    s += f'<text x="560" y="1720" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{GOLD}">點這裡收藏 →</text>'
    return s

def ending():
    s = sky(seed=7) + chrome()
    s += hero(470, 1010, G, "stars", wand=True, tilt=-6, scale=1.1)
    s += (f'<text x="540" y="1310" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">錯幾題？留言告訴我</text>'
          f'<text x="540" y="1430" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="48" fill="{INK}">看不懂也沒關係</text>'
          f'<text x="540" y="1505" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{INK}"><tspan fill="{GOLD}">3+1 指標</tspan>直接幫你標好</text>'
          f'<rect x="220" y="1580" width="640" height="110" rx="55" fill="{GOLD}"/><rect x="220" y="1580" width="640" height="110" rx="55" fill="none" stroke="#fff3c9" stroke-width="4"/>'
          f'<text x="540" y="1652" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{NAVY}">方法放在主頁 Portaly 👆</text>')
    return s

if __name__ == "__main__":
    frames = [("ep2_01", question(0, False)), ("ep2_02", question(0, True)), ("ep2_03", question(2, False)),
              ("ep2_04", question(2, True)), ("ep2_05", question(4, True)), ("ep2_06", cards()), ("ep2_07", ending())]
    html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&display=block" rel="stylesheet">'
            '<style>body{margin:0;background:#000}svg{display:block;margin-bottom:10px}</style></head><body>'
            + "".join(f'<svg id="{n}" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">{f}</svg>' for n, f in frames)
            + '<script>document.fonts.ready.then(()=>{document.body.dataset.ready="1"})</script></body></html>')
    open(os.path.join(OUT, "mockup.html"), "w", encoding="utf-8").write(html)
