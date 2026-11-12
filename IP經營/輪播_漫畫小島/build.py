"""漫畫輪播：阿明 × 小狐狸（扁平風）。8 頁，1080×1350。"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
INK, SOFT, ACC, BG = "#2a2622", "#7a7066", "#a8763e", "#f4efe6"
SKIN, HAIR, SHIRT, TIE, PANTS = "#f3d3b5", "#2b2a33", "#9cc3e6", "#2d3e66", "#4a4f5c"
FOX, FOXD, CREAM, PINK = "#f08a3c", "#c9662a", "#fff3e2", "#ff8e9e"
N = 8

# ---------- 角色 ----------
def face_aming(x, y, mood):
    s = ""
    if mood == "determined":
        s += f'<path d="M{x-44},{y-22} l26,8 M{x+44},{y-22} l-26,8" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>'
        s += f'<circle cx="{x-28}" cy="{y}" r="7" fill="{INK}"/><circle cx="{x+28}" cy="{y}" r="7" fill="{INK}"/>'
        s += f'<path d="M{x-14},{y+30} h28" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
    elif mood == "sleep":
        s += f'<path d="M{x-40},{y} q12,10 24,0 M{x+16},{y} q12,10 24,0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
        s += f'<ellipse cx="{x+4}" cy="{y+30}" rx="10" ry="7" fill="{INK}"/>'
        s += f'<path d="M{x+12},{y+34} q6,22 0,34 q-8,-8 0,-34z" fill="#9fd6f2"/>'
    elif mood == "dizzy":
        for k in (-1, 1):
            cx = x + k*28
            s += f'<path d="M{cx},{y} m-12,0 a12,12 0 1,1 24,0 a8,8 0 1,1 -16,0 a4,4 0 1,1 8,0" stroke="{INK}" stroke-width="4" fill="none"/>'
        s += f'<path d="M{x-18},{y+32} q6,-8 12,0 t12,0 t12,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    elif mood == "shine":
        for k in (-1, 1):
            cx = x + k*28
            s += f'<circle cx="{cx}" cy="{y}" r="15" fill="{INK}"/><circle cx="{cx+5}" cy="{y-6}" r="6" fill="#fff"/><circle cx="{cx-5}" cy="{y+6}" r="3" fill="#fff"/>'
        s += f'<path d="M{x-18},{y+26} q18,24 36,0z" fill="{INK}"/><path d="M{x-9},{y+34} q9,8 18,0" fill="{PINK}"/>'
    else:  # confused
        s += f'<circle cx="{x-28}" cy="{y}" r="7" fill="{INK}"/><circle cx="{x+28}" cy="{y}" r="7" fill="{INK}"/>'
        s += f'<path d="M{x-44},{y-24} l24,-6 M{x+20},{y-30} l24,6" stroke="{HAIR}" stroke-width="6" stroke-linecap="round"/>'
        s += f'<path d="M{x-12},{y+32} q12,-10 24,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    s += f'<ellipse cx="{x-44}" cy="{y+18}" rx="12" ry="7" fill="#f4a6a0" opacity=".6"/><ellipse cx="{x+44}" cy="{y+18}" rx="12" ry="7" fill="#f4a6a0" opacity=".6"/>'
    return s

def head(x, y, mood, tilt=0):
    s = f'<g transform="rotate({tilt} {x} {y+60})">'
    s += f'<circle cx="{x-76}" cy="{y+6}" r="16" fill="{SKIN}"/><circle cx="{x+76}" cy="{y+6}" r="16" fill="{SKIN}"/>'
    s += f'<ellipse cx="{x}" cy="{y}" rx="78" ry="84" fill="{SKIN}"/>'
    s += f'<path d="M{x-82},{y-4} C{x-90},{y-90} {x+70},{y-118} {x+84},{y-10} C{x+60},{y-48} {x+10},{y-40} {x-20},{y-60} C{x-30},{y-30} {x-60},{y-36} {x-82},{y-4}z" fill="{HAIR}"/>'
    s += face_aming(x, y+10, mood) + '</g>'
    return s

def torso(x, top, bot):
    s = f'<path d="M{x-92},{bot} L{x-88},{top+40} Q{x-86},{top} {x-40},{top} L{x+40},{top} Q{x+86},{top} {x+88},{top+40} L{x+92},{bot}z" fill="{SHIRT}"/>'
    s += f'<path d="M{x-34},{top} L{x},{top+40} L{x+34},{top}" fill="#fff"/>'
    s += f'<path d="M{x-6},{top+34} l14,0 l10,86 l-14,16 l-14,-18z" fill="{TIE}" transform="rotate(8 {x} {top+40})"/>'
    return s

def aming(x, hip, mood="confused", arms="phone", stand=False, tilt=0, glow=False):
    top = hip - 230
    s = ""
    if stand:
        s += f'<rect x="{x-80}" y="{hip-10}" width="70" height="240" rx="24" fill="{PANTS}"/><rect x="{x+10}" y="{hip-10}" width="70" height="240" rx="24" fill="{PANTS}"/>'
        s += f'<ellipse cx="{x-48}" cy="{hip+232}" rx="46" ry="18" fill="{INK}"/><ellipse cx="{x+48}" cy="{hip+232}" rx="46" ry="18" fill="{INK}"/>'
    else:
        s += f'<rect x="{x-96}" y="{hip-20}" width="192" height="70" rx="30" fill="{PANTS}"/>'
        s += f'<rect x="{x-86}" y="{hip+20}" width="64" height="150" rx="24" fill="{PANTS}"/><rect x="{x+22}" y="{hip+20}" width="64" height="150" rx="24" fill="{PANTS}"/>'
        s += f'<ellipse cx="{x-56}" cy="{hip+170}" rx="44" ry="17" fill="{INK}"/><ellipse cx="{x+56}" cy="{hip+170}" rx="44" ry="17" fill="{INK}"/>'
    s += torso(x, top, hip + 10)
    if arms == "phone":
        s += f'<path d="M{x-86},{top+50} Q{x-120},{top+150} {x-36},{top+150}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/>'
        s += f'<path d="M{x+86},{top+50} Q{x+120},{top+150} {x+36},{top+150}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/>'
        s += f'<rect x="{x-40}" y="{top+80}" width="80" height="130" rx="14" fill="{INK}"/><rect x="{x-32}" y="{top+90}" width="64" height="108" rx="8" fill="#cfe8ff"/>'
        s += f'<circle cx="{x-34}" cy="{top+150}" r="18" fill="{SKIN}"/><circle cx="{x+34}" cy="{top+150}" r="18" fill="{SKIN}"/>'
    elif arms == "fist":
        s += f'<path d="M{x-86},{top+50} Q{x-120},{top+150} {x-110},{top+220}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/><circle cx="{x-110}" cy="{top+230}" r="20" fill="{SKIN}"/>'
        s += f'<path d="M{x+86},{top+50} Q{x+150},{top-10} {x+150},{top-90}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/><circle cx="{x+150}" cy="{top-108}" r="28" fill="{SKIN}"/>'
        s += f'<path d="M{x+132},{top-118} h30 M{x+132},{top-104} h30" stroke="#d9a989" stroke-width="4"/>'
    elif arms == "lap":
        s += f'<path d="M{x-86},{top+50} Q{x-112},{top+170} {x-60},{top+220}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/>'
        s += f'<path d="M{x+86},{top+50} Q{x+112},{top+170} {x+60},{top+220}" stroke="{SHIRT}" stroke-width="40" fill="none" stroke-linecap="round"/>'
        s += f'<rect x="{x-46}" y="{top+200}" width="92" height="56" rx="12" fill="{INK}" transform="rotate(-8 {x} {top+228})"/>'
    s += head(x, top - 92, mood, tilt)
    return s

def fox(x, y, s=1.0, pose="cheeks"):
    S = lambda v: v * s
    o = f'<g transform="translate({x} {y}) scale({s}) translate({-x} {-y})">'
    o += f'<path d="M{x+60},{y+40} C{x+200},{y+10} {x+210},{y-140} {x+120},{y-160} C{x+170},{y-90} {x+130},{y-10} {x+50},{y-10}z" fill="{FOX}"/>'
    o += f'<path d="M{x+120},{y-160} C{x+160},{y-150} {x+180},{y-110} {x+168},{y-80} C{x+150},{y-110} {x+130},{y-130} {x+120},{y-160}z" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x}" cy="{y}" rx="78" ry="88" fill="{FOX}"/><ellipse cx="{x}" cy="{y+18}" rx="48" ry="62" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x-40}" cy="{y+84}" rx="30" ry="16" fill="{FOXD}"/><ellipse cx="{x+40}" cy="{y+84}" rx="30" ry="16" fill="{FOXD}"/>'
    hy = y - 150
    for k in (-1, 1):
        o += f'<path d="M{x+k*30},{hy-60} L{x+k*92},{hy-150} L{x+k*100},{hy-30}z" fill="{FOX}"/>'
        o += f'<path d="M{x+k*44},{hy-62} L{x+k*86},{hy-124} L{x+k*90},{hy-44}z" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x}" cy="{hy}" rx="118" ry="102" fill="{FOX}"/>'
    o += f'<path d="M{x-104},{hy+20} C{x-80},{hy+110} {x+80},{hy+110} {x+104},{hy+20} C{x+60},{hy+46} {x+20},{hy+10} {x},{hy+30} C{x-20},{hy+10} {x-60},{hy+46} {x-104},{hy+20}z" fill="{CREAM}"/>'
    for k in (-1, 1):
        o += f'<path d="M{x+k*48-18},{hy-4} q18,-22 36,0" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        o += f'<ellipse cx="{x+k*72}" cy="{hy+30}" rx="18" ry="11" fill="{PINK}" opacity=".7"/>'
    o += f'<ellipse cx="{x}" cy="{hy+22}" rx="13" ry="9" fill="{INK}"/>'
    o += f'<path d="M{x-24},{hy+40} q24,36 48,0z" fill="#8a2f3a"/><path d="M{x-12},{hy+56} q12,10 24,0" fill="{PINK}"/>'
    if pose == "cheeks":
        o += f'<ellipse cx="{x-76}" cy="{hy+50}" rx="26" ry="32" fill="{FOX}"/><ellipse cx="{x+76}" cy="{hy+50}" rx="26" ry="32" fill="{FOX}"/>'
    elif pose == "wave":
        o += f'<path d="M{x+66},{y-40} Q{x+140},{y-80} {x+150},{y-170}" stroke="{FOX}" stroke-width="40" fill="none" stroke-linecap="round"/><circle cx="{x+152}" cy="{y-182}" r="26" fill="{CREAM}"/>'
        o += f'<path d="M{x+190},{y-200} q14,-10 10,-28 M{x+196},{y-170} q18,-2 22,-18" stroke="{ACC}" stroke-width="5" fill="none" stroke-linecap="round"/>'
        o += f'<ellipse cx="{x-70}" cy="{y-20}" rx="22" ry="30" fill="{FOX}"/>'
    elif pose == "peek":
        o += f'<ellipse cx="{x-96}" cy="{hy+86}" rx="30" ry="22" fill="{FOX}"/><ellipse cx="{x+96}" cy="{hy+86}" rx="30" ry="22" fill="{FOX}"/>'
    return o + '</g>'

def sofa(x, y, w=620):
    return (f'<rect x="{x-w/2}" y="{y-250}" width="{w}" height="260" rx="40" fill="#d9c7ab"/>'
            f'<rect x="{x-w/2-40}" y="{y-60}" width="90" height="190" rx="36" fill="#cbb594"/><rect x="{x+w/2-50}" y="{y-60}" width="90" height="190" rx="36" fill="#cbb594"/>'
            f'<rect x="{x-w/2+20}" y="{y-6}" width="{w-40}" height="110" rx="30" fill="#e6d6bd"/>')

def room(night=0.0):
    wall = ["#efe3cf", "#ded3c2", "#cdc6bd"][min(2, int(night * 3))]
    return (f'<rect width="920" height="980" fill="{wall}"/><rect y="760" width="920" height="220" fill="#d8c5a6"/>'
            f'<rect x="640" y="90" width="200" height="230" rx="10" fill="{"#2c3354" if night > .3 else "#bcd8ea"}"/><path d="M740,90 v230 M640,205 h200" stroke="#f5ecdc" stroke-width="10"/>'
            + (f'<circle cx="790" cy="140" r="22" fill="#fff3c9"/><circle cx="800" cy="134" r="20" fill="#2c3354"/>' if night > .3 else ""))

def qmarks(pts):
    return "".join(f'<text x="{x}" y="{y}" font-family="Noto Serif TC" font-weight="900" font-size="{sz}" fill="{ACC}" transform="rotate({r} {x} {y})">?</text>' for x, y, sz, r in pts)

# ---------- 頁面 ----------
CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#999;font-family:"Noto Sans TC",sans-serif;color:{INK}}}
.slide{{width:1080px;height:1350px;background:{BG};position:relative;overflow:hidden;margin:0 0 20px}}
.top{{position:absolute;top:58px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:26px;letter-spacing:.14em;color:{SOFT}}}
.foot{{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:flex-end;font-size:26px;color:{SOFT};letter-spacing:.08em}}
.sign{{font-family:"Mrs Saint Delafield",cursive;font-size:80px;color:{ACC};line-height:.6}}
.panel{{position:absolute;top:130px;left:80px;width:920px;height:980px;border:5px solid {INK};border-radius:28px;overflow:hidden;background:#fff}}
.panel svg{{display:block}}
.cap{{position:absolute;top:24px;left:24px;background:{INK};color:{BG};font-family:"Noto Serif TC",serif;font-weight:900;font-size:34px;padding:8px 22px;border-radius:6px}}
.bub{{position:absolute;background:#fff;border:5px solid {INK};border-radius:40px;padding:26px 34px;font-family:"Noto Serif TC",serif;font-weight:900;font-size:44px;line-height:1.45}}
.bub::after{{content:"";position:absolute;width:34px;height:34px;background:#fff;border-right:5px solid {INK};border-bottom:5px solid {INK}}}
.bub.dl::after{{left:70px;bottom:-21px;transform:rotate(45deg)}}
.bub.dr::after{{right:70px;bottom:-21px;transform:rotate(45deg)}}
.bub.ur::after{{right:80px;top:-21px;transform:rotate(225deg)}}
.bub.fox{{border-color:{FOXD}}} .bub.fox::after{{border-color:{FOXD}}}
.under{{position:absolute;left:80px;right:80px;top:1130px;font-family:"Noto Serif TC",serif;font-weight:900;font-size:40px;line-height:1.4;text-align:center}}
.hl{{background:#ffe066;padding:0 10px;border-radius:6px}}
.acc{{color:{ACC}}}
"""

