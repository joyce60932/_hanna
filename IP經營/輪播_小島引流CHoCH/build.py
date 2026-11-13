"""小島引流輪播：先學會這 1 個就好（CHoCH）。手繪色鉛筆風，6 頁 1080×1350。"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
INK, LINE, SOFT = "#2f2a26", "#5b4636", "#7a6a5c"
SKIN, BLUSH = "#f6dcc6", "#f2a9a0"
H_HAIR, H_TOP, H_IN, JEAN, GOLD = "#b65a2f", "#f0e2c8", "#fbf7ef", "#5f7aa8", "#d4a43a"
C_HAIR, C_SHIRT, TIE = "#2b2a2e", "#a9c7e6", "#2f3f66"
UP, DN, SAGE, WOOD = "#3f9a6e", "#d1584a", "#b9c7a4", "#c99a66"
N = 6
SW = 3  # 線寬

def P(d, fill, stroke=LINE, sw=SW, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'

# ---------------- 人物（半身，(x,y) 為頸部中點） ----------------
def face(x, y, s, mood, who):
    ey = y - 82*s; o = ""
    def eye(cx, look=0):
        return (f'<ellipse cx="{cx}" cy="{ey+look}" rx="{8.5*s}" ry="{11.5*s}" fill="#3a2a22"/>'
                f'<circle cx="{cx+3*s}" cy="{ey+look-4*s}" r="{3*s}" fill="#fff"/>')
    if mood in ("happy", "nod"):
        o += "".join(f'<path d="M{x+k*24*s-10*s},{ey+2*s} q{10*s},{-11*s} {20*s},0" stroke="#3a2a22" stroke-width="{3.6*s}" fill="none" stroke-linecap="round"/>' for k in (-1, 1))
    elif mood == "tired":
        o += "".join(f'<path d="M{x+k*24*s-10*s},{ey} q{10*s},{6*s} {20*s},0" stroke="#3a2a22" stroke-width="{3.4*s}" fill="none" stroke-linecap="round"/>' for k in (-1, 1))
    elif mood == "focus":
        o += eye(x-24*s, 4*s) + eye(x+24*s, 4*s)
    elif mood == "aha":
        o += "".join(f'<ellipse cx="{x+k*24*s}" cy="{ey}" rx="{10*s}" ry="{13.5*s}" fill="#3a2a22"/><circle cx="{x+k*24*s+3*s}" cy="{ey-5*s}" r="{3.6*s}" fill="#fff"/>' for k in (-1, 1))
    else:
        o += eye(x-24*s) + eye(x+24*s)
    by = ey - 22*s
    if mood == "confused":
        o += f'<path d="M{x-36*s},{by+2*s} q12,{-6*s} {24*s},{-2*s}" stroke="#4a3528" stroke-width="{3*s}" fill="none"/><path d="M{x+12*s},{by-6*s} q12,{-4*s} {24*s},{4*s}" stroke="#4a3528" stroke-width="{3*s}" fill="none"/>'
    elif mood == "tired":
        o += f'<path d="M{x-36*s},{by-2*s} l{24*s},{6*s} M{x+12*s},{by+4*s} l{24*s},{-6*s}" stroke="#4a3528" stroke-width="{3*s}" fill="none"/>'
    else:
        o += f'<path d="M{x-36*s},{by} q12,{-5*s} {24*s},0 M{x+12*s},{by} q12,{-5*s} {24*s},0" stroke="#4a3528" stroke-width="{2.8*s}" fill="none"/>'
    my = y - 50*s
    M = {"smile": f'<path d="M{x-10*s},{my} q{10*s},{8*s} {20*s},0" stroke="#8a3b2e" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>',
         "nod": f'<path d="M{x-10*s},{my} q{10*s},{8*s} {20*s},0" stroke="#8a3b2e" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>',
         "happy": f'<path d="M{x-14*s},{my-2*s} q{14*s},{18*s} {28*s},0z" fill="#8a3b2e"/>',
         "aha": f'<ellipse cx="{x}" cy="{my+2*s}" rx="{7*s}" ry="{9*s}" fill="#8a3b2e"/>',
         "confused": f'<path d="M{x-10*s},{my+2*s} q{5*s},{-5*s} {10*s},0 t{10*s},0" stroke="#8a3b2e" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>',
         "tired": f'<path d="M{x-10*s},{my+4*s} q{10*s},{-6*s} {20*s},0" stroke="#8a3b2e" stroke-width="{3*s}" fill="none" stroke-linecap="round"/>',
         "focus": f'<path d="M{x-8*s},{my+2*s} h{16*s}" stroke="#8a3b2e" stroke-width="{3*s}" stroke-linecap="round"/>'}
    o += M.get(mood, M["smile"])
    o += "".join(f'<ellipse cx="{x+k*40*s}" cy="{ey+22*s}" rx="{11*s}" ry="{6*s}" fill="{BLUSH}" opacity=".55"/>' for k in (-1, 1))
    if mood in ("confused", "tired"):
        o += f'<path d="M{x+70*s},{ey-30*s} q{8*s},{14*s} 0,{20*s} q{-8*s},{-6*s} 0,{-20*s}z" fill="#9fd0ea" stroke="{LINE}" stroke-width="2"/>'
    return o

def arm(x0, y0, x1, y1, x2, y2, s, sleeve, cuff=None):
    d = f"M{x0},{y0} Q{x1},{y1} {x2},{y2}"
    return (f'<path d="{d}" stroke="{LINE}" stroke-width="{36*s+SW*2}" fill="none" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="{sleeve}" stroke-width="{36*s}" fill="none" stroke-linecap="round"/>'
            f'<circle cx="{x2}" cy="{y2}" r="{15*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/>')

POSE = {  # (左手肘, 左手, 右手肘, 右手) 相對頸部
    "rest": ((-96, 140), (-62, 215), (96, 140), (62, 215)),
    "phone": ((-92, 150), (-28, 168), (92, 150), (28, 168)),
    "head": ((-128, 10), (-66, -118), (128, 10), (66, -118)),
    "pointR": ((-96, 140), (-62, 215), (160, 95), (240, 70)),
    "pointL": ((-160, 95), (-240, 70), (96, 140), (62, 215)),
    "card": ((-96, 140), (-62, 215), (150, 70), (175, -25)),
    "mug": ((-100, 140), (-30, 125), (96, 140), (62, 215)),
    "cheer": ((-92, 150), (-30, 170), (140, -5), (150, -105)),
    "chin": ((-96, 140), (-62, 215), (92, 120), (30, -28)),
    "watch": ((-70, 140), (40, 105), (90, 135), (-10, 140)),
    "write": ((-90, 150), (-40, 210), (100, 150), (50, 205)),
}

def person(who, x, y, s, mood="smile", pose="rest", front=""):
    sl = H_TOP if who == "h" else C_SHIRT
    o = ""
    if who == "h":  # 長髮在身後
        o += P(f"M{x-80*s},{y-110*s} C{x-110*s},{y-10*s} {x-120*s},{y+120*s} {x-90*s},{y+170*s} L{x+90*s},{y+170*s} C{x+120*s},{y+120*s} {x+110*s},{y-10*s} {x+80*s},{y-110*s}Z", H_HAIR)
    # 身體
    o += P(f"M{x-72*s},{y+30*s} Q{x-80*s},{y+10*s} {x-40*s},{y} L{x+40*s},{y} Q{x+80*s},{y+10*s} {x+72*s},{y+30*s} L{x+78*s},{y+250*s} L{x-78*s},{y+250*s}Z", sl)
    if who == "h":
        o += P(f"M{x-30*s},{y+2*s} L{x},{y+80*s} L{x+30*s},{y+2*s}Z", H_IN, sw=2)
        o += f'<path d="M{x-6*s},{y+90*s} v150 M{x+6*s},{y+90*s} v150" stroke="#d9c7a6" stroke-width="{3*s}"/>'
        o += "".join(f'<path d="M{x+k*50*s},{y+40*s} q{6*s},{20*s} 0,{40*s} q{-6*s},{20*s} 0,{40*s}" stroke="#ddcaa8" stroke-width="{3*s}" fill="none"/>' for k in (-1, 1))
    else:
        o += P(f"M{x-34*s},{y} L{x-8*s},{y+30*s} L{x},{y+8*s} L{x+8*s},{y+30*s} L{x+34*s},{y}Z", "#fff", sw=2)
        o += P(f"M{x-8*s},{y+22*s} l{16*s},0 l{6*s},{70*s} l{-14*s},{14*s} l{-14*s},{-14*s}Z", TIE, sw=2, extra=f'transform="rotate(7 {x} {y})"')
    # 脖子＋頭
    o += P(f"M{x-16*s},{y-30*s} L{x-16*s},{y+6*s} Q{x},{y+16*s} {x+16*s},{y+6*s} L{x+16*s},{y-30*s}Z", SKIN, sw=2)
    hx, hy = x, y - 92*s
    o += f'<ellipse cx="{hx-62*s}" cy="{hy+6*s}" rx="{11*s}" ry="{16*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/><ellipse cx="{hx+62*s}" cy="{hy+6*s}" rx="{11*s}" ry="{16*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/>'
    if who == "h":
        o += f'<circle cx="{hx+64*s}" cy="{hy+28*s}" r="{7*s}" fill="none" stroke="{GOLD}" stroke-width="{4*s}"/>'
    o += P(f"M{hx-60*s},{hy-6*s} C{hx-62*s},{hy+60*s} {hx-28*s},{hy+76*s} {hx},{hy+76*s} C{hx+28*s},{hy+76*s} {hx+62*s},{hy+60*s} {hx+60*s},{hy-6*s} C{hx+58*s},{hy-70*s} {hx-58*s},{hy-70*s} {hx-60*s},{hy-6*s}Z", SKIN)
    if who == "h":
        o += P(f"M{hx-66*s},{hy+20*s} C{hx-80*s},{hy-70*s} {hx-30*s},{hy-92*s} {hx+6*s},{hy-90*s} C{hx+60*s},{hy-88*s} {hx+84*s},{hy-50*s} {hx+66*s},{hy+24*s} "
               f"C{hx+52*s},{hy-20*s} {hx+40*s},{hy-34*s} {hx+30*s},{hy-30*s} L{hx+18*s},{hy-14*s} L{hx+6*s},{hy-32*s} L{hx-8*s},{hy-12*s} L{hx-22*s},{hy-32*s} L{hx-36*s},{hy-14*s} L{hx-44*s},{hy-34*s} C{hx-56*s},{hy-20*s} {hx-60*s},{hy}  {hx-66*s},{hy+20*s}Z", H_HAIR)
    else:
        o += P(f"M{hx-64*s},{hy+4*s} C{hx-74*s},{hy-70*s} {hx-10*s},{hy-96*s} {hx+40*s},{hy-80*s} L{hx+52*s},{hy-92*s} L{hx+56*s},{hy-70*s} C{hx+72*s},{hy-52*s} {hx+70*s},{hy-20*s} {hx+64*s},{hy+4*s} "
               f"L{hx+50*s},{hy-24*s} L{hx+34*s},{hy-12*s} L{hx+22*s},{hy-36*s} L{hx+4*s},{hy-18*s} L{hx-12*s},{hy-38*s} L{hx-28*s},{hy-16*s} L{hx-44*s},{hy-34*s} L{hx-52*s},{hy-10*s}Z", C_HAIR)
    o += face(x, y, s, mood, who)
    le, lh, re, rh = POSE[pose]
    L = arm(x-70*s, y+38*s, x+le[0]*s, y+le[1]*s, x+lh[0]*s, y+lh[1]*s, s, sl)
    R = arm(x+70*s, y+38*s, x+re[0]*s, y+re[1]*s, x+rh[0]*s, y+rh[1]*s, s, sl)
    if pose == "phone":
        o += L + R + f'<rect x="{x-34*s}" y="{y+110*s}" width="{68*s}" height="{100*s}" rx="{10*s}" fill="#3a3a40" stroke="{LINE}" stroke-width="{SW}"/><rect x="{x-27*s}" y="{y+118*s}" width="{54*s}" height="{82*s}" rx="6" fill="#dbe9f2"/>'
        o += f'<circle cx="{x-30*s}" cy="{y+168*s}" r="{15*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/><circle cx="{x+30*s}" cy="{y+168*s}" r="{15*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/>'
    elif pose == "cheer":
        o += f'<rect x="{x-60*s}" y="{y+140*s}" width="{60*s}" height="{90*s}" rx="{10*s}" fill="#3a3a40" stroke="{LINE}" stroke-width="{SW}" transform="rotate(-12 {x-30*s} {y+185*s})"/>' + L + R
    else:
        o += L + R
    if pose == "card":
        cx, cy = x + 175*s, y - 25*s
        o += f'<rect x="{cx-10*s}" y="{cy-110*s}" width="{90*s}" height="{120*s}" rx="{8*s}" fill="#fffaf0" stroke="{LINE}" stroke-width="{SW}" transform="rotate(8 {cx} {cy})"/>'
        o += f'<g transform="rotate(8 {cx} {cy})"><line x1="{cx+35*s}" y1="{cy-90*s}" x2="{cx+35*s}" y2="{cy-20*s}" stroke="{UP}" stroke-width="{4*s}"/><rect x="{cx+25*s}" y="{cy-75*s}" width="{20*s}" height="{40*s}" fill="{UP}"/></g>'
        o += f'<circle cx="{cx}" cy="{cy}" r="{15*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/>'
    if pose == "mug":
        mx, my = x - 30*s, y + 125*s
        o += P(f"M{mx-26*s},{my-30*s} h{52*s} v{50*s} q0,{14*s} {-14*s},{14*s} h{-24*s} q{-14*s},0 {-14*s},{-14*s}Z", "#fbf7ef")
        o += f'<path d="M{mx-6*s},{my-12*s} q{10*s},{-10*s} {6*s},{6*s}" stroke="#8da86c" stroke-width="{3*s}" fill="none"/>'
        o += f'<circle cx="{mx}" cy="{my+8*s}" r="{14*s}" fill="{SKIN}" stroke="{LINE}" stroke-width="{SW}"/>'
    if pose == "watch":
        o += f'<rect x="{x+22*s}" y="{y+94*s}" width="{22*s}" height="{20*s}" rx="4" fill="#e9eef2" stroke="{LINE}" stroke-width="{SW}"/>'
    if pose == "write":
        o += f'<line x1="{x+46*s}" y1="{y+205*s}" x2="{x+80*s}" y2="{y+160*s}" stroke="#6a4b2e" stroke-width="{6*s}" stroke-linecap="round"/>'
    return o + front

# ---------------- 場景元件 ----------------
def room(w, h, plant=True, shelf=True):
    o = f'<rect width="{w}" height="{h}" fill="#f3ead9"/><rect y="{h*.72}" width="{w}" height="{h*.28}" fill="#e8d8bd"/>'
    if shelf:
        o += P(f"M{w*.05},{h*.08} h{w*.24} v{h*.5} h{-w*.24}Z", "#e3c9a0")
        for k in range(3):
            yy = h*.08 + (k+1)*h*.16
            o += f'<line x1="{w*.05}" y1="{yy}" x2="{w*.29}" y2="{yy}" stroke="{LINE}" stroke-width="{SW}"/>'
            cols = ["#8aa3c4", "#d9a35a", "#a7b98a", "#c97a62", "#e7d7b0"]
            for j in range(5):
                bx = w*.065 + j*w*.042
                o += P(f"M{bx},{yy-4} v{-h*.1+j*4} h{w*.032} v{h*.1-j*4}Z", cols[(j+k) % 5], sw=2)
    if plant:
        px = w*.9
        o += P(f"M{px-30},{h*.66} h60 l-8,{h*.06} h-44Z", "#d7b08a")
        for a, b in ((-60, -120), (-20, -150), (30, -140), (60, -100), (0, -90)):
            o += P(f"M{px},{h*.66} Q{px+a*.4},{h*.66+b*.6} {px+a},{h*.66+b} Q{px+a*.6},{h*.66+b*.4} {px},{h*.66}Z", "#9cb67e", sw=2)
    return o

def sofa(x, y, w):
    return (P(f"M{x-w/2},{y-200} q0,-30 30,-30 h{w-60} q30,0 30,30 v200 h{-w}Z", SAGE) +
            P(f"M{x-w/2-30},{y-90} q0,-24 24,-24 h30 v200 h-54Z", "#a9b993") + P(f"M{x+w/2+30},{y-90} q0,-24 -24,-24 h-30 v200 h54Z", "#a9b993") +
            P(f"M{x-w/2+10},{y-10} h{w-20} v70 h{-w+20}Z", "#c5d1b1") +
            P(f"M{x-w/2+40},{y-170} q50,-20 110,0 v70 q-55,15 -110,0Z", "#f1dcc9") + P(f"M{x+w/2-150},{y-170} q50,-20 110,0 v70 q-55,15 -110,0Z", "#efe3c9"))

def table(x, y, w):
    return P(f"M{x-w/2},{y} h{w} l-10,24 h{-w+20}Z", WOOD) + P(f"M{x-w/2+30},{y+24} v80 h16 v-80Z M{x+w/2-46},{y+24} v80 h16 v-80Z", "#b2834f")

def tablet(x, y, w=170, h=110, blank=True):
    return P(f"M{x},{y} h{w} v{h} h{-w}Z", "#3a3a40") + f'<rect x="{x+8}" y="{y+8}" width="{w-16}" height="{h-16}" rx="4" fill="#e3ecef"/>'

def swirl(x, y, r):
    return f'<path d="M{x},{y} m-{r},0 a{r},{r} 0 1,1 {2*r},0 a{r*.66},{r*.66} 0 1,1 -{r*1.32},0 a{r*.33},{r*.33} 0 1,1 {r*.66},0" stroke="{LINE}" stroke-width="3" fill="none"/>'

def fox_plush(x, y, s=1):
    o = P(f"M{x+30*s},{y+20*s} q{60*s},{-10*s} {50*s},{-70*s} q{-30*s},{30*s} {-60*s},{40*s}Z", "#e8823c")
    o += P(f"M{x-40*s},{y+30*s} q0,{-60*s} {40*s},{-60*s} q{40*s},0 {40*s},{60*s}Z", "#e8823c")
    for k in (-1, 1):
        o += P(f"M{x+k*20*s},{y-60*s} l{k*14*s},{-40*s} l{k*14*s},{40*s}Z", "#e8823c")
    o += P(f"M{x-34*s},{y-40*s} q0,{-40*s} {34*s},{-40*s} q{34*s},0 {34*s},{40*s} q0,{30*s} {-34*s},{30*s} q{-34*s},0 {-34*s},{-30*s}Z", "#e8823c")
    o += P(f"M{x-24*s},{y-30*s} q{24*s},{30*s} {48*s},0 q{-10*s},{24*s} {-24*s},{24*s} q{-14*s},0 {-24*s},{-24*s}Z", "#fff3e2", sw=2)
    o += f'<path d="M{x-16*s},{y-46*s} q6,-6 12,0 M{x+4*s},{y-46*s} q6,-6 12,0" stroke="{INK}" stroke-width="3" fill="none"/><circle cx="{x}" cy="{y-30*s}" r="{4*s}" fill="{INK}"/>'
    return o

def thumbs(pts):
    o = ""
    for x, y, r in pts:
        o += f'<g transform="rotate({r} {x} {y})">' + P(f"M{x-55},{y-34} h110 v68 h-110Z", "#4a5578") + f'<path d="M{x-10},{y-14} l24,14 l-24,14z" fill="#fff"/></g>'
    return o

def notes(pts):
    cols = ["#f7d974", "#f3a6a0", "#a9d0e8", "#bfe0a6"]
    return "".join(f'<g transform="rotate({r} {x} {y})">' + P(f"M{x-34},{y-34} h68 v68 h-68Z", cols[i % 4], sw=2) +
                   f'<path d="M{x-20},{y-12} h40 M{x-20},{y+4} h30" stroke="{LINE}" stroke-width="2"/></g>' for i, (x, y, r) in enumerate(pts))

# ---------------- K 線示意圖 ----------------
CANDLES = [(100, 95, 101, 94), (95, 92, 96, 90), (92, 95, 96, 91), (95, 97, 98, 94), (97, 92, 97.5, 91),
           (92, 88, 93, 87), (88, 90, 91, 86), (90, 94, 95, 89), (94, 100, 101, 93), (100, 99, 101.5, 98)]

def chart(x, y, w, h, flip=False):
    data = [(200-o, 200-c, 200-l, 200-hh) if flip else (o, c, hh, l) for o, c, hh, l in CANDLES]
    lo = min(d[3] for d in data) - 2; hi = max(d[2] for d in data) + 2
    Y = lambda v: y + h - (v - lo) / (hi - lo) * h
    step = w / len(data); cw = step * .5
    o = P(f"M{x-20},{y-30} h{w+40} v{h+60} h{-w-40}Z", "#fffaf0", sw=2)
    for i, (op, cl, hh, ll) in enumerate(data):
        cx = x + step*i + step/2
        col = UP if cl > op else DN
        o += f'<line x1="{cx}" y1="{Y(hh)}" x2="{cx}" y2="{Y(ll)}" stroke="{col}" stroke-width="4" stroke-linecap="round"/>'
        o += P(f"M{cx-cw/2},{Y(max(op, cl))} h{cw} v{max(Y(min(op, cl))-Y(max(op, cl)), 4)} h{-cw}Z", col, stroke=col, sw=2)
    lvl = data[3][2] if not flip else data[3][3]
    ly = Y(lvl); x0 = x + step*3 + step/2; x1 = x + step*8 + step/2 + 30
    col = UP if not flip else DN
    o += f'<line x1="{x0}" y1="{ly}" x2="{x1}" y2="{ly}" stroke="{col}" stroke-width="4" stroke-dasharray="12 9"/>'
    lab = "前高" if not flip else "前低"
    o += f'<text x="{x0-6}" y="{ly + (-18 if not flip else 44)}" font-family="LXGW WenKai TC" font-weight="700" font-size="34" fill="{col}" text-anchor="middle">{lab}</text>'
    bx = x + step*8 + step/2
    by = Y(data[8][1])
    o += f'<circle cx="{bx}" cy="{by}" r="30" fill="none" stroke="{col}" stroke-width="5"/>'
    o += f'<text x="{bx-10}" y="{by + (-48 if not flip else 76)}" font-family="LXGW WenKai TC" font-weight="700" font-size="38" fill="{col}" text-anchor="middle">CHoCH</text>'
    return o

# ---------------- 頁面 ----------------
DEFS = """<defs>
<filter id="pencil" x="-5%" y="-5%" width="110%" height="110%">
 <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="4" result="n"/>
 <feDisplacementMap in="SourceGraphic" in2="n" scale="3.5" xChannelSelector="R" yChannelSelector="G" result="d"/>
 <feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="7" result="g"/>
 <feColorMatrix in="g" type="saturate" values="0" result="gg"/>
 <feComposite in="d" in2="gg" operator="arithmetic" k1="0" k2="1" k3="-0.10" k4="0.02" result="t"/>
 <feComposite in="t" in2="d" operator="in"/>
