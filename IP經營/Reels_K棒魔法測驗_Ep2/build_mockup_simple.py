"""K 棒魔法測驗 Ep.2 簡化版 mockup：暗夜空、金色細框、方角 K 棒、答案＋型態名稱。"""
import os, random

G, R, GOLD, INK, SOFT, NAVY = "#4fb98a", "#e0705f", "#e2bd72", "#f3ecdf", "#9a93b8", "#141127"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "mockup_preview")
SERIF, SANS = "Noto Serif TC", "Noto Sans TC"

# 單根 K 棒（開, 收, 高, 低），0 在上；答案、顏色、型態名稱、咒語卡上的一句話
QS = [
    ((86, 14, 9, 91), "買方贏",     G,    "大陽線",   "從頭漲到尾"),
    ((14, 86, 9, 91), "賣方贏",     R,    "大陰線",   "從頭跌到尾"),
    ((92, 74, 8, 95), "賣方佔上風", R,    "長上影線", "漲上去又被賣下來"),
    ((26,  8, 5, 92), "買方贏",     G,    "長下影線", "跌下去又被買回來"),
    ((50, 50, 14, 86), "平手",      GOLD, "十字線",   "多空在猶豫，先別急"),
]
TRAP = 2

def t(x, y, s, size, col=INK, w=900, anchor="middle", font=SERIF, ls=0, op=1):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-weight="{w}" font-size="{size}" fill="{col}" letter-spacing="{ls}" opacity="{op}">{s}</text>'

def bg():
    random.seed(11)
    s = ('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0e0c22"/><stop offset="1" stop-color="#07060f"/></linearGradient>'
         f'<radialGradient id="gl" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{GOLD}" stop-opacity=".35"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient></defs>'
         '<rect width="1080" height="1920" fill="url(#sky)"/>')
    for _ in range(45):
        s += f'<circle cx="{random.randint(0,1080)}" cy="{random.randint(0,1920)}" r="{random.choice([1,1.4,1.8])}" fill="#fff" opacity="{random.uniform(.15,.5):.2f}"/>'
    s += '<circle cx="965" cy="118" r="30" fill="#f4e6bf" opacity=".9"/><circle cx="979" cy="108" r="27" fill="#0e0c22"/>'
    return s

def top():
    return (t(70, 122, "Hanna｜K棒魔法師", 32, GOLD, 700, "start", SERIF, 2)
            + t(540, 262, "這根 K 棒是誰贏？", 66, GOLD)
            + t(540, 314, "K 棒魔法測驗 · Ep.2", 28, SOFT, 700, "middle", SANS, 4))

def progress(n, trap=False):
    col = R if trap else GOLD
    s = f'<rect x="466" y="368" width="148" height="54" rx="27" fill="none" stroke="{col}" stroke-width="3"/>' + t(540, 405, f"{n:02d} / 05", 30, col, 700, "middle", SANS)
    s += "".join(f'<circle cx="{492 + i*24}" cy="452" r="{6 if i == n-1 else 4.5}" fill="{col if i < n else "#3b3757"}"/>' for i in range(5))
    return s

def frame(trap=False):
    s = f'<rect x="150" y="490" width="780" height="620" rx="26" fill="#121027" stroke="{GOLD}" stroke-opacity=".75" stroke-width="3"/>'
    if not trap:
        s += t(900, 530, "示意", 22, SOFT, 400, "end", SANS)
    s += f'<path d="M182,520 l5,12 l12,5 l-12,5 l-5,12 l-5,-12 l-12,-5 l12,-5z" fill="{GOLD}" opacity=".8"/>'
    if trap:
        s += f'<rect x="760" y="470" width="190" height="56" rx="28" fill="{R}"/>' + t(855, 509, "⚠ 陷阱題", 32, "#fff", 900)
    return s

