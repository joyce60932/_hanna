"""Q 版動態漫畫：阿明的 K 線日記（小島遊戲導流）。每頁一個 HTML，window.setT(t) 驅動動畫。"""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
INK, SOFT, ACC, BG = "#2a2622", "#7a7066", "#a8763e", "#f4efe6"
SKIN, HAIR, SHIRT, TIE, PANTS = "#ffd9bd", "#2b2a33", "#8ec5f2", "#2d3e66", "#4a4f5c"
FOX, FOXD, CREAM, PINK, YEL, UP, DN = "#f7893a", "#c9662a", "#fff3e2", "#ff8e9e", "#ffe066", "#2fae74", "#ef5b4c"
N = 8

def A(kind="", s=0, d=.35, loop="", amp=0, fr=0, o=None, e=None, ss=None):
    """動畫屬性：kind 進場、loop 循環、o 變形中心、e 消失時間、ss 震動開始。"""
    r = f' data-a="{kind}" data-s="{s}" data-d="{d}"'
    if loop: r += f' data-l="{loop}" data-amp="{amp}" data-fr="{fr}"'
    if o: r += f' data-ox="{o[0]}" data-oy="{o[1]}"'
    if e is not None: r += f' data-e="{e}"'
    if ss is not None: r += f' data-ss="{ss}"'
    return r

def star(cx, cy, r, col, sw=0):
    pts = " ".join(f"{cx+(r if i%2==0 else r*.45)*math.cos(-math.pi/2+i*math.pi/5):.1f},{cy+(r if i%2==0 else r*.45)*math.sin(-math.pi/2+i*math.pi/5):.1f}" for i in range(10))
    st = f' stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"' if sw else ""
    return f'<polygon points="{pts}" fill="{col}"{st}/>'

def sparkle(cx, cy, r, col="#fff"):
    return f'<path d="M{cx},{cy-r} Q{cx+r*.15},{cy-r*.15} {cx+r},{cy} Q{cx+r*.15},{cy+r*.15} {cx},{cy+r} Q{cx-r*.15},{cy+r*.15} {cx-r},{cy} Q{cx-r*.15},{cy-r*.15} {cx},{cy-r}Z" fill="{col}"/>'

def burst(cx, cy, c1, c2, n=24):
    s = f'<rect width="920" height="980" fill="{c1}"/>'
    for i in range(n):
        if i % 2: continue
        a0, a1 = i*2*math.pi/n, (i+1)*2*math.pi/n
        s += f'<path d="M{cx},{cy} L{cx+1400*math.cos(a0):.0f},{cy+1400*math.sin(a0):.0f} L{cx+1400*math.cos(a1):.0f},{cy+1400*math.sin(a1):.0f}Z" fill="{c2}"/>'
    return s

def sfx(x, y, text, size, rot=0, fill="#fff", attrs=""):
    return (f'<g{attrs}><text x="{x}" y="{y}" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="{size}" '
            f'fill="{fill}" stroke="{INK}" stroke-width="{size*.12:.0f}" stroke-linejoin="round" paint-order="stroke" transform="rotate({rot} {x} {y})">{text}</text></g>')

def bubble(x, y, w, lines, tail, size=44, border=INK, kind="speech", attrs="", hl=None):
    h = len(lines) * size * 1.4 + size * 0.9
    tx, ty = tail
    s = f'<g{attrs}>'
    if kind == "shout":
        pts, n = [], 28
        cx, cy, rx, ry = x + w/2, y + h/2, w/2 + 26, h/2 + 26
        for i in range(n):
            a = i * 2*math.pi/n; k = 1 if i % 2 == 0 else .86
            pts.append(f"{cx+rx*k*math.cos(a):.0f},{cy+ry*k*math.sin(a):.0f}")
        s += f'<polygon points="{" ".join(pts)}" fill="#fff" stroke="{border}" stroke-width="6" stroke-linejoin="round"/>'
    else:
        bx = min(max(tx, x+60), x+w-60)
        by = y + h if ty > y + h/2 else y
        s += f'<path d="M{bx-26},{by} L{tx},{ty} L{bx+26},{by}Z" fill="#fff" stroke="{border}" stroke-width="6" stroke-linejoin="round"/>'
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(48, h/2)}" fill="#fff" stroke="{border}" stroke-width="6"/>'
        s += f'<path d="M{bx-23},{by} L{bx+23},{by}" stroke="#fff" stroke-width="9"/>'
    for i, ln in enumerate(lines):
        ly = y + size*0.45 + size*1.4*i + size
        if hl and hl[0] == i:
            s += f'<rect x="{x+34+hl[1]*size-4}" y="{ly-size*.92}" width="{hl[2]*size+8}" height="{size*1.18}" rx="8" fill="{YEL}"/>'
        s += f'<text x="{x+34}" y="{ly}" font-family="Noto Serif TC" font-weight="900" font-size="{size}" fill="{INK}">{ln}</text>'
    return s + '</g>'