def page(i, svg, overlay="", under=""):
    return (f'<section class="slide"><div class="top"><span>BISANCOS・Hanna｜阿明的 K 線日記</span><span>{i:02d} / {N:02d}</span></div>'
            f'<div class="panel"><svg width="920" height="980" viewBox="0 0 920 980" xmlns="http://www.w3.org/2000/svg">{svg}</svg>{overlay}</div>'
            f'<div class="under">{under}</div>'
            f'<div class="foot"><span>Hanna｜教路人會交易的教官</span><span class="sign">Hanna</span></div></section>')

P = []
# 01 封面
svg = room(.6).split('<rect x="640" y="90"')[0] + sofa(460, 760) + aming(460, 760, "confused", "phone")
svg += qmarks([(150, 470, 90, -15), (720, 440, 110, 12), (270, 560, 70, -8), (660, 330, 64, 18), (110, 640, 60, -20)])
P.append(page(1, svg,
    '<div style="position:absolute;top:34px;left:40px;right:40px;font-family:\'Noto Serif TC\',serif;font-weight:900;font-size:66px;line-height:1.3;color:#2a2622">看了 <span style="color:#a8763e;font-size:90px">30</span> 支 K 線影片<br>還是看不懂？</div>',
    '<span class="acc">往左滑，看阿明的一天 →</span>'))
