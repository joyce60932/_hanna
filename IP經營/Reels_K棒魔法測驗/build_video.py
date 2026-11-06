"""K 棒魔法測驗 Reels：逐格產生 SVG（30fps、18.13 秒），節拍對齊參考影片的音樂。

參考影片量到的重拍（背景閃光）時間：0.77、2.23、3.73、5.20、6.67、8.17、9.63、11.13、12.60、14.10、15.57、17.07 秒，
大約每 1.48 秒一拍。8 題的答案都落在重拍上。
"""
import os, sys, json, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_mockup_v2 import (QS, G, R, GOLD, INK, NAVY, DEFS, star, sparkle, kbar, hero, chrome, book)

FPS, DUR = 30, 18.13
ANS = [2.23, 3.73, 5.20, 6.67, 8.17, 9.63, 11.13, 12.60]          # 每題答案揭曉（重拍）
START = [1.50] + [a + 0.60 for a in ANS[:-1]]                        # 每題開始
SUMMARY, SUM_BEAT, END, END_BEAT1, END_BEAT2 = 13.33, 14.10, 15.40, 15.57, 17.07
HOOK_BEAT = 0.77

clamp = lambda x, a=0.0, b=1.0: max(a, min(b, x))
def ease_out(x): x = clamp(x); return 1 - (1 - x) ** 3
def back(x):
    x = clamp(x); c = 1.9
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def pop(t, t0, d=0.22): return back((t - t0) / d) if t >= t0 else 0.0
def g(inner, cx=540, cy=960, sc=1.0, op=1.0, dx=0, dy=0, rot=0):
    if op <= 0.001 or sc <= 0.001: return ""
    return f'<g opacity="{op:.3f}" transform="translate({cx+dx:.1f} {cy+dy:.1f}) rotate({rot:.2f}) scale({sc:.4f}) translate({-cx} {-cy})">{inner}</g>'

random.seed(3)
STARS = [(random.randint(0,1080), random.randint(0,1920), random.choice([1.2,1.6,2,2.6,3.2]), random.choice([GOLD,"#fff","#fff","#bfe8ff"]), random.uniform(0, 6.28), random.uniform(1.5, 4)) for _ in range(110)]
SPARK = [(random.randint(40,1040), random.randint(180,1780), random.randint(7,18), random.choice(["#fff8e1", GOLD]), random.uniform(0,6.28)) for _ in range(12)]