def caption(text, attrs=""):
    w = len(text) * 30 + 40
    return f'<g{attrs}><rect x="24" y="24" width="{w}" height="58" rx="8" fill="{INK}"/><text x="44" y="66" font-family="Noto Serif TC" font-weight="900" font-size="32" fill="{BG}">{text}</text></g>'

# ---------- Q 版阿明（2 頭身） ----------
def q_face(x, y, mood):
    s = ""
    if mood == "worried":
        for k in (-1, 1):
            s += f'<ellipse cx="{x+k*42}" cy="{y}" rx="14" ry="19" fill="{INK}"/><circle cx="{x+k*42+5}" cy="{y-7}" r="6" fill="#fff"/>'
            s += f'<path d="M{x+k*62},{y-40} L{x+k*24},{y-30}" stroke="{HAIR}" stroke-width="7" stroke-linecap="round"/>'
        s += f'<path d="M{x-16},{y+42} q8,-8 16,0 t16,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
        s += f'<path d="M{x+104},{y-46} q12,20 0,32 q-12,-12 0,-32z" fill="#7fc8f0"/>'
    elif mood == "fire":
        for k in (-1, 1):
            s += f'<path d="M{x+k*62},{y-6} L{x+k*22},{y+4}" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>'
            s += f'<path d="M{x+k*66},{y-38} L{x+k*20},{y-18}" stroke="{HAIR}" stroke-width="9" stroke-linecap="round"/>'
        s += f'<rect x="{x-30}" y="{y+28}" width="60" height="26" rx="8" fill="#fff" stroke="{INK}" stroke-width="5"/><path d="M{x},{y+28} v26 M{x-30},{y+41} h60" stroke="{INK}" stroke-width="3"/>'
    elif mood == "sleep":
        for k in (-1, 1):
            s += f'<path d="M{x+k*42-18},{y} q18,14 36,0" stroke="{INK}" stroke-width="6" fill="none" stroke-linecap="round"/>'
        s += f'<ellipse cx="{x}" cy="{y+40}" rx="14" ry="11" fill="{INK}"/><path d="M{x+12},{y+46} q8,28 0,44 q-10,-10 0,-44z" fill="#9fd6f2"/>'
    elif mood == "spiral":
        for k in (-1, 1):
            cx = x + k*42
            s += (f'<g{A(loop="spin", amp=420, o=(cx, y))}><path d="M{cx},{y} m-18,0 a18,18 0 1,1 36,0 a13,13 0 1,1 -26,0 a8,8 0 1,1 16,0 a4,4 0 1,1 -8,0" '
                  f'stroke="{INK}" stroke-width="5" fill="none"/></g>')
        s += f'<path d="M{x-24},{y+44} q8,-10 16,0 t16,0 t16,0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
    elif mood == "star":
        for k in (-1, 1):
            s += star(x+k*42, y, 26, "#ffd23f", 4)
        s += f'<path d="M{x-30},{y+30} q30,40 60,0z" fill="{INK}"/><path d="M{x-14},{y+46} q14,12 28,0" fill="{PINK}"/>'
    for k in (-1, 1):
        s += f'<ellipse cx="{x+k*74}" cy="{y+28}" rx="18" ry="10" fill="#ff9aa0" opacity=".65"/>'
    return s

def q_head(x, y, mood):
    s = f'<circle cx="{x-122}" cy="{y+14}" r="22" fill="{SKIN}" stroke="{INK}" stroke-width="5"/><circle cx="{x+122}" cy="{y+14}" r="22" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>'
    s += f'<ellipse cx="{x}" cy="{y}" rx="126" ry="114" fill="{SKIN}" stroke="{INK}" stroke-width="6"/>'
    s += (f'<path d="M{x-128},{y+4} C{x-140},{y-120} {x+120},{y-160} {x+130},{y-6} L{x+104},{y-40} L{x+80},{y-8} L{x+46},{y-56} L{x+10},{y-20} '
          f'L{x-30},{y-64} L{x-60},{y-22} L{x-96},{y-60} L{x-108},{y-6}z" fill="{HAIR}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>')
    return s + q_face(x, y + 24, mood)