def candle(cx, top_, bot, k, w, col=None, face=None):
    o, c, h, l = k
    Y = lambda v: top_ + (bot - top_) * v / 100
    if o == c:  # 十字線
        col = col or GOLD
        return (f'<line x1="{cx}" y1="{Y(h)}" x2="{cx}" y2="{Y(l)}" stroke="{col}" stroke-width="{max(w*.07,3)}" stroke-linecap="round"/>'
                f'<rect x="{cx-w/2}" y="{Y(o)-max(w*.05,3)}" width="{w}" height="{max(w*.1,6)}" rx="3" fill="{col}"/>')
    col = col or (G if c < o else R)
    bt, bb = Y(min(o, c)), Y(max(o, c))
    s = f'<line x1="{cx}" y1="{Y(h)}" x2="{cx}" y2="{Y(l)}" stroke="{col}" stroke-width="{max(w*.07,3)}" stroke-linecap="round"/>'
    s += f'<rect x="{cx-w/2}" y="{bt}" width="{w}" height="{bb-bt}" rx="{min(w*.06, 8)}" fill="{col}"/>'
    if face and (bb - bt) > w * .45:
        fy, sc = bt + min((bb-bt)*.4, w*.45), w / 150
        if face == "dot":
            s += "".join(f'<circle cx="{cx+d*sc}" cy="{fy}" r="{6*sc}" fill="{NAVY}"/>' for d in (-22, 22))
        elif face == "happy":
            s += "".join(f'<path d="M{cx+d*sc-9*sc},{fy+3*sc} q{9*sc},{-12*sc} {18*sc},0" stroke="{NAVY}" stroke-width="{4.5*sc}" fill="none" stroke-linecap="round"/>' for d in (-22, 22))
            s += f'<path d="M{cx-10*sc},{fy+16*sc} q{10*sc},{10*sc} {20*sc},0" stroke="{NAVY}" stroke-width="{4*sc}" fill="none" stroke-linecap="round"/>'
        elif face == "oops":
            s += "".join(f'<circle cx="{cx+d*sc}" cy="{fy}" r="{7*sc}" fill="{NAVY}"/>' for d in (-22, 22))
            s += f'<ellipse cx="{cx}" cy="{fy+20*sc}" rx="{6*sc}" ry="{8*sc}" fill="{NAVY}"/><path d="M{cx+40*sc},{fy-18*sc} q{6*sc},{10*sc} 0,{15*sc} q{-6*sc},{-5*sc} 0,{-15*sc}" fill="#a8dcff"/>'
        elif face == "smug":
            s += "".join(f'<path d="M{cx+d*sc-9*sc},{fy} h{18*sc}" stroke="{NAVY}" stroke-width="{4.5*sc}" stroke-linecap="round"/>' for d in (-22, 22))
            s += f'<path d="M{cx-8*sc},{fy+16*sc} q{11*sc},{7*sc} {18*sc},{-4*sc}" stroke="{NAVY}" stroke-width="{4*sc}" fill="none" stroke-linecap="round"/>'
    return s

def bursts(cx, cy, col):
    out = ""
    for dx, dy, ex, ey in ((-210,-30,-260,-50),(-215,10,-275,10),(-210,50,-260,70),(210,-30,260,-50),(215,10,275,10),(210,50,260,70)):
        out += f'<line x1="{cx+dx}" y1="{cy+dy}" x2="{cx+ex}" y2="{cy+ey}" stroke="{col}" stroke-width="5" stroke-linecap="round" opacity=".8"/>'
    return out

def bottom(hint=True):
    s = t(540, 1840, "@_hannapang", 30, SOFT, 400, "middle", SANS, 2)
    if hint:
        s += t(540, 1730, "📌 最後有 5 張咒語卡", 34, GOLD, 900)
    return s

FACES = ["happy", "smug", "oops", "happy", None]

def question(i, answered):
    k, verdict, col, name, why = QS[i]
    trap = i == TRAP
    s = bg() + top() + progress(i+1, trap) + frame(trap)
    s += candle(540, 560, 1060, k, 150, face=(FACES[i] if answered else "dot"))
    if answered:
        s += f'<ellipse cx="540" cy="1225" rx="300" ry="90" fill="url(#gl)"/>' + bursts(540, 1210, col)
        s += t(540, 1245, verdict, 92 if len(verdict) <= 3 else 80, col)
        s += f'<rect x="{540-110}" y="1282" width="220" height="56" rx="28" fill="none" stroke="{col}" stroke-width="2.5"/>' + t(540, 1321, name, 32, col, 700, "middle", SANS)
    s += t(540, 1450, f'<tspan fill="{G}">買方贏</tspan>？還是<tspan fill="{R}">賣方贏</tspan>？', 58, INK)
    if i == 0 and not answered:
        s += f'<rect x="300" y="1500" width="480" height="62" rx="31" fill="none" stroke="{GOLD}" stroke-width="2.5"/>' + t(540, 1543, "第 3 題，最多人答錯", 34, GOLD)
    return s + bottom()