# 02 決心
svg = room(0) + aming(560, 600, "determined", "fist", stand=True)
svg += f'<path d="M420,420 l-60,-20 M410,470 l-70,0 M790,330 l50,-40" stroke="{ACC}" stroke-width="8" stroke-linecap="round"/>'
P.append(page(2, svg, '<div class="cap">19:30｜下班後</div><div class="bub dr" style="left:30px;top:100px;width:400px">今天一定要把<br>K 線學起來！</div>'))
# 03 睡著
svg = room(.6) + sofa(460, 760) + aming(470, 740, "sleep", "lap", tilt=-14)
svg += '<rect x="560" y="200" width="320" height="220" rx="18" fill="#2a2622"/><rect x="574" y="214" width="292" height="150" rx="8" fill="#3a4466"/>'
svg += '<path d="M690,250 l50,39 l-50,39z" fill="#fff" opacity=".9"/><rect x="574" y="378" width="292" height="30" rx="6" fill="#111"/>'
svg += '<text x="720" y="400" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="20" fill="#fff">……所以 CHoCH 就是……</text>'
svg += '<text x="590" y="240" font-family="Noto Sans TC" font-weight="700" font-size="22" fill="#fff" opacity=".8">第 3 支</text>'
svg += f'<text x="190" y="300" font-family="Noto Serif TC" font-weight="900" font-size="80" fill="{ACC}">Z</text><text x="250" y="240" font-family="Noto Serif TC" font-weight="900" font-size="60" fill="{ACC}">z</text><text x="290" y="200" font-family="Noto Serif TC" font-weight="900" font-size="44" fill="{ACC}">z</text>'
P.append(page(3, svg, '<div class="cap">21:40</div>'))
# 04 蚊香眼
svg = room(.9) + sofa(460, 760) + aming(460, 740, "dizzy", "phone")
cand = "".join(f'<rect x="{90+i*34}" y="{o}" width="20" height="{h}" rx="3" fill="{c}"/><line x1="{100+i*34}" y1="{o-14}" x2="{100+i*34}" y2="{o+h+14}" stroke="{c}" stroke-width="3"/>'
               for i, (o, h, c) in enumerate([(560, 60, "#2f8a5f"), (530, 70, "#d0584a"), (570, 50, "#2f8a5f"), (520, 90, "#d0584a"), (600, 40, "#2f8a5f"), (540, 80, "#d0584a"), (510, 60, "#2f8a5f")]))