def q_aming(x, y, mood="worried", arms="down", sit=False):
    """y 是腳底。"""
    hy = y - 300
    s = ""
    if sit:
        s += f'<rect x="{x-74}" y="{y-80}" width="148" height="50" rx="24" fill="{PANTS}" stroke="{INK}" stroke-width="5"/>'
        s += f'<ellipse cx="{x-46}" cy="{y-26}" rx="34" ry="18" fill="{INK}"/><ellipse cx="{x+46}" cy="{y-26}" rx="34" ry="18" fill="{INK}"/>'
    else:
        s += f'<rect x="{x-56}" y="{y-80}" width="46" height="72" rx="18" fill="{PANTS}" stroke="{INK}" stroke-width="5"/><rect x="{x+10}" y="{y-80}" width="46" height="72" rx="18" fill="{PANTS}" stroke="{INK}" stroke-width="5"/>'
        s += f'<ellipse cx="{x-36}" cy="{y-8}" rx="36" ry="16" fill="{INK}"/><ellipse cx="{x+36}" cy="{y-8}" rx="36" ry="16" fill="{INK}"/>'
    def arm(x1, y1, x2, y2, cxp, cyp):
        return (f'<path d="M{x1},{y1} Q{cxp},{cyp} {x2},{y2}" stroke="{INK}" stroke-width="34" fill="none" stroke-linecap="round"/>'
                f'<path d="M{x1},{y1} Q{cxp},{cyp} {x2},{y2}" stroke="{SHIRT}" stroke-width="24" fill="none" stroke-linecap="round"/>'
                f'<circle cx="{x2}" cy="{y2}" r="20" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>')
    sy = y - 186
    ARMS = {"down": [(x-66, sy, x-92, y-96, x-100, y-140), (x+66, sy, x+92, y-96, x+100, y-140)],
            "head": [(x-66, sy, x-128, hy+10, x-130, sy-40), (x+66, sy, x+128, hy+10, x+130, sy-40)],
            "fist": [(x-66, sy, x-96, y-100, x-104, y-140), (x+66, sy, x+150, hy-60, x+160, sy-40)],
            "phone": [(x-66, sy, x-30, y-140, x-100, y-130), (x+66, sy, x+30, y-140, x+100, y-130)],
            "cheer": [(x-66, sy, x-150, hy-50, x-140, sy-30), (x+66, sy, x+150, hy-50, x+140, sy-30)]}
    body = f'<path d="M{x-74},{y-70} L{x-70},{sy-10} Q{x-66},{sy-24} {x-30},{sy-26} L{x+30},{sy-26} Q{x+66},{sy-24} {x+70},{sy-10} L{x+74},{y-70}z" fill="{SHIRT}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
    body += f'<path d="M{x-26},{sy-24} L{x},{sy+6} L{x+26},{sy-24}" fill="#fff" stroke="{INK}" stroke-width="4"/>'
    body += f'<path d="M{x-8},{sy+2} h16 l8,60 l-16,16 l-16,-16z" fill="{TIE}" stroke="{INK}" stroke-width="3" transform="rotate(10 {x} {sy})"/>'
    s += body
    if arms == "phone":
        s += "".join(arm(*a) for a in ARMS[arms])
        s += f'<rect x="{x-44}" y="{y-210}" width="88" height="130" rx="14" fill="{INK}"/><rect x="{x-36}" y="{y-200}" width="72" height="104" rx="8" fill="#cfe8ff"/>'
        s += f'<circle cx="{x-40}" cy="{y-140}" r="20" fill="{SKIN}" stroke="{INK}" stroke-width="5"/><circle cx="{x+40}" cy="{y-140}" r="20" fill="{SKIN}" stroke="{INK}" stroke-width="5"/>'
        s += q_head(x, hy, mood)
    else:
        s += q_head(x, hy, mood) + "".join(arm(*a) for a in ARMS[arms])
    return s