def sky(t, tint=None, flash=0.0):
    s = DEFS + '<rect width="1080" height="1920" fill="url(#bg)"/>'
    s += '<ellipse cx="180" cy="520" rx="420" ry="300" fill="url(#neb1)"/><ellipse cx="930" cy="1350" rx="460" ry="330" fill="url(#neb2)"/><ellipse cx="820" cy="300" rx="300" ry="220" fill="url(#neb1)"/>'
    if tint:
        s += f'<rect width="1080" height="1920" fill="{tint}" opacity="{0.22 + 0.35*flash:.3f}"/><ellipse cx="540" cy="1200" rx="620" ry="520" fill="{tint}" opacity=".18" filter="url(#blur)"/>'
    elif flash > 0:
        s += f'<rect width="1080" height="1920" fill="{GOLD}" opacity="{0.35*flash:.3f}"/>'
    s += f'<circle cx="935" cy="250" r="62" fill="#fff3c9" opacity=".95"/><circle cx="960" cy="232" r="56" fill="#22194d"/><circle cx="935" cy="250" r="110" fill="url(#glow)" opacity=".35"/>'
    for x, y, r, c, ph, sp in STARS:
        s += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" opacity="{0.25 + 0.7*(0.5+0.5*math.sin(t*sp+ph)):.2f}"/>'
    for x, y, r, c, ph in SPARK:
        k = 0.6 + 0.4 * math.sin(t*3 + ph)
        s += sparkle(x, y, r*k, c, 0.5 + 0.5*k)
    pts = [(70,330),(150,280),(230,320),(270,250)]
    s += "".join(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="#cfc6ff" stroke-opacity=".35" stroke-width="2"/>' for a, b in zip(pts, pts[1:]))
    s += "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#fff"/>' for x, y in pts)
    return s

def flash_at(t, beats, d=0.28):
    return max([clamp(1 - (t - b) / d) for b in beats if t >= b] + [0.0])

def progress_t(t, n, t0):
    pp = pop(t, t0)
    s = g(f'<rect x="452" y="222" width="176" height="64" rx="32" fill="{GOLD}"/><text x="540" y="266" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="34" fill="{NAVY}">{n:02d} / 08</text>', 540, 254, pp)
    for i in range(8):
        on = i < n
        cx = 372 + i*48
        if on and i == n-1:
            k = pop(t, t0 + 0.05)
            s += f'<circle cx="{cx}" cy="330" r="{26*k:.1f}" fill="url(#glow)"/>' + g(star(cx, 330, 16, GOLD), cx, 330, k)
        else:
            s += star(cx, 330, 16 if on else 13, GOLD if on else "#5c5490")
    return s

def moods(k1, k2, ans, answered):
    if not answered: return ("surprised","side","surprised","up")
    if ans == "多":
        m1 = ("happy","up") if k1[1] < k1[0] else ("scared","cheeks")
        m2 = ("stars","up") if k2[1] < k2[0] else ("happy","up")
    else:
        m1 = ("scared","cheeks") if k1[1] < k1[0] else ("dizzy","side")
        m2 = ("smug","hip")
    return m1 + m2

def question_frame(t, i):
    k1, k2, ans = QS[i]
    col = G if ans == "多" else R
    A, S = ANS[i], START[i]
    answered = t >= A
    C1, C2 = S + 0.12, A - 0.42
    out_t = (START[i+1] if i < 7 else SUMMARY)
    leave = clamp((t - (out_t - 0.12)) / 0.12)            # 換題前 0.12 秒淡出
    fl = flash_at(t, [A]) if answered else 0
    s = sky(t, col if answered else None, fl)
    if answered:
        k = ease_out((t - A) / 0.3)
        rot = (t - A) * 12
        rays = "".join(f'<path d="M540,1260 L{540+math.cos(a-.06)*620},{1260+math.sin(a-.06)*620} L{540+math.cos(a+.06)*620},{1260+math.sin(a+.06)*620}Z" fill="{col}" opacity=".18"/>' for a in [j*math.pi/9 for j in range(18)])
        s += g(rays, 540, 1260, 0.4 + 0.6*k, 1 - leave, rot=rot)
    s += chrome() + progress_t(t, i+1, S)
    bk = ease_out((t - S) / 0.18)
    s += g(book(), 540, 760, 0.94 + 0.06*bk, bk * (1 - leave))
    lo, hi = min(k1[2], k2[2]), max(k1[3], k2[3])
    norm = lambda k: tuple((v - lo) / (hi - lo) * 100 for v in k)
    m1, p1, m2, p2 = moods(k1, k2, ans, answered)
    bob = math.sin(t * 6) * 6
    if t >= C1:
        s += g(kbar(250, 530, 990, norm(k1), 130, m1, p1), 315, 760, pop(t, C1), 1 - leave, dy=bob)
    if t >= C2:
        k = pop(t, C2, 0.2)
        jump = -40 * clamp(1 - (t - A) / 0.2) if answered else 0
        s += g(kbar(700, 530, 990, norm(k2), 130, m2, p2), 765, 760, k, 1 - leave, dy=-bob + jump)
        if not answered:
            sw = clamp((t - C2) / 0.25)
            s += g("".join(f'<line x1="{765+math.cos(a)*120}" y1="{560+math.sin(a)*120}" x2="{765+math.cos(a)*(120+40*sw)}" y2="{560+math.sin(a)*(120+40*sw)}" stroke="{GOLD}" stroke-width="7" stroke-linecap="round"/>' for a in [math.radians(d) for d in (-160,-125,-90,-55,-20)])
                   + f'<text x="900" y="520" font-family="Noto Serif TC" font-weight="900" font-size="54" fill="{GOLD}" transform="rotate(12 900 520)">咻！</text>', 765, 560, 1, 1 - clamp((t - C2 - 0.3) / 0.1))
    if not answered and t >= C1:
        q = pop(t, C1 + 0.05)
        s += g(f'<text x="540" y="1290" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="150" fill="{INK}" opacity=".9">？</text>', 540, 1240, q * (1 + 0.06*math.sin(t*10)))
    if answered:
        cy = 1260
        k = pop(t, A, 0.26)
        circle = (f'<ellipse cx="540" cy="{cy+20}" rx="340" ry="92" fill="none" stroke="{col}" stroke-width="6"/>'
                  f'<ellipse cx="540" cy="{cy+20}" rx="292" ry="74" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 12" stroke-dashoffset="{-(t-A)*120:.1f}"/>'
                  f'<ellipse cx="540" cy="{cy+20}" rx="240" ry="58" fill="{col}" opacity=".18"/>'
                  + "".join(star(540+math.cos(a)*316, cy+20+math.sin(a)*83, 10, GOLD) for a in [j*math.pi/4 + (t-A)*1.5 for j in range(8)]))
        s += g(circle, 540, cy+20, ease_out((t - A) / 0.25), 1 - leave)
        s += g(f'<circle cx="540" cy="{cy-40}" r="260" fill="url(#glow)" opacity=".45"/>'
               f'<text x="540" y="{cy+10}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="140" fill="{col}" stroke="#fff8e8" stroke-width="5" paint-order="stroke">{"▲ 做多" if ans == "多" else "▼ 做空"}</text>', 540, cy-40, k, 1 - leave)
        random.seed(i + 20)
        conf = ""
        for _ in range(14):
            x0, y0 = 540, 1230
            x1, y1 = random.randint(90, 990), random.randint(1110, 1420)
            p = ease_out((t - A) / 0.35)
            conf += star(x0 + (x1-x0)*p, y0 + (y1-y0)*p + 30*(t-A), random.randint(8, 16), random.choice([GOLD, col, "#fff"]), .95)
        s += g(conf, op=1 - leave)
    s += g(f'<text x="540" y="1530" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{INK}"><tspan fill="{G}">做多</tspan>還是<tspan fill="{R}">做空</tspan>？</text>', 540, 1510, 1, ease_out((t - S) / 0.15) * (1 - leave))
    return s

def hook_frame(t):
    fl = flash_at(t, [HOOK_BEAT])
    s = sky(t, None, fl) + chrome()
    b = pop(t, HOOK_BEAT - 0.08)
    s += g(f'<circle cx="540" cy="335" r="110" fill="url(#glow)" opacity=".7"/><rect x="410" y="285" width="260" height="96" rx="48" fill="{GOLD}"/><text x="540" y="353" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="{NAVY}">8 題</text>', 540, 335, b)
    s += g(sparkle(380, 300, 16) + sparkle(710, 290, 12, GOLD) + sparkle(700, 390, 10), op=b)
    h1 = pop(t, 0.0, 0.3); h2 = pop(t, 0.12, 0.3)
    s += g(hero(360, 1040, G, "happy", wand=True, tilt=-8 + 4*math.sin(t*5)), 360, 1040, h1, dy=math.sin(t*6)*10)
    s += g(hero(760, 1060, R, "scared", tilt=8, hat_tilt=16, scale=.9), 760, 1060, h2, dx=math.sin(t*40)*3)
    s += g(f'<text x="660" y="720" font-family="Noto Serif TC" font-weight="900" font-size="48" fill="{INK}" transform="rotate(10 660 720)">嚇！</text>', 680, 700, pop(t, 0.35))
    tt = ease_out((t - 0.2) / 0.3)
    s += g(f'<text x="540" y="1380" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="104" fill="{GOLD}" stroke="#2a1f55" stroke-width="6" paint-order="stroke">K 棒魔法測驗</text>', 540, 1350, 0.9 + 0.1*tt, tt)
    s += g(f'<text x="540" y="1500" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="62" fill="{INK}">1 秒判斷，8 題你能<tspan fill="{GOLD}">全對</tspan>嗎？</text>', 540, 1480, 1, ease_out((t - 0.4) / 0.3), dy=20*(1-ease_out((t-0.4)/0.3)))
    leave = clamp((t - 1.38) / 0.12)
    if leave > 0:
        s += f'<rect width="1080" height="1920" fill="#0d0b1e" opacity="{leave:.2f}"/>'
    return s

def summary_frame(t):
    fl = flash_at(t, [SUM_BEAT])
    s = sky(t, None, fl * 0.8) + chrome()
    tt = pop(t, SUMMARY)
    s += g(f'<text x="540" y="300" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="86" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">K 棒咒語卡</text>'
           f'<text x="540" y="380" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="46" fill="{INK}">8 種一次帶走</text>', 540, 330, tt)
    for i, (k1, k2, ans) in enumerate(QS):
        t0 = SUMMARY + 0.1 + i * 0.08
        if t < t0: continue
        cx, cy = 86 + (i % 4) * 232, 450 + (i // 4) * 420
        col = G if ans == "多" else R
        lo, hi = min(k1[2], k2[2]), max(k1[3], k2[3])
        norm = lambda k: tuple((v - lo) / (hi - lo) * 100 for v in k)
        card = (f'<rect x="{cx-6}" y="{cy-6}" width="220" height="392" rx="26" fill="{col}" opacity=".35" filter="url(#blur2)"/>'
                f'<rect x="{cx}" y="{cy}" width="208" height="380" rx="22" fill="#1a1640" stroke="{GOLD}" stroke-width="3"/>'
                f'<rect x="{cx+10}" y="{cy+10}" width="188" height="360" rx="16" fill="none" stroke="{GOLD}" stroke-opacity=".3" stroke-width="2" stroke-dasharray="6 8"/>'
                + star(cx+30, cy+32, 11, GOLD) + f'<text x="{cx+182}" y="{cy+44}" text-anchor="end" font-family="Noto Sans TC" font-weight="700" font-size="26" fill="{GOLD}">{i+1:02d}</text>'
                + kbar(cx+40, cy+70, cy+290, norm(k1), 54, faces=False, glow=False) + kbar(cx+114, cy+70, cy+290, norm(k2), 54, faces=False, glow=False)
                + f'<text x="{cx+104}" y="{cy+350}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{col}">{"▲ 做多" if ans == "多" else "▼ 做空"}</text>')
        p = ease_out((t - t0) / 0.22)
        s += g(card, cx+104, cy+190, 0.6 + 0.4*back((t - t0) / 0.22), p, dy=(1-p)*-120, rot=(1-p)*-12)
    sv = pop(t, SUM_BEAT - 0.05, 0.25)
    s += g(f'<text x="540" y="1420" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="72" fill="{INK}">📌 先收藏！</text>'
           f'<text x="540" y="1515" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="60" fill="{GOLD}">看盤前打開對一遍</text>', 540, 1460, sv)
    if t >= SUM_BEAT:
        ph = (t - SUM_BEAT) % 0.74 / 0.74
        bm = f'<circle cx="930" cy="1690" r="130" fill="url(#glow)"/>'
        bm += "".join(f'<circle cx="930" cy="1690" r="{r + 40*ph:.1f}" fill="none" stroke="{GOLD}" stroke-opacity="{op*(1-ph):.2f}" stroke-width="4"/>' for r, op in ((86,.8),(112,.5),(138,.3)))
        bm += f'<path d="M898,1636 h64 v108 l-32,-26 l-32,26Z" fill="{GOLD}" stroke="#fff3c9" stroke-width="4"/>'
        wob = math.sin((t - SUM_BEAT) * 9) * 10
        bm += g(f'<line x1="640" y1="1600" x2="820" y2="1668" stroke="#8a6234" stroke-width="11" stroke-linecap="round"/>' + star(832, 1673, 26, GOLD, 1, .45, "#fff3c9"), 820, 1668, 1, dx=wob)
        bm += f'<text x="560" y="1700" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{GOLD}">點這裡收藏 →</text>'
        s += g(bm, 930, 1690, pop(t, SUM_BEAT, 0.25))
    leave = clamp((t - (END - 0.1)) / 0.1)
    if leave > 0:
        s += f'<rect width="1080" height="1920" fill="#0d0b1e" opacity="{leave:.2f}"/>'
    return s

def end_frame(t):
    fl = flash_at(t, [END_BEAT1, END_BEAT2])
    s = sky(t, None, fl * 0.8) + chrome()
    h = pop(t, END, 0.3)
    s += g(hero(470, 1010, G, "stars", wand=True, tilt=-6 + 5*math.sin(t*5), scale=1.1), 470, 1000, h, dy=math.sin(t*6)*12)
    a = ease_out((t - END - 0.15) / 0.25)
    s += g(f'<text x="540" y="1310" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">錯了幾題？留言告訴我</text>', 540, 1290, 0.9 + 0.1*a, a)
    b = ease_out((t - END - 0.35) / 0.25)
    s += g(f'<text x="540" y="1430" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="48" fill="{INK}">看不懂也沒關係</text>'
           f'<text x="540" y="1505" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{INK}"><tspan fill="{GOLD}">3+1 指標</tspan>直接告訴你做多還是做空</text>', 540, 1460, 1, b, dy=20*(1-b))
    c = pop(t, END + 0.55, 0.25)
    pulse = 1 + 0.08 * flash_at(t, [END_BEAT2], 0.4)
    btn = (f'<rect x="220" y="1580" width="640" height="110" rx="55" fill="{GOLD}"/><rect x="220" y="1580" width="640" height="110" rx="55" fill="none" stroke="#fff3c9" stroke-width="4"/>'
           f'<text x="540" y="1652" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="50" fill="{NAVY}">方法放在主頁 Portaly 👆</text>')
    s += g(btn, 540, 1635, c * pulse)
    s += g("".join(sparkle(x, y, r, col) for x, y, r, col in ((190,1590,16,GOLD),(890,1580,14,"#fff"),(900,1700,10,GOLD))), op=c)
    return s

def frame(t):
    if t < START[0]: return hook_frame(t)
    if t < SUMMARY:
        i = max(j for j in range(8) if START[j] <= t)
        return question_frame(t, i)
    if t < END: return summary_frame(t)
    return end_frame(t)

if __name__ == "__main__":
    out = sys.argv[1]
    n = int(round(DUR * FPS))
    with open(out, "w", encoding="utf-8") as f:
        for k in range(n):
            f.write(json.dumps(frame(k / FPS), ensure_ascii=False) + "\n")
    print(n, "frames")