</filter>
<filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" seed="2" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="26"/></filter>
<filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="9"/><feColorMatrix type="matrix" values="0 0 0 0 0.45  0 0 0 0 0.38  0 0 0 0 0.3  0 0 0 0.10 0"/></filter>
</defs>"""

def vignette(x, y, w, h, inner, mid):
    return (f'<mask id="m{mid}"><rect x="{x+14}" y="{y+14}" width="{w-28}" height="{h-28}" rx="30" fill="#fff" filter="url(#rough)"/></mask>'
            f'<g mask="url(#m{mid})"><g transform="translate({x} {y})"><g filter="url(#pencil)">{inner}</g></g></g>')

CSS = f"""*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#999}}
.slide{{width:1080px;height:1350px;background:#f6efe1;position:relative;overflow:hidden;margin:0 0 20px;font-family:"LXGW WenKai TC",serif;color:{INK}}}
.slide svg{{position:absolute;inset:0}}"""

def T(x, y, s, size, w=700, anchor="middle", fill=INK):
    return f'<text x="{x}" y="{y}" font-family="LXGW WenKai TC" font-weight="{w}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

def pill(x, y, w, text, col):
    return (f'<path d="M{x-w/2},{y-38} h{w} q16,38 0,76 h{-w} q-16,-38 0,-76Z" fill="{col}" opacity=".75" filter="url(#rough)"/>' + T(x, y+16, text, 46))

def frame(i, body):
    return (f'<section class="slide"><svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">{DEFS}'
            f'<rect width="1080" height="1350" fill="#f6efe1"/>{body}'
            f'<rect width="1080" height="1350" filter="url(#paper)"/>'
            + T(70, 1300, "@_hannapang", 32, 400, "start") + T(1010, 1300, f"{i:02d} / {N:02d}", 32, 400, "end") + '</svg></section>')

PAGES = []
# 01 封面
sc = room(960, 860) + sofa(500, 760, 660)
sc += person("c", 370, 470, 1.25, "confused", "phone") + person("h", 640, 470, 1.18, "smile", "rest")
sc += swirl(250, 250, 22) + swirl(470, 200, 18) + swirl(180, 360, 14)
sc += f'<text x="225" y="300" font-family="LXGW WenKai TC" font-weight="700" font-size="70" fill="{LINE}">?</text><text x="520" y="250" font-family="LXGW WenKai TC" font-weight="700" font-size="56" fill="{LINE}">?</text>'
PAGES.append(frame(1, T(540, 150, "看了 30 支 K 線影片", 92) + T(540, 262, "還是看不懂？", 92) + vignette(60, 320, 960, 860, sc, 1)
                   + T(540, 1238, "先別學 30 個，先學會這 1 個就好", 46, 700, "middle", "#a8763e")))
# 02 對照
left = room(460, 470, plant=False) + thumbs([(90, 120, -12), (380, 110, 10), (70, 300, 8), (390, 300, -8), (230, 70, 4)]) + notes([(150, 210, -10), (330, 220, 12), (110, 390, 6), (360, 400, -6)])
left += person("c", 230, 300, .78, "tired", "head")
right = room(460, 470, shelf=False) + person("h", 130, 300, .78, "smile", "card") + person("c", 385, 300, .78, "nod", "rest")
body = T(540, 140, "不是你不努力", 84) + T(540, 245, "是一次學太多", 84)
body += pill(290, 340, 360, "一次學 30 個", "#f4b9b2") + pill(790, 340, 300, "先學 1 個", "#b9cfe8")
body += f'<line x1="540" y1="310" x2="540" y2="1100" stroke="#bda98c" stroke-width="2"/>'
body += vignette(60, 400, 460, 470, left, 2) + vignette(560, 400, 460, 470, right, 3)
for k, (a, b) in enumerate((("影片一支接一支", "只看一件事"), ("名詞越背越多", "看懂了，再加下一個"), ("打開盤面還是不知道看哪", "打開盤面，知道先找什麼"))):
    body += T(290, 940 + k*58, a, 38, 400) + T(790, 940 + k*58, b, 38, 400)
body += T(540, 1180, "先學會：方向什麼時候「轉」", 56)
PAGES.append(frame(2, body))
# 03 綠色 CHoCH
sc = room(960, 470) + table(480, 400, 520) + tablet(400, 290) + person("h", 270, 240, .9, "smile", "pointR") + person("c", 680, 250, .9, "aha", "rest")
body = T(540, 140, "一路創新低", 80) + T(540, 240, "突然站上前一個高點", 80, 700, "middle", UP)
body += f'<g filter="url(#pencil)">{chart(140, 330, 800, 300)}</g>'
body += T(540, 730, "這叫綠色 CHoCH：結構「可能」開始往上轉", 42, 700)
body += vignette(60, 760, 960, 420, sc, 4)
body += T(540, 1238, "重點是「收盤」站上，不是影線碰到", 44, 700, "middle", "#a8763e")
PAGES.append(frame(3, body))
# 04 紅色 CHoCH
sc = room(960, 470) + table(480, 400, 520) + tablet(400, 290) + person("c", 270, 240, .9, "smile", "pointR") + person("h", 680, 250, .9, "nod", "mug")
body = T(540, 140, "一路創新高", 80) + T(540, 240, "突然跌破前一個低點", 80, 700, "middle", DN)
body += f'<g filter="url(#pencil)">{chart(140, 330, 800, 300, flip=True)}</g>'
body += T(540, 730, "這叫紅色 CHoCH：結構「可能」開始往下轉", 42, 700)
body += vignette(60, 760, 960, 420, sc, 5)
body += T(540, 1238, "一根 K 棒不算數，等下一根確認", 44, 700, "middle", "#a8763e")
PAGES.append(frame(4, body))
# 05 小抄
v1 = room(470, 300, plant=False, shelf=False) + table(250, 250, 360) + P("M170,150 h170 v100 h-170Z", "#3a3a40") + '<rect x="178" y="158" width="154" height="84" fill="#e3ecef"/>' + "".join(f'<rect x="{196+k*26}" y="{180+(k%3)*10}" width="12" height="{40-(k%2)*12}" fill="{UP if k%2 else DN}"/>' for k in range(5)) + person("c", 110, 150, .55, "focus", "rest")
v2 = room(470, 300, plant=False, shelf=False) + person("c", 230, 140, .6, "focus", "watch")
v3 = room(470, 300, shelf=False) + table(230, 240, 380) + P("M200,212 l110,-6 l6,30 l-110,6Z", "#fffaf0", sw=2) + person("c", 230, 120, .55, "focus", "write")
body = T(540, 140, "看到 CHoCH", 84) + T(540, 245, "先做這 3 件事", 84)
items = (("① 確認收盤突破", "不是影線碰到就算"), ("② 等下一根確認", "不要急著追進去"), ("③ 先想好停損", "放哪裡，再決定進不進"))
for k, ((h, sub), v) in enumerate(zip(items, (v1, v2, v3))):
    yy = 300 + k*300
    if k % 2 == 0:
        body += T(80, yy+130, h, 52, 700, "start") + T(80, yy+195, sub, 38, 400, "start", SOFT) + vignette(540, yy, 480, 300, v, 6+k)
    else:
        body += vignette(60, yy, 480, 300, v, 6+k) + T(580, yy+130, h, 52, 700, "start") + T(580, yy+195, sub, 38, 400, "start", SOFT)
body += T(540, 1238, "📌 先收藏，看盤時對一遍", 52, 700, "middle", "#a8763e")
PAGES.append(frame(5, body))
# 06 導流
sc = room(560, 640, shelf=False) + sofa(290, 560, 420) + person("h", 175, 330, .82, "happy", "rest") + person("c", 390, 330, .82, "happy", "cheer") + fox_plush(510, 470, .7)
body = T(540, 140, "學完，馬上練一次", 84) + T(540, 230, "小島 Day 1 就考這題", 56, 700, "middle", "#a8763e")
body += P("M80,300 h360 v720 h-360Z", "#3a3a40") + '<clipPath id="ph"><rect x="96" y="316" width="328" height="688" rx="18"/></clipPath><image href="quiz.png" x="96" y="316" width="328" height="688" preserveAspectRatio="xMidYMax slice" clip-path="url(#ph)"/>'
body += vignette(460, 300, 560, 640, sc, 9)
body += T(740, 990, "看圖選答案", 42, 700) + T(740, 1045, "答錯也會告訴你為什麼", 42, 700)
body += f'<rect x="100" y="1110" width="880" height="96" rx="48" fill="#3f6f4e"/>' + T(540, 1172, "主頁連結 → 加 LINE@ → 回覆「小島」", 42, 700, "middle", "#fff")
body += T(540, 1250, "僅供教學參考，非投資建議", 28, 400, "middle", SOFT)
PAGES.append(frame(6, body))

html = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=LXGW+WenKai+TC:wght@400;700&display=block" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>' + "\n".join(PAGES) + '<script>document.fonts.ready.then(()=>setTimeout(()=>{document.body.dataset.ready="1"},400))</script></body></html>')
open(os.path.join(HERE, "slides.html"), "w", encoding="utf-8").write(html)
print(len(PAGES))