# ---------- 小狐狸 ----------
def fox(x, y, s=1.0, pose="cheeks"):
    o = f'<g transform="translate({x} {y}) scale({s}) translate({-x} {-y})">'
    o += f'<path d="M{x+60},{y+40} C{x+200},{y+10} {x+210},{y-140} {x+120},{y-160} C{x+170},{y-90} {x+130},{y-10} {x+50},{y-10}z" fill="{FOX}" stroke="{INK}" stroke-width="6"/>'
    o += f'<path d="M{x+120},{y-160} C{x+160},{y-150} {x+180},{y-110} {x+168},{y-80} C{x+150},{y-110} {x+130},{y-130} {x+120},{y-160}z" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x}" cy="{y}" rx="78" ry="88" fill="{FOX}" stroke="{INK}" stroke-width="6"/><ellipse cx="{x}" cy="{y+18}" rx="48" ry="62" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x-40}" cy="{y+84}" rx="30" ry="16" fill="{FOXD}" stroke="{INK}" stroke-width="5"/><ellipse cx="{x+40}" cy="{y+84}" rx="30" ry="16" fill="{FOXD}" stroke="{INK}" stroke-width="5"/>'
    hy = y - 150
    for k in (-1, 1):
        o += f'<path d="M{x+k*30},{hy-60} L{x+k*92},{hy-150} L{x+k*100},{hy-30}z" fill="{FOX}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
        o += f'<path d="M{x+k*44},{hy-62} L{x+k*86},{hy-124} L{x+k*90},{hy-44}z" fill="{CREAM}"/>'
    o += f'<ellipse cx="{x}" cy="{hy}" rx="118" ry="102" fill="{FOX}" stroke="{INK}" stroke-width="6"/>'
    o += f'<path d="M{x-104},{hy+20} C{x-80},{hy+110} {x+80},{hy+110} {x+104},{hy+20} C{x+60},{hy+46} {x+20},{hy+10} {x},{hy+30} C{x-20},{hy+10} {x-60},{hy+46} {x-104},{hy+20}z" fill="{CREAM}"/>'
    for k in (-1, 1):
        o += f'<path d="M{x+k*48-18},{hy-4} q18,-22 36,0" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>'
        o += f'<ellipse cx="{x+k*72}" cy="{hy+30}" rx="18" ry="11" fill="{PINK}" opacity=".75"/>'
    o += f'<ellipse cx="{x}" cy="{hy+22}" rx="13" ry="9" fill="{INK}"/><path d="M{x-24},{hy+40} q24,36 48,0z" fill="#8a2f3a"/><path d="M{x-12},{hy+56} q12,10 24,0" fill="{PINK}"/>'
    if pose == "cheeks":
        o += f'<ellipse cx="{x-76}" cy="{hy+50}" rx="26" ry="32" fill="{FOX}" stroke="{INK}" stroke-width="5"/><ellipse cx="{x+76}" cy="{hy+50}" rx="26" ry="32" fill="{FOX}" stroke="{INK}" stroke-width="5"/>'
    elif pose == "jump":
        for k in (-1, 1):
            o += f'<path d="M{x+k*66},{y-40} Q{x+k*140},{y-90} {x+k*150},{y-180}" stroke="{INK}" stroke-width="48" fill="none" stroke-linecap="round"/><path d="M{x+k*66},{y-40} Q{x+k*140},{y-90} {x+k*150},{y-180}" stroke="{FOX}" stroke-width="36" fill="none" stroke-linecap="round"/><circle cx="{x+k*152}" cy="{y-190}" r="26" fill="{CREAM}" stroke="{INK}" stroke-width="5"/>'
    elif pose == "wave":
        o += f'<g{A(loop="wave", amp=14, fr=9, o=(x+66, y-40))}><path d="M{x+66},{y-40} Q{x+140},{y-80} {x+150},{y-170}" stroke="{INK}" stroke-width="48" fill="none" stroke-linecap="round"/><path d="M{x+66},{y-40} Q{x+140},{y-80} {x+150},{y-170}" stroke="{FOX}" stroke-width="36" fill="none" stroke-linecap="round"/><circle cx="{x+152}" cy="{y-182}" r="26" fill="{CREAM}" stroke="{INK}" stroke-width="5"/></g>'
        o += f'<ellipse cx="{x-70}" cy="{y-20}" rx="22" ry="30" fill="{FOX}" stroke="{INK}" stroke-width="5"/>'
    return o + '</g>'

