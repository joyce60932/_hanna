"""K 棒魔法測驗 Ep.2 影片：逐格產生 SVG（30fps、18.13 秒），答案揭曉對在 Ep.1 同一首音樂的重拍。"""
import os, sys, json, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "Reels_K棒魔法測驗"))
from build_video import sky, flash_at, pop, ease_out, back, g, clamp           # Ep.1 的動畫工具
import importlib.util
_spec = importlib.util.spec_from_file_location("ep2_mockup", os.path.join(HERE, "build_mockup.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)          # Ep.1 也有 build_mockup.py，所以用路徑載入
QS, TRAP, header, save_hint, doji, kbar = _m.QS, _m.TRAP, _m.header, _m.save_hint, _m.doji, _m.kbar
G, R, GOLD, INK, NAVY, star, sparkle, chrome, book = _m.G, _m.R, _m.GOLD, _m.INK, _m.NAVY, _m.star, _m.sparkle, _m.chrome, _m.book

FPS, DUR = 30, 18.13
ANS = [2.23, 5.20, 8.17, 11.13, 14.10]                 # 5 題揭曉（每題 2 拍）
START = [0.0] + [a + 1.2 for a in ANS[:-1]]            # 答案和解析停 1.2 秒再換題
SUMMARY, CARD_BEAT, CTA_BEAT = 14.85, 15.57, 17.07

def moods(i, answered):
    k, verdict, col, why, mood = QS[i]
    if not answered: return "surprised", "side"
    if i == TRAP: return "scared", "cheeks"
    return mood, ("up" if col == G else "hip")

def question_frame(t, i):
    k, verdict, col, why, _ = QS[i]
    A, S = ANS[i], START[i]
    trap = i == TRAP
    answered = t >= A
    nxt = START[i+1] if i < 4 else SUMMARY
    leave = clamp((t - (nxt - 0.12)) / 0.12)
    fade = 1 - leave
    fl = flash_at(t, [A]) if answered else 0
    s = sky(t, col if answered else (R if trap else None), fl)
    if answered:
        kk = ease_out((t - A) / 0.3)
        rays = "".join(f'<path d="M540,1250 L{540+math.cos(a-.06)*640},{1250+math.sin(a-.06)*640} L{540+math.cos(a+.06)*640},{1250+math.sin(a+.06)*640}Z" fill="{col}" opacity=".16"/>' for a in [j*math.pi/9 for j in range(18)])
        s += g(rays, 540, 1250, 0.4 + 0.6*kk, fade, rot=(t - A) * 12)
    # 陷阱題揭曉時整個畫面抖一下
    shake = math.sin((t - A) * 70) * 14 * clamp(1 - (t - A) / 0.35) if (trap and answered) else 0
    body = header(i+1, trap) + book()
    C = S + (0.0 if i == 0 else 0.08)
    if t >= C:
        m, p = moods(i, answered)
        bob = math.sin(t * 6) * 6
        jump = -40 * clamp(1 - (t - A) / 0.2) if answered else 0
        if i == 4:
            cand = f'<rect x="440" y="740" width="200" height="60" rx="30" fill="{GOLD}" opacity=".45" filter="url(#blur)"/>' + doji(540, 500, 1040, k, 200)
            wob = math.sin(t * 8) * 3
            cand += "".join(f'<text x="{x}" y="{y}" font-family="Noto Serif TC" font-weight="900" font-size="{sz}" fill="{GOLD}" transform="rotate({r + wob} {x} {y})">?</text>' for x, y, sz, r in ((640,690,70,15),(400,760,56,-15),(650,880,44,10)))
        else:
            cand = kbar(540-75, 500, 1040, k, 150, m, p)
        body += g(cand, 540, 770, pop(t, C, 0.24), fade, dy=bob + jump)
    if trap:
        body += g(f'<g transform="rotate(-8 880 470)"><rect x="770" y="430" width="230" height="74" rx="18" fill="{R}"/>'
                  f'<text x="885" y="481" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="#fff">⚠️ 陷阱題</text></g>', 885, 467,
                  pop(t, S + 0.2) * (1 + 0.06 * math.sin(t * 12)), fade)
    if not answered:
        q = pop(t, C + 0.1)
        body += g(f'<text x="540" y="1290" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="150" fill="{INK}" opacity=".9">？</text>', 540, 1240, q * (1 + 0.06 * math.sin(t * 10)), fade)
        body += g(f'<text x="540" y="1480" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="66" fill="{INK}"><tspan fill="{G}">買方贏</tspan>？還是<tspan fill="{R}">賣方贏</tspan>？</text>', 540, 1460, 1, ease_out((t - S) / 0.15) * fade)
        if i == 0:
            body += g(f'<rect x="250" y="1550" width="580" height="84" rx="42" fill="{GOLD}"/>'
                      f'<text x="540" y="1606" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{NAVY}">第 3 題，最多人答錯</text>', 540, 1592, pop(t, 0.35) * (1 + 0.04 * math.sin(t * 8)))
    else:
        cy = 1250
        ring = (f'<ellipse cx="540" cy="{cy+20}" rx="360" ry="92" fill="none" stroke="{col}" stroke-width="6"/>'
                f'<ellipse cx="540" cy="{cy+20}" rx="310" ry="74" fill="none" stroke="{GOLD}" stroke-width="3" stroke-dasharray="10 12" stroke-dashoffset="{-(t-A)*120:.1f}"/>'
                + "".join(star(540+math.cos(a)*336, cy+20+math.sin(a)*83, 10, GOLD) for a in [j*math.pi/4 + (t-A)*1.5 for j in range(8)]))
        body += g(ring, 540, cy+20, ease_out((t - A) / 0.25), fade)
        size = 120 if len(verdict) <= 3 else 104
        body += g(f'<circle cx="540" cy="{cy-40}" r="260" fill="url(#glow)" opacity=".45"/>'
                  f'<text x="540" y="{cy+10}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{size}" fill="{col}" stroke="#fff8e8" stroke-width="5" paint-order="stroke">{verdict}</text>', 540, cy-40, pop(t, A, 0.26), fade)
        random.seed(i + 40)
        conf = ""
        for _ in range(12):
            x1, y1 = random.randint(90, 990), random.randint(1110, 1400)
            pp = ease_out((t - A) / 0.35)
            conf += star(540 + (x1-540)*pp, 1230 + (y1-1230)*pp + 30*(t-A), random.randint(8, 15), random.choice([GOLD, col, "#fff"]), .9)
        body += g(conf, op=fade)
        e = ease_out((t - A - 0.12) / 0.2)
        body += g(f'<rect x="120" y="1420" width="840" height="110" rx="26" fill="#1a1640" fill-opacity=".85" stroke="{col}" stroke-width="3"/>'
                  f'<text x="540" y="1492" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{46 if len(why) <= 10 else 40}" fill="{INK}">{why}</text>', 540, 1475, 1, e * fade, dy=30*(1-e))
    body += save_hint()
    return s + g(body, dx=shake)

def card(i, x, y):
    k, verdict, col, why, _ = QS[i]
    c = (f'<rect x="{x-6}" y="{y-6}" width="312" height="412" rx="20" fill="{col}" opacity=".3" filter="url(#blur2)"/>'
         f'<rect x="{x}" y="{y}" width="300" height="400" rx="18" fill="#1a1640" stroke="{GOLD}" stroke-width="3"/>'
         f'<rect x="{x+10}" y="{y+10}" width="280" height="380" rx="12" fill="none" stroke="{GOLD}" stroke-opacity=".3" stroke-width="2" stroke-dasharray="6 8"/>'
         + star(x+32, y+34, 11, GOLD) + f'<text x="{x+270}" y="{y+46}" text-anchor="end" font-family="Noto Sans TC" font-weight="700" font-size="26" fill="{GOLD if i != TRAP else R}">{"⚠️ " if i == TRAP else ""}{i+1:02d}</text>')
    c += doji(x+150, y+60, y+262, k, 70) if i == 4 else kbar(x+122, y+60, y+262, k, 56, faces=False, glow=False)
    c += f'<text x="{x+150}" y="{y+320}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{42 if len(verdict) <= 3 else 36}" fill="{col}">{verdict}</text>'
    short = why if len(why) <= 9 else "漲上去又被賣下來"
    c += f'<text x="{x+150}" y="{y+366}" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="27" fill="{INK}" opacity=".85">{short}</text>'
    return c

def summary_frame(t):
    s = sky(t, None, flash_at(t, [CARD_BEAT, CTA_BEAT]) * 0.8) + chrome()
    s += g(f'<text x="540" y="280" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="80" fill="{GOLD}" stroke="#2a1f55" stroke-width="5" paint-order="stroke">K 棒咒語卡 Ep.2</text>'
           f'<text x="540" y="352" text-anchor="middle" font-family="Noto Serif TC" font-weight="700" font-size="44" fill="{INK}">這根 K 棒是誰贏？5 種一次帶走</text>', 540, 320, pop(t, SUMMARY))
    pos = [(60, 410), (390, 410), (720, 410), (225, 840), (555, 840)]
    for i, (x, y) in enumerate(pos):
        t0 = SUMMARY + 0.12 + i * 0.1
        if t < t0: continue
        p = ease_out((t - t0) / 0.22)
        s += g(card(i, x, y), x+150, y+200, 0.6 + 0.4*back((t - t0) / 0.22), p, dy=(1-p)*-120, rot=(1-p)*-12)
    sv = pop(t, CARD_BEAT - 0.05, 0.25)
    s += g(f'<text x="470" y="1350" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="{INK}">📌 先收藏！<tspan fill="{GOLD}">看盤時對一遍</tspan></text>', 470, 1330, sv)
    if t >= CARD_BEAT:
        ph = (t - CARD_BEAT) % 0.74 / 0.74
        bm = f'<circle cx="960" cy="1330" r="100" fill="url(#glow)"/>'
        bm += "".join(f'<circle cx="960" cy="1330" r="{r + 30*ph:.1f}" fill="none" stroke="{GOLD}" stroke-opacity="{op*(1-ph):.2f}" stroke-width="4"/>' for r, op in ((66,.8),(88,.5)))
        bm += f'<path d="M935,1288 h50 v84 l-25,-20 l-25,20Z" fill="{GOLD}" stroke="#fff3c9" stroke-width="4"/>'
        s += g(bm, 960, 1330, pop(t, CARD_BEAT, 0.25))
    a = ease_out((t - CARD_BEAT - 0.35) / 0.25)
    s += g(f'<line x1="140" y1="1420" x2="940" y2="1420" stroke="{GOLD}" stroke-opacity=".35" stroke-width="2"/>'
           f'<text x="540" y="1510" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="56" fill="{GOLD}">錯幾題？留言告訴我</text>'
           f'<text x="540" y="1590" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="42" fill="{INK}">看不懂？<tspan fill="{GOLD}">3+1 指標</tspan>直接幫你標好</text>', 540, 1540, 1, a, dy=20*(1-a))
    btn = (f'<rect x="220" y="1630" width="640" height="104" rx="52" fill="{GOLD}"/><rect x="220" y="1630" width="640" height="104" rx="52" fill="none" stroke="#fff3c9" stroke-width="4"/>'
           f'<text x="540" y="1698" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="48" fill="{NAVY}">方法放在主頁 Portaly 👆</text>')
    s += g(btn, 540, 1682, pop(t, CARD_BEAT + 0.55, 0.25) * (1 + 0.08 * flash_at(t, [CTA_BEAT], 0.4)))
    return s

def frame(t):
    if t < SUMMARY:
        i = max(j for j in range(5) if START[j] <= t)
        return question_frame(t, i)
    return summary_frame(t)

if __name__ == "__main__":
    n = int(round(DUR * FPS))
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        for k in range(n):
            f.write(json.dumps(frame(k / FPS), ensure_ascii=False) + "\n")
    print(n, "frames")