svg += cand
svg += "".join(f'<rect x="{620+i*34}" y="{o}" width="20" height="{h}" rx="3" fill="{c}"/>' for i, (o, h, c) in enumerate([(560, 70, "#d0584a"), (520, 60, "#2f8a5f"), (580, 50, "#d0584a"), (530, 90, "#2f8a5f"), (560, 60, "#d0584a"), (510, 70, "#2f8a5f"), (550, 40, "#d0584a")]))
P.append(page(4, svg, '<div class="cap">23:15</div><div class="bub dr" style="left:120px;top:100px;width:700px">紅紅綠綠的……<br>所以現在是要漲，還是要跌？</div>'))
# 05 小狐狸探頭
svg = room(.9) + f'<rect x="260" y="380" width="400" height="640" rx="50" fill="{INK}"/><rect x="280" y="400" width="360" height="600" rx="34" fill="#cfe8ff"/>'
svg += f'<ellipse cx="460" cy="420" rx="200" ry="70" fill="#fff6d8" opacity=".9"/>'
svg += fox(460, 600, 1.0, "peek")
svg += f'<rect x="270" y="560" width="380" height="460" rx="0" fill="{INK}"/><rect x="290" y="560" width="340" height="420" fill="#cfe8ff"/>'
svg += "".join(f'<path d="M{x},{y} l6,14 l14,6 l-14,6 l-6,14 l-6,-14 l-14,-6 l14,-6z" fill="{ACC}"/>' for x, y in ((230, 360), (700, 330), (680, 470), (200, 500)))
svg += f'<rect x="300" y="600" width="320" height="40" rx="8" fill="#fff"/><rect x="300" y="660" width="240" height="40" rx="8" fill="#fff"/><rect x="300" y="720" width="280" height="40" rx="8" fill="#fff"/>'
P.append(page(5, svg, '<div class="bub fox dr" style="left:70px;top:60px;width:780px">看不懂很正常啦～<br>要不要來<span class="hl">小島</span>玩一下？</div>'))
# 06 地圖
svg = f'<rect width="920" height="980" fill="#cfe9f5"/><rect x="40" y="300" width="840" height="560" rx="26" fill="#fff"/>'
svg += '<image href="map.png" x="56" y="316" width="808" height="528" preserveAspectRatio="xMidYMid slice"/>'
svg += fox(760, 940, .62, "wave")
P.append(page(6, svg, '<div class="bub fox dl" style="left:50px;top:50px;width:820px">看圖選答案，答錯也沒關係，<br>我會告訴你為什麼。</div>'))
# 07 答對
svg = room(.6) + sofa(620, 860, 420)
svg += f'<rect x="60" y="150" width="400" height="800" rx="48" fill="{INK}"/><clipPath id="sc"><rect x="78" y="168" width="364" height="764" rx="32"/></clipPath>'
svg += '<image href="quiz.png" x="78" y="168" width="364" height="764" preserveAspectRatio="xMidYMax slice" clip-path="url(#sc)"/>'
svg += aming(660, 840, "shine", "lap")
svg += "".join(f'<path d="M{x},{y} l6,14 l14,6 l-14,6 l-6,14 l-6,-14 l-14,-6 l14,-6z" fill="{ACC}"/>' for x, y in ((540, 300), (800, 280), (560, 420)))
P.append(page(7, svg, '<div class="bub dl" style="left:480px;top:150px;width:400px;font-size:40px">欸……<br>原來這根是<br>在說這個！</div>'))
# 08 收尾
svg = f'<rect width="920" height="980" fill="#cfe9f5"/><rect y="760" width="920" height="220" fill="#9fd08a"/>'
svg += f'<rect x="470" y="380" width="380" height="300" rx="16" fill="#c8955c"/><rect x="490" y="400" width="340" height="260" rx="10" fill="#e1b27a"/><rect x="640" y="680" width="40" height="160" fill="#a8763e"/>'
svg += f'<text x="660" y="470" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="38" fill="{INK}">主頁連結</text><text x="660" y="520" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="30" fill="{INK}">↓</text>'
svg += f'<text x="660" y="565" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="38" fill="{INK}">加 LINE@</text><text x="660" y="610" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="30" fill="{INK}">↓</text>'
svg += f'<rect x="555" y="620" width="210" height="52" rx="8" fill="#ffe066"/><text x="660" y="658" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="36" fill="{INK}">回覆「小島」</text>'
svg += fox(250, 830, .9, "wave")
P.append(page(8, svg, '<div class="bub fox dl" style="left:50px;top:60px;width:820px">想跟小狐狸<br>一起闖關嗎？🏝️</div>',
              '📌 先收藏，想玩的時候再來找我'))

html = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&family=Mrs+Saint+Delafield&display=block" rel="stylesheet">'
        f'<style>{CSS}</style></head><body>' + "\n".join(P) + '<script>document.fonts.ready.then(()=>setTimeout(()=>{document.body.dataset.ready="1"},300))</script></body></html>')
open(os.path.join(HERE, "slides.html"), "w", encoding="utf-8").write(html)
print(len(P))