def g(inner, attrs=""): return f'<g{attrs}>{inner}</g>'

# ---------- 頁面框架 ----------
CSS = f"""*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#000;font-family:"Noto Sans TC",sans-serif;color:{INK}}}
.slide{{width:1080px;height:1350px;background:{BG};position:relative;overflow:hidden}}
.top{{position:absolute;top:58px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:26px;letter-spacing:.14em;color:{SOFT}}}
.foot{{position:absolute;bottom:52px;left:80px;right:80px;display:flex;justify-content:space-between;align-items:flex-end;font-size:26px;color:{SOFT};letter-spacing:.08em}}
.sign{{font-family:"Mrs Saint Delafield",cursive;font-size:80px;color:{ACC};line-height:.6}}
.panel{{position:absolute;top:130px;left:80px;width:920px;height:980px;border:6px solid {INK};border-radius:28px;overflow:hidden}}
.panel svg{{display:block}}
.under{{position:absolute;left:80px;right:80px;top:1132px;font-family:"Noto Serif TC",serif;font-weight:900;font-size:40px;text-align:center;color:{ACC}}}"""

JS = """<script>
const EL=[...document.querySelectorAll('[data-a],[data-l]')];
const c=x=>Math.max(0,Math.min(1,x)), eo=p=>1-Math.pow(1-p,3), bo=p=>{p=c(p);const k=1.9;return 1+(k+1)*Math.pow(p-1,3)+k*Math.pow(p-1,2)};
const bounce=p=>{p=c(p);const n=7.5625,d=2.75;if(p<1/d)return n*p*p;if(p<2/d)return n*(p-=1.5/d)*p+.75;if(p<2.5/d)return n*(p-=2.25/d)*p+.9375;return n*(p-=2.625/d)*p+.984375};
for(const e of EL){if(!e.dataset.ox){const b=e.getBBox();e.dataset.ox=b.x+b.width/2;e.dataset.oy=b.y+b.height/2;}}
window.setT=function(t){for(const e of EL){const D=e.dataset,s=+(D.s||0),d=+(D.d||.35),p=c((t-s)/d),ox=+D.ox,oy=+D.oy,amp=+(D.amp||0),fr=+(D.fr||0);
 let sc=1,dx=0,dy=0,rot=0,op=1;
 switch(D.a){case'pop':sc=bo(p);op=t>=s?1:0;break;case'drop':dy=-(1-bounce(p))*500;op=t>=s?1:0;break;
  case'fade':op=p;break;case'rise':dy=(1-eo(p))*60;op=p;break;case'up':dy=(1-bo(p))*520;op=t>=s?1:0;break;
  case'slide':dx=(1-eo(p))*-700;op=t>=s?1:0;break;case'grow':sc=.25+eo(p)*1.05;op=t>=s?1:0;break;}
 const tt=Math.max(0,t-s);
 switch(D.l){case'bob':dy+=amp*Math.sin(fr*tt);break;case'spin':rot+=amp*tt;break;case'pulse':sc*=1+amp*Math.sin(fr*tt);break;
  case'wave':rot+=amp*Math.sin(fr*tt);break;case'float':{const ph=(tt*fr)%1;dy-=ph*amp;op*=t>=s?Math.min(1,(1-ph)*1.6):0;break;}}
 if(D.ss!==undefined){const k=t-(+D.ss);if(k>=0&&k<.45)dx+=18*Math.sin(k*70)*(1-k/.45);}
 if(D.e!==undefined&&t>=+D.e)op=0;
 e.setAttribute('transform',`translate(${ox+dx} ${oy+dy}) rotate(${rot}) scale(${sc}) translate(${-ox} ${-oy})`);e.setAttribute('opacity',op);}};
</script>"""

def page(i, dur, svg, under=""):
    return ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&family=Mrs+Saint+Delafield&display=block" rel="stylesheet">'
            f'<style>{CSS}</style></head><body><section class="slide"><div class="top"><span>BISANCOS・Hanna｜阿明的 K 線日記</span><span>{i:02d} / {N:02d}</span></div>'
            f'<div class="panel"><svg width="920" height="980" viewBox="0 0 920 980" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">{svg}</svg></div>'
            f'<div class="under">{under}</div><div class="foot"><span>Hanna｜教路人會交易的教官</span><span class="sign">Hanna</span></div></section>'
            f'{JS}<script>window.DUR={dur};document.fonts.ready.then(()=>{{setT(0);document.body.dataset.ready="1"}})</script></body></html>')

