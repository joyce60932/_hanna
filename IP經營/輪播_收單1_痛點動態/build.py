"""收單系列 1｜篇 1 痛點：打字機（由左往右刷出）動態輪播。每頁一個 HTML，window.setT(t) 控制動畫。"""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
INK, SOFT, ACC, LINE = "#2a2622", "#7a7066", "#a8763e", "#ddd2c1"
N = 8

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;font-family:"Noto Sans TC",sans-serif;color:{INK}}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.paper{{position:absolute;inset:0;background-image:radial-gradient(rgba(120,100,80,.05) 1px,transparent 1px);background-size:6px 6px}}
.idx{{position:absolute;top:70px;left:90px;display:flex;gap:26px;font-family:"Noto Serif TC",serif;font-size:26px;color:#b3a898;letter-spacing:.05em}}
.idx b{{color:{INK};font-weight:900}}
.pn{{position:absolute;top:66px;right:90px;font-size:26px;color:{SOFT};letter-spacing:.12em}}
.foot{{position:absolute;bottom:60px;left:90px;right:90px;display:flex;justify-content:space-between;align-items:flex-end;font-size:26px;color:{SOFT};letter-spacing:.08em}}
.sign{{font-family:"Mrs Saint Delafield",cursive;font-size:84px;color:{ACC};line-height:.6}}
.body{{position:absolute;top:180px;left:90px;right:90px;bottom:190px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.w{{display:inline-block;white-space:nowrap}}
.lab{{background:{INK};color:#f4efe6;font-family:"Noto Serif TC",serif;font-weight:900;font-size:40px;padding:10px 26px;margin-bottom:40px;letter-spacing:.06em}}
.say{{font-size:32px;color:{SOFT};letter-spacing:.3em;margin-bottom:14px}}
.t{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:92px;line-height:1.25;letter-spacing:-.01em}}
.ul{{height:8px;background:{INK};width:640px;margin:22px auto 34px;transform-origin:left center}}
.s{{font-size:48px;font-weight:700;line-height:1.5;margin-bottom:12px}}
.res{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:72px;color:{ACC};line-height:1.3}}
.small{{font-size:38px;color:{SOFT};line-height:1.6}}
.h1{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:168px;line-height:1.15;letter-spacing:-.03em}}
.h2{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:86px;color:{ACC};line-height:1.3}}
.row{{font-family:"Noto Serif TC",serif;font-weight:900;font-size:62px;line-height:1.3;margin-bottom:30px}}
.row i{{font-style:normal;color:{ACC}}}
table{{width:100%;border-collapse:collapse;font-size:34px;line-height:1.4;background:#fbf8f2;text-align:left}}
th,td{{border:2px solid {LINE};padding:22px 18px;vertical-align:top}}
th{{font-family:"Noto Serif TC",serif;font-size:36px;background:#efe6d6}}
"""

def idx(i):
    return '<div class="idx">' + "".join(f'<b>{k:02d}</b>' if k == i else f'<span>{k:02d}</span>' for k in range(1, N + 1)) + '</div>'

def page(i, bg, body, static=False):
    script = "" if static else """
<script>
const EL=[...document.querySelectorAll('[data-s]')];
const F=14, c=x=>Math.max(0,Math.min(1,x));
window.setT=function(t){for(const e of EL){const s=+e.dataset.s,d=+e.dataset.d,k=e.dataset.k||'w',p=c((t-s)/d);
 if(k==='w'){const a=p*(100+F)-F;e.style.webkitMaskImage=e.style.maskImage=`linear-gradient(90deg,#000 ${a}%,transparent ${a+F}%)`;}
 else if(k==='x'){e.style.transform=`scaleX(${1-Math.pow(1-p,3)})`;}
 else if(k==='f'){e.style.opacity=p;e.style.transform=`translateY(${(1-p)*14}px)`;}}};
window.DUR=Math.max(...EL.map(e=>+e.dataset.s+ +e.dataset.d))+0.9;
</script>"""
    return ('<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&family=Noto+Serif+TC:wght@700;900&family=Mrs+Saint+Delafield&display=block" rel="stylesheet">'
            f'<style>{CSS}</style></head><body><section class="slide" style="background:{bg}"><div class="paper"></div>{idx(i)}<div class="pn">{i:02d} / {N:02d}</div>'
            f'<div class="body">{body}</div><div class="foot"><span>Hanna｜教路人會交易的教官</span><span class="sign">Hanna</span></div></section>'
            f'{script}<script>document.fonts.ready.then(()=>{{if(window.setT)setT(0);document.body.dataset.ready="1"}})</script></body></html>')

def W(cls, text, s, d, tag="div"):
    return f'<{tag} class="w {cls}" data-s="{s}" data-d="{d}">{text}</{tag}>'

def story(label, said, said2, result):
    return (W("lab", label, .15, .35) + "<div></div>" + W("say", "你　說", .45, .2)
            + W("t", said, .6, .65) + f'<div class="ul" data-s="1.2" data-d=".35" data-k="x"></div>'
            + W("s", said2, 1.5, .45) + '<div style="height:44px"></div>'
            + W("say", "結　果", 2.3, .2) + W("res", result, 2.45, .6))

pages = []
# 01 封面
pages.append(page(1, "#f4efe6",
    W("small", "一虧就想回本的人，一定要看", .1, .5) + '<div style="height:36px"></div>'
    + W("h1", "同一個錯", .55, .7) + '<div class="ul" data-s="1.25" data-d=".35" data-k="x" style="width:560px"></div>'
    + W("h2", "你這週犯了第幾次？", 1.55, .7) + '<div style="height:60px"></div>'
    + W("small", "不信？往左滑，一次一次數給你看", 2.4, .5)
    + f'<div class="w s" data-s="2.95" data-d=".3" data-k="f" style="position:absolute;right:0;bottom:-40px;color:{ACC}">往左滑 →</div>'))
pages.append(page(2, "#f4efe6", story("22:14｜第 1 次", "「停損往下移一點」", "等它彈回來就好。", "沒彈回來，虧更多。")))
pages.append(page(3, "#ece6dc", story("23:40｜第 2 次", "「我一定要賺回來」", "虧完，馬上反手開單。", "又虧一筆。")))
pages.append(page(4, "#e3ded6", story("隔天 01:30｜第 3 次", "「這次不一樣」", "我很有把握。", "跟前兩次，一模一樣。")))
# 05 轉折：「是」被劃掉，改成「不是」
p5 = (W("lab", "隔天 09:05", .15, .35) + "<div></div>"
      + '<div style="position:relative;margin-top:80px">'
      + W("t", f'問題<span style="position:relative;display:inline-block">是<span class="w" data-s="1.15" data-d=".3" data-k="x" style="position:absolute;left:-6px;right:-6px;top:52%;height:9px;background:#d0584a;transform-origin:left center"></span>'
              f'<span class="w" data-s="1.5" data-d=".3" data-k="f" style="position:absolute;left:50%;top:-62px;margin-left:-62px;font-size:56px;color:{ACC}">不是</span></span>行情，', .5, .55).replace('class="w t"', 'class="w t" style="padding-top:80px;margin-top:-80px"', 1)
      + '</div>' + '<div style="height:20px"></div>'
      + W("t", "是你不知道", 2.0, .55) + W("t", "自己在重複。", 2.55, .6)
      + '<div class="ul" data-s="3.2" data-d=".35" data-k="x" style="width:520px"></div>'
      + W("res", "看不見的錯，改不了。", 3.5, .6))
pages.append(page(5, "#f7f2e8", p5))
pages.append(page(6, "#f4efe6",
    W("lab", "每單結束", .15, .35) + "<div></div>" + W("t", "只寫 3 件事", .55, .6)
    + '<div class="ul" data-s="1.15" data-d=".35" data-k="x" style="width:480px"></div>'
    + W("row", "<i>①</i> 為什麼進場？", 1.5, .45) + W("row", "<i>②</i> 有沒有照計畫出場？", 2.0, .55)
    + W("row", "<i>③</i> 下一單改什麼？", 2.6, .45) + '<div style="height:16px"></div>'
    + W("small", "一次只改一件事，改得掉，才算數。", 3.2, .5)))
# 07 小抄（靜態）
pages.append(page(7, "#f4efe6", '''<div class="t" style="font-size:80px;margin-bottom:40px">交易紀錄小抄</div>
<table><colgroup><col style="width:15%"><col style="width:31%"><col style="width:22%"><col style="width:32%"></colgroup>
<tr><th>日期</th><th>為什麼進場</th><th>照計畫？</th><th>下次改什麼</th></tr>
<tr><td>11/12</td><td>突破前高<br>收在上面</td><td style="color:#2f8a5f">✓ 照做</td><td>—</td></tr>
<tr><td>11/13</td><td>感覺要跌了</td><td style="color:#d0584a">✕ 移停損</td><td>停損設好<br>就不動</td></tr>
<tr><td>　</td><td>　</td><td>　</td><td>　</td></tr></table>
<div class="small" style="margin-top:22px">每單結束，花 1 分鐘填一行就好</div>
<div class="res" style="font-size:56px;margin-top:40px">📌 先收藏，今晚收盤就開始寫</div>''', static=True))
pages.append(page(8, "#f4efe6",
    W("lab", "你呢？", .15, .35) + "<div></div>" + W("t", "這週犯了第幾次？", .55, .7)
    + '<div class="ul" data-s="1.25" data-d=".35" data-k="x"></div>'
    + W("s", "留言告訴我，我一個一個看 👇", 1.6, .55) + '<div style="height:50px"></div>'
    + W("res", "📌 先收藏，今晚就開始寫。", 2.3, .65) + '<div style="height:40px"></div>'
    + W("small", "僅供教學參考，非投資建議", 3.0, .4)))

os.makedirs(os.path.join(HERE, "html"), exist_ok=True)
for i, h in enumerate(pages, 1):
    open(os.path.join(HERE, "html", f"p{i:02d}.html"), "w", encoding="utf-8").write(h)
print(len(pages), "pages")
