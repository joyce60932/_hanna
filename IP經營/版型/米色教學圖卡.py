"""米色教學圖卡（收單系列用）。依輪播設計訓練：內文 ≥40px、邊距 ≥80px、最多 2 種字體、3 色＋黑白灰、右上角放頁碼。"""
INK, SOFT, ACC, UP, DOWN, BG, CARD, LINE = "#2a2622", "#7a7066", "#a8763e", "#2f8a5f", "#d0584a", "#f4efe6", "#fbf8f2", "#ddd2c1"

CSS = f"""
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ background:#999; font-family:"Noto Sans TC",sans-serif; color:{INK}; }}
.slide {{ width:1080px; height:1350px; background:{BG}; position:relative; overflow:hidden; margin:0 0 20px; }}
.top {{ position:absolute; top:64px; left:90px; right:90px; display:flex; justify-content:space-between; font-size:26px; letter-spacing:.16em; color:{SOFT}; }}
.foot {{ position:absolute; bottom:60px; left:90px; right:90px; display:flex; justify-content:space-between; align-items:flex-end; font-size:26px; letter-spacing:.08em; color:{SOFT}; }}
.sign {{ font-family:"Mrs Saint Delafield",cursive; font-size:84px; color:{ACC}; line-height:.6; }}
.body {{ position:absolute; top:170px; left:90px; right:90px; bottom:170px; display:flex; flex-direction:column; justify-content:center; }}
.serif {{ font-family:"Noto Serif TC",serif; }}
.kicker {{ font-size:34px; color:{ACC}; letter-spacing:.12em; margin-bottom:28px; font-weight:700; }}
h1 {{ font-family:"Noto Serif TC",serif; font-weight:900; font-size:112px; line-height:1.3; letter-spacing:-.02em; }}
h2 {{ font-family:"Noto Serif TC",serif; font-weight:900; font-size:72px; line-height:1.35; margin-bottom:44px; }}
p {{ font-size:42px; line-height:1.6; margin-bottom:28px; }}
.sub {{ font-family:"Noto Serif TC",serif; font-size:52px; font-weight:700; color:{SOFT}; margin-top:30px; }}
.acc {{ color:{ACC}; }} .up {{ color:{UP}; }} .down {{ color:{DOWN}; }}
.card {{ background:{CARD}; border:2px solid {LINE}; border-radius:24px; padding:34px 40px; margin-bottom:26px; font-size:40px; line-height:1.55; }}
.row {{ display:flex; align-items:flex-start; gap:22px; font-size:42px; line-height:1.5; margin-bottom:22px; }}
.mk {{ flex:none; width:52px; font-weight:700; }}
.take {{ font-family:"Noto Serif TC",serif; font-weight:900; font-size:48px; line-height:1.45; margin-top:26px; }}
.take::before {{ content:""; display:block; width:96px; height:6px; background:{ACC}; margin-bottom:26px; }}
.num {{ display:inline-flex; align-items:center; justify-content:center; width:96px; height:96px; border-radius:50%; background:{ACC}; color:{BG}; font-family:"Noto Serif TC",serif; font-weight:900; font-size:52px; margin-bottom:34px; }}
.quote {{ font-family:"Noto Serif TC",serif; font-weight:900; font-size:66px; line-height:1.4; margin-bottom:40px; }}
table {{ width:100%; border-collapse:collapse; font-size:34px; line-height:1.4; background:{CARD}; border-radius:18px; overflow:hidden; }}
th, td {{ border:2px solid {LINE}; padding:22px 18px; text-align:left; vertical-align:top; }}
th {{ font-family:"Noto Serif TC",serif; font-size:36px; background:#efe6d6; }}
.note {{ font-size:30px; color:{SOFT}; margin-top:18px; line-height:1.5; }}
.cta {{ display:inline-block; background:{INK}; color:{BG}; font-family:"Noto Serif TC",serif; font-weight:900; font-size:44px; padding:24px 44px; border-radius:60px; margin-top:10px; }}
"""

def page(i, n, label, inner):
    return (f'<section class="slide"><div class="top"><span>BISANCOS・Hanna｜{label}</span><span>{i:02d} / {n:02d}</span></div>'
            f'<div class="body">{inner}</div>'
            f'<div class="foot"><span>Hanna｜教路人會交易的教官</span><span class="sign">Hanna</span></div></section>')

def write(path, pages, title):
    html = ('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><title>' + title + '</title>'
            '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&family=Mrs+Saint+Delafield&display=block" rel="stylesheet">'
            '<style>' + CSS + '</style></head><body>' + "\n".join(pages) +
            '<script>document.fonts.ready.then(()=>{document.body.dataset.ready="1"})</script></body></html>')
    open(path, "w", encoding="utf-8").write(html)