P = []
# 01 封面：30 支影片疊上來
svg = burst(460, 600, "#ffe08a", "#ffd25c")
svg += g(f'<text x="460" y="120" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{INK}">看了<tspan fill="#e0641c" font-size="96"> 30 </tspan>支 K 線影片</text>'
         f'<text x="460" y="215" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="74" fill="{INK}">還是看不懂？</text>', A("rise", 0, .4))
thumbs = [(170, 420, -14), (750, 400, 12), (130, 640, -8), (790, 620, 10), (150, 330, -20), (770, 300, 18), (210, 820, 6), (720, 830, -6)]
for k, (tx, ty, r) in enumerate(thumbs):
    svg += g(f'<g transform="rotate({r} {tx} {ty})"><rect x="{tx-90}" y="{ty-56}" width="180" height="112" rx="12" fill="#3a4466" stroke="{INK}" stroke-width="5"/>'
             f'<path d="M{tx-16},{ty-24} l40,24 l-40,24z" fill="#fff"/><rect x="{tx-80}" y="{ty+34}" width="{60+k*12}" height="8" rx="4" fill="{ACC}"/></g>', A("pop", .3 + k*.1, .3))
svg += g(q_aming(460, 900, "spiral", "head"), A("pop", .1, .4, ss=1.35))
svg += g(f'<path d="M310,440 l-34,-20 M300,480 l-40,0 M610,440 l34,-20 M620,480 l40,0" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>', A("fade", 1.2, .2))
svg += sfx(720, 560, "30", 150, 10, "#ffd23f", A("pop", 1.3, .35, loop="pulse", amp=.05, fr=10))
P.append(page(1, 3.6, svg, "往左滑，看阿明的一天 →"))

# 02 決心
svg = burst(460, 520, "#c9e8ff", "#b3ddff")
svg += g(f'<path d="M460,860 C300,800 300,560 380,470 C380,560 430,560 430,500 C430,400 500,380 520,300 C560,420 640,480 620,600 C660,560 650,500 640,470 C720,560 640,820 460,860Z" fill="#ff8a3d" opacity=".85"/>', A("pop", .3, .4, loop="pulse", amp=.04, fr=14, o=(460, 860)))
svg += g(q_aming(460, 900, "fire", "fist"), A("drop", 0, .6))
svg += sfx(760, 300, "燃！", 110, 12, "#ff6a3d", A("pop", .7, .3))
svg += bubble(70, 120, 470, ["今天一定要把", "K 線學起來！"], (380, 380), 50, kind="shout", attrs=A("pop", .9, .35))
svg += caption("19:30｜下班後", A("fade", 0, .2))
P.append(page(2, 3.4, svg))

# 03 睡著：鼻涕泡泡啵
svg = '<rect width="920" height="980" fill="#2e335f"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".6"/>' for x, y, r in ((120, 160, 3), (300, 90, 2), (520, 140, 3), (820, 220, 2), (700, 80, 3)))
svg += '<circle cx="780" cy="150" r="50" fill="#fff3c9"/><circle cx="800" cy="138" r="46" fill="#2e335f"/>'
svg += '<rect x="80" y="640" width="760" height="230" rx="50" fill="#8b7ba8" stroke="#1d1a33" stroke-width="6"/><rect x="40" y="740" width="120" height="200" rx="40" fill="#7a6a98" stroke="#1d1a33" stroke-width="6"/><rect x="760" y="740" width="120" height="200" rx="40" fill="#7a6a98" stroke="#1d1a33" stroke-width="6"/>'
svg += g(q_aming(420, 940, "sleep", "down", sit=True), f' transform="rotate(-10 420 700)"')
svg += g(f'<circle cx="372" cy="700" r="34" fill="#cdeeff" stroke="#7fc8f0" stroke-width="4" opacity=".9"/><circle cx="362" cy="688" r="8" fill="#fff"/>', A("grow", .2, 1.9, o=(400, 700), e=2.3))
svg += sfx(300, 560, "啵！", 100, -8, "#fff", A("pop", 2.3, .3))
for k in range(3):
    svg += g(f'<text x="{560+k*40}" y="{420-k*40}" font-family="Noto Serif TC" font-weight="900" font-size="{70-k*14}" fill="#ffe066">Z</text>', A("", .0 + k*.4, loop="float", amp=80, fr=.7))
