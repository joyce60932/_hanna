# 深色輪播配色範例：A 深藍墨、B 炭灰，各做封面＋小抄頁
import os
OUT = os.path.dirname(os.path.abspath(__file__))
PAL = {
 'A': dict(bg='#13202E', card='#1B2B3D', line='#2C3E52', text='#F3EBDD', muted='#9FAAB6', accent='#E8A33D', up='#3DAA7D', down='#E35D5B', name='深藍墨'),
 'B': dict(bg='#1D1E21', card='#28292D', line='#3A3B40', text='#FFFFFF', muted='#9C9CA3', accent='#C9A962', up='#3DAA7D', down='#E35D5B', name='炭灰'),
}
HEAD = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Noto+Serif+TC:wght@700;900&family=Playfair+Display:ital,wght@1,600&display=swap" rel="stylesheet">
<style>
:root{{--bg:{bg};--card:{card};--line:{line};--text:{text};--muted:{muted};--accent:{accent};--up:{up};--down:{down}}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:var(--bg);color:var(--text);font-family:'Noto Sans TC',sans-serif;position:relative;overflow:hidden}}
.top{{position:absolute;top:64px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:26px;color:var(--muted);letter-spacing:2px}}
.foot{{position:absolute;bottom:60px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:24px;color:var(--muted)}}
.tag{{color:var(--accent);font-size:34px;font-weight:500;letter-spacing:2px}}
.en{{font-family:'Playfair Display',serif;font-style:italic;color:var(--accent)}}
</style></head><body>"""

def chart(p, w=760, h=520):
    # 兩根 K 棒＋停損虛線（綠漲紅跌；不放箭頭、不放買賣按鈕）
    y = lambda v: 40 + (100 - v) * (h - 80) / 100
    def candle(cx, o, c, hi, lo, col):
        top, bot = y(max(o, c)), y(min(o, c))
        return (f'<line x1="{cx}" y1="{y(hi)}" x2="{cx}" y2="{y(lo)}" stroke="{col}" stroke-width="6"/>'
                f'<rect x="{cx-55}" y="{top}" width="110" height="{bot-top}" rx="6" fill="{col}"/>')
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    for g in (40, 60, 80):
        s += f'<line x1="0" y1="{y(g)}" x2="{w}" y2="{y(g)}" stroke="{p["line"]}" stroke-width="2"/>'
    s += candle(220, 62, 40, 70, 22, p['down'])
    s += candle(440, 38, 80, 88, 30, p['up'])
    sl = y(14)
    s += f'<line x1="80" y1="{sl}" x2="{w-20}" y2="{sl}" stroke="{p["accent"]}" stroke-width="5" stroke-dasharray="18 12"/>'
    s += f'<text x="{w-20}" y="{sl-18}" text-anchor="end" font-size="36" font-weight="700" fill="{p["accent"]}" font-family="Noto Sans TC">停損放這裡</text>'
    s += f'<text x="196" y="{y(22)+8}" text-anchor="end" font-size="26" fill="{p["muted"]}" font-family="Noto Sans TC">最低點</text>'
    return s + '</svg>'

def cover(p):
    return HEAD.format(**p) + f"""
<div class="top"><span>BISANCOS・Hanna</span><span>01 / 07</span></div>
<div style="position:absolute;top:200px;left:80px;right:80px">
  <div class="tag"># 交易工具</div>
  <div style="font-family:'Noto Serif TC',serif;font-weight:900;font-size:104px;line-height:1.25;margin-top:28px">2 根 K 棒<br>找到你的<span style="color:var(--accent)">停損位置</span></div>
  <div class="en" style="font-size:64px;margin-top:20px">Stop Loss</div>
</div>
<div style="position:absolute;left:160px;top:720px">{chart(p)}</div>
<div class="foot"><span>看不懂 K 棒也沒關係</span><span>往左滑 →</span></div>
</body></html>"""

def cheat(p):
    steps = [('找到進場前的 2 根 K 棒', '只看最近這 2 根，不用看整張圖'),
             ('找出這 2 根的最低點', '影線也算，取最低的那一個'),
             ('停損放在最低點下方一點', '價格跌破這裡，代表原本的理由不成立')]
    rows = ''.join(f"""<div style="display:flex;gap:36px;align-items:flex-start;padding:40px 0;border-top:2px solid var(--line)">
      <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:76px;color:var(--accent);line-height:1;width:70px">{i+1}</div>
      <div><div style="font-size:46px;font-weight:700">{a}</div><div style="font-size:32px;color:var(--muted);margin-top:14px">{b}</div></div></div>"""
      for i, (a, b) in enumerate(steps))
    return HEAD.format(**p) + f"""
<div class="top"><span>BISANCOS・Hanna</span><span>07 / 07</span></div>
<div style="position:absolute;top:170px;left:80px;right:80px;background:var(--card);border-radius:28px;padding:64px 64px 30px">
  <div style="display:flex;justify-content:space-between;align-items:baseline">
    <div style="font-size:60px;font-weight:900">停損小抄</div>
    <div style="font-size:30px;color:var(--accent);border:2px solid var(--accent);border-radius:40px;padding:8px 26px">存起來</div>
  </div>
  <div style="margin-top:40px">{rows}</div>
</div>
<div style="position:absolute;top:1080px;left:80px;right:80px;font-family:'Noto Serif TC',serif;font-size:44px;font-weight:700;line-height:1.5">停損不是認輸，<br>是<span style="color:var(--accent)">先決定最多虧多少</span>。</div>
<div class="foot"><span>更多教學，請看主頁連結</span><span>@_hannapang</span></div>
</body></html>"""

for k, p in PAL.items():
    for name, fn in (('cover', cover), ('cheat', cheat)):
        open(os.path.join(OUT, f'{k}_{name}.html'), 'w', encoding='utf-8').write(fn(p))
print('ok')
