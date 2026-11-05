"""K 棒教學圖卡產生器：import 這個檔，用 page()/candle() 組頁面，write() 輸出 slides.html。"""

CSS = """
:root { --bg:#f4efe6; --card:#fbf8f2; --ink:#2a2622; --soft:#7a7066; --accent:#a8763e; --up:#2f8a5f; --down:#d0584a; --line:#ddd2c1; }
* { box-sizing:border-box; margin:0; padding:0; }
body { background:#999; font-family:"Noto Sans TC",sans-serif; color:var(--ink); }
.slide { width:1080px; height:1350px; background:var(--bg); position:relative; overflow:hidden; margin:0 0 20px; padding:150px 90px 150px; display:flex; flex-direction:column; justify-content:center; }
.top { position:absolute; top:60px; left:90px; right:90px; display:flex; justify-content:space-between; font-size:24px; letter-spacing:.18em; color:var(--soft); }
.foot { position:absolute; bottom:56px; left:90px; right:90px; display:flex; justify-content:space-between; font-size:22px; letter-spacing:.1em; color:var(--soft); border-top:1.5px solid var(--line); padding-top:18px; }
.serif { font-family:"Noto Serif TC",serif; }
.kicker { font-size:36px; color:var(--soft); letter-spacing:.1em; margin-bottom:18px; }
h1 { font-family:"Noto Serif TC",serif; font-size:88px; line-height:1.3; font-weight:900; letter-spacing:.04em; }
h2 { font-family:"Noto Serif TC",serif; font-size:62px; line-height:1.35; font-weight:900; margin-bottom:36px; }
.acc { color:var(--accent); } .up { color:var(--up); } .down { color:var(--down); }
p { font-size:36px; line-height:1.7; margin-bottom:24px; }
.card { font-size:34px; line-height:1.6; background:var(--card); border:1.5px solid var(--line); border-radius:22px; padding:30px 36px; margin-bottom:26px; }
.card b { font-size:38px; }
.take { font-family:"Noto Serif TC",serif; font-weight:900; font-size:40px; margin-top:20px; }
.take::before { content:""; display:block; width:88px; height:5px; background:var(--accent); margin-bottom:20px; }
.num { display:inline-block; width:54px; height:54px; border-radius:50%; background:var(--ink); color:var(--bg); text-align:center; line-height:54px; font-size:30px; font-weight:700; margin-right:18px; }
.row { display:flex; align-items:flex-start; margin-bottom:30px; font-size:36px; line-height:1.55; }
.row small { display:block; font-size:28px; color:var(--soft); }
table { width:100%; border-collapse:collapse; font-size:30px; line-height:1.5; }
th, td { border-bottom:1.5px solid var(--line); padding:20px 14px; text-align:left; vertical-align:middle; }
th { font-family:"Noto Serif TC",serif; font-size:34px; }
td:first-child { color:var(--soft); width:22%; }
svg { display:block; }
.note { font-size:24px; color:var(--soft); margin-top:24px; }
"""

UP, DOWN, INK, SOFT, ACC = "#2f8a5f", "#d0584a", "#2a2622", "#7a7066", "#a8763e"

def candle(x, o, c, h, l, w=56):
    """畫一根 K 棒。數值是 SVG 的 y 座標（越小越高）。收盤比開盤高（c < o）就是陽線。"""
    col = UP if c < o else DOWN
    top, bot = min(o, c), max(o, c)
    cx = x + w / 2
    return (f'<line x1="{cx}" y1="{h}" x2="{cx}" y2="{l}" stroke="{col}" stroke-width="4"/>'
            f'<rect x="{x}" y="{top}" width="{w}" height="{max(bot - top, 4)}" fill="{col}" rx="3"/>')

def svg(w, h, inner):
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans TC">{inner}</svg>'

def text(x, y, s, size=28, col=SOFT, anchor="start", weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{col}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def dashed(x1, y1, x2, y2, col=SOFT):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3" stroke-dasharray="10 8"/>'

def page(i, n, series, inner, footer="HANNA｜帶你看懂市場", cls=""):
    return (f'<section class="slide {cls}"><div class="top"><span>{series}</span><span>{i:02d} / {n:02d}</span></div>'
            f'{inner}<div class="foot"><span>{footer}</span><span>先收藏，看盤時對照</span></div></section>')

def write(path, pages, title="K 棒小教室"):
    html = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>' + title + '</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&display=block" rel="stylesheet">'
            '<style>' + CSS + '</style></head><body>' + "\n".join(pages) +
            '<script>document.fonts.ready.then(() => { document.body.dataset.ready = "1"; });</script></body></html>')
    open(path, "w", encoding="utf-8").write(html)