svg += g(f'<rect x="560" y="660" width="300" height="200" rx="16" fill="{INK}" transform="rotate(8 710 760)"/><rect x="574" y="674" width="272" height="140" rx="8" fill="#3a4466" transform="rotate(8 710 760)"/>'
         f'<path d="M690,710 l46,30 l-46,30z" fill="#fff" transform="rotate(8 710 760)"/>'
         f'<text x="710" y="842" text-anchor="middle" font-family="Noto Sans TC" font-weight="700" font-size="22" fill="#fff" transform="rotate(8 710 760)">……所以 CHoCH 就是……</text>'
         f'<text x="590" y="700" font-family="Noto Sans TC" font-weight="700" font-size="22" fill="#ffe066" transform="rotate(8 710 760)">第 3 支</text>', A("fade", 0, .3))
svg += caption("21:40", A("fade", 0, .2))
P.append(page(3, 3.8, svg))

# 04 蚊香眼＋K 棒漩渦
svg = '<rect width="920" height="980" fill="#6b4fa8"/>' + "".join(f'<circle cx="460" cy="600" r="{r}" fill="none" stroke="#7f63bd" stroke-width="40"/>' for r in (140, 260, 380, 500))
ring = ""
for k in range(12):
    a = k * 2*math.pi/12
    cx, cy = 460 + 330*math.cos(a), 600 + 330*math.sin(a)
    col = UP if k % 2 else DN
    ring += f'<g transform="rotate({math.degrees(a)+90:.0f} {cx:.0f} {cy:.0f})"><line x1="{cx:.0f}" y1="{cy-52:.0f}" x2="{cx:.0f}" y2="{cy+52:.0f}" stroke="{INK}" stroke-width="5"/><rect x="{cx-17:.0f}" y="{cy-34:.0f}" width="34" height="68" rx="4" fill="{col}" stroke="{INK}" stroke-width="4"/></g>'
svg += g(ring, A("fade", 0, .3, loop="spin", amp=40, o=(460, 600)))
svg += g(q_aming(460, 940, "spiral", "phone"), A("pop", .1, .35, loop="bob", amp=6, fr=4))
svg += sfx(150, 380, "暈～", 90, -12, "#ffe066", A("pop", 1.0, .3))
svg += bubble(60, 60, 800, ["紅紅綠綠的……", "所以現在是要漲，還是要跌？"], (420, 330), 48, attrs=A("pop", .6, .35))
svg += caption("23:15", A("fade", 0, .2)).replace('y="24"', 'y="900"').replace('y="66"', 'y="942"')
P.append(page(4, 3.6, svg))

# 05 小狐狸蹦出來
svg = burst(460, 640, "#ffd2a1", "#ffbf7d")
svg += f'<rect x="250" y="560" width="420" height="520" rx="54" fill="{INK}"/><rect x="272" y="582" width="376" height="470" rx="36" fill="#cfe8ff"/>'
svg += g(fox(460, 640, 1.05, "jump"), A("up", .4, .55))
svg += f'<rect x="250" y="760" width="420" height="320" fill="{INK}"/><rect x="272" y="760" width="376" height="292" fill="#cfe8ff"/>'
for k, (x, y, r) in enumerate(((160, 470, 30), (770, 430, 36), (200, 680, 22), (740, 650, 26), (460, 300, 24))):
    svg += g(sparkle(x, y, r, "#fff"), A("pop", .8 + k*.06, .25, loop="pulse", amp=.15, fr=8))
svg += sfx(730, 330, "蹦！", 120, 14, "#ffe066", A("pop", .7, .3))
svg += bubble(40, 40, 840, ["看不懂很正常啦～", "要不要來小島玩一下？"], (420, 290), 50, border=FOXD, attrs=A("pop", 1.3, .35), hl=(1, 4, 2))
P.append(page(5, 3.8, svg))