def mascot(cx, cy, sc=1.0):
    w, h = 70*sc, 100*sc
    s = f'<line x1="{cx}" y1="{cy-h/2-18*sc}" x2="{cx}" y2="{cy+h/2+18*sc}" stroke="{G}" stroke-width="{5*sc}" stroke-linecap="round"/>'
    s += f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{5*sc}" fill="{G}"/>'
    s += f'<path d="M{cx-48*sc},{cy-h/2+2*sc} Q{cx},{cy-h/2-8*sc} {cx+48*sc},{cy-h/2+2*sc} L{cx+8*sc},{cy-h/2-80*sc}Z" fill="#4a3d99"/>'
    s += f'<path d="M{cx-34*sc},{cy-h/2-8*sc} Q{cx},{cy-h/2-16*sc} {cx+34*sc},{cy-h/2-8*sc}" stroke="{GOLD}" stroke-width="{5*sc}" fill="none"/>'
    s += f'<path d="M{cx+8*sc},{cy-h/2-96*sc} l4,10 l10,4 l-10,4 l-4,10 l-4,-10 l-10,-4 l10,-4z" fill="{GOLD}"/>'
    s += "".join(f'<path d="M{cx+d*sc-7*sc},{cy-12*sc} q{7*sc},{-9*sc} {14*sc},0" stroke="{NAVY}" stroke-width="{3.5*sc}" fill="none" stroke-linecap="round"/>' for d in (-14, 14))
    s += f'<path d="M{cx+w/2},{cy+6*sc} q{26*sc},{-10*sc} {30*sc},{-40*sc}" stroke="{G}" stroke-width="{7*sc}" fill="none" stroke-linecap="round"/>'
    return s

def summary():
    s = bg()
    s += t(70, 122, "Hanna｜K棒魔法師", 32, GOLD, 700, "start", SERIF, 2)
    s += t(540, 250, "K 棒咒語卡 Ep.2", 70, GOLD) + t(540, 305, "截圖收藏，看盤時拿出來對照", 34, SOFT, 700, "middle", SANS)
    cells = [(70, 360), (550, 360), (70, 560), (550, 560), (310, 760)]
    for i, ((k, verdict, col, name, why), (x, y)) in enumerate(zip(QS, cells)):
        s += f'<rect x="{x}" y="{y}" width="460" height="170" rx="18" fill="#121027" stroke="{R if i == TRAP else GOLD}" stroke-opacity=".7" stroke-width="2.5"/>'
        s += candle(x+70, y+22, y+148, k, 38)
        s += t(x+130, y+62, ("⚠ " if i == TRAP else "") + verdict, 38, col, 900, "start")
        s += t(x+130, y+104, name, 28, INK, 700, "start", SANS)
        s += t(x+130, y+142, why, 24, SOFT, 400, "start", SANS)
    s += t(540, 990, "單根 K 棒只是線索，記得看位置和趨勢", 28, SOFT, 400, "middle", SANS)
    s += f'<path d="M515,1060 h50 v80 l-25,-20 l-25,20z" fill="{GOLD}"/><path d="M540,1080 l4,10 l10,4 l-10,4 l-4,10 l-4,-10 l-10,-4 l10,-4z" fill="{NAVY}"/>'
    s += t(540, 1215, "看到這裡，先收藏起來", 60, INK)
    s += f'<line x1="200" y1="1290" x2="880" y2="1290" stroke="{GOLD}" stroke-opacity=".3" stroke-width="2"/>'
    s += t(540, 1380, "錯幾題？留言告訴我", 52, GOLD)
    s += t(540, 1455, f'看不懂？<tspan fill="{GOLD}">3+1 指標</tspan>直接幫你標好', 40, INK)
    s += f'<rect x="220" y="1510" width="640" height="100" rx="50" fill="{GOLD}"/>' + t(540, 1575, "方法放在主頁 Portaly 👆", 46, NAVY)
    s += mascot(540, 1748, .8)
    s += t(540, 1840, "@_hannapang　·　僅供教學參考，非投資建議", 24, SOFT, 400, "middle", SANS)
    return s

if __name__ == "__main__":
    frames = [("ep2s_01", question(0, False)), ("ep2s_02", question(0, True)), ("ep2s_03", question(2, False)),
              ("ep2s_04", question(2, True)), ("ep2s_05", question(4, True)), ("ep2s_06", summary())]
    html = ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&display=block" rel="stylesheet">'
            '<style>body{margin:0;background:#000}svg{display:block;margin-bottom:10px}</style></head><body>'
            + "".join(f'<svg id="{n}" width="1080" height="1920" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">{f}</svg>' for n, f in frames)
            + '<script>document.fonts.ready.then(()=>{document.body.dataset.ready="1"})</script></body></html>')
    open(os.path.join(OUT, "mockup.html"), "w", encoding="utf-8").write(html)