# 06 地圖
svg = '<rect width="920" height="980" fill="#bfe6f7"/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.45}" fill="#fff" opacity=".8"/>' for x, y, r in ((120, 300, 90), (780, 260, 110), (650, 920, 120)))
svg += g('<rect x="40" y="330" width="840" height="560" rx="26" fill="#fff" stroke="#2a2622" stroke-width="6"/><image href="../map.png" x="56" y="346" width="808" height="528" preserveAspectRatio="xMidYMid slice"/>', A("rise", .1, .45))
svg += g(fox(780, 960, .6, "wave"), A("pop", .6, .35, loop="bob", amp=6, fr=5))
svg += bubble(40, 50, 840, ["看圖選答案，答錯也沒關係，", "我會告訴你為什麼。"], (400, 300), 46, border=FOXD, attrs=A("pop", 1.0, .35))
for k, (x, y) in enumerate(((140, 420), (520, 700), (300, 820))):
    svg += g(sparkle(x, y, 24, "#ffe066"), A("pop", 1.4 + k*.1, .25, loop="pulse", amp=.2, fr=7))
P.append(page(6, 3.4, svg))

# 07 答對了
svg = burst(560, 500, "#fff2b3", "#ffe48a")
svg += g(f'<rect x="50" y="130" width="400" height="800" rx="48" fill="{INK}"/><clipPath id="sc"><rect x="68" y="148" width="364" height="764" rx="32"/></clipPath>'
         '<image href="../quiz.png" x="68" y="148" width="364" height="764" preserveAspectRatio="xMidYMax slice" clip-path="url(#sc)"/>', A("slide", 0, .4))
svg += g(f'<rect x="90" y="430" width="560" height="130" rx="65" fill="{UP}" stroke="{INK}" stroke-width="6"/>'
         f'<text x="370" y="518" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="58" fill="#fff">叮！答對了 +10</text>', A("pop", .9, .35, ss=None))
svg += g(q_aming(690, 940, "star", "cheer"), A("pop", .3, .35, loop="bob", amp=14, fr=9))
for k, (x, y) in enumerate(((560, 300), (850, 360), (600, 640), (860, 640))):
    svg += g(star(x, y, 30, "#ffd23f", 4), A("pop", 1.0 + k*.07, .25))
svg += bubble(470, 40, 420, ["欸……原來", "這根是在說這個！"], (680, 330), 40, attrs=A("pop", 1.6, .35))
P.append(page(7, 3.8, svg))

# 08 收尾
svg = '<rect width="920" height="980" fill="#bfe6f7"/><rect y="760" width="920" height="220" fill="#9fd08a"/><ellipse cx="300" cy="780" rx="420" ry="60" fill="#8cc476"/>'
sign = (f'<rect x="470" y="370" width="390" height="330" rx="18" fill="#c8955c" stroke="{INK}" stroke-width="6"/><rect x="490" y="390" width="350" height="290" rx="10" fill="#e9bd85"/><rect x="645" y="700" width="40" height="150" fill="#a8763e" stroke="{INK}" stroke-width="5"/>'
        f'<text x="665" y="458" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{INK}">主頁連結</text><text x="665" y="505" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="32" fill="{INK}">↓</text>'
        f'<text x="665" y="555" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{INK}">加 LINE@</text><text x="665" y="600" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="32" fill="{INK}">↓</text>')
svg += g(sign, A("up", .3, .55))
svg += g(f'<rect x="530" y="612" width="270" height="58" rx="10" fill="{YEL}" stroke="{INK}" stroke-width="4"/><text x="665" y="654" text-anchor="middle" font-family="Noto Serif TC" font-weight="900" font-size="40" fill="{INK}">回覆「小島」</text>',
         A("up", .3, .55, loop="pulse", amp=.05, fr=7))
svg += g(fox(250, 840, .9, "wave"), A("pop", 0, .4, loop="bob", amp=6, fr=5))
svg += bubble(40, 50, 560, ["想跟小狐狸", "一起闖關嗎？🏝️"], (260, 330), 52, border=FOXD, attrs=A("pop", 1.0, .35))
for k, (x, y) in enumerate(((820, 160), (700, 260), (860, 300))):
    svg += g(sparkle(x, y, 22, "#fff"), A("pop", 1.3 + k*.08, .25, loop="pulse", amp=.2, fr=7))
P.append(page(8, 3.4, svg, "📌 先收藏，想玩的時候再來找我"))

os.makedirs(os.path.join(HERE, "html"), exist_ok=True)
for i, h in enumerate(P, 1):
    open(os.path.join(HERE, "html", f"p{i:02d}.html"), "w", encoding="utf-8").write(h)
print(len(P))
