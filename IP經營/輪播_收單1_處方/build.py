import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "版型"))
import importlib.util
spec = importlib.util.spec_from_file_location("t", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "版型", "米色教學圖卡.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
N, L = 7, "交易日常"
P = []
lines = "".join(f'<rect x="60" y="{60+i*58}" width="{360 if i%2 else 300}" height="10" rx="5" fill="#ddd2c1"/>' for i in range(5))
note = (f'<svg width="900" height="330" viewBox="0 0 900 330"><rect x="20" y="20" width="560" height="300" rx="22" fill="#fbf8f2" stroke="#ddd2c1" stroke-width="3"/>{lines}'
        f'<g font-family="Noto Serif TC" font-weight="900" font-size="46" fill="#a8763e"><text x="640" y="100">① 為什麼進</text><text x="640" y="190">② 照計畫嗎</text><text x="640" y="280">③ 下次改</text></g></svg>')
P.append(t.page(1, N, L, f'<div class="kicker">一虧就想回本的人，一定要看</div><h1>同一個錯<br><span class="acc">一直犯？</span></h1><div class="sub">每單結束，只寫 3 件事</div><div style="margin-top:60px">{note}</div>'))
P.append(t.page(2, N, L, '''<h2>你以為是運氣不好<br>其實是同一個錯</h2>
<div class="row"><span class="mk down">✕</span><span>停損到了，又往下移一點</span></div>
<div class="row"><span class="mk down">✕</span><span>一虧就馬上反手，想賺回來</span></div>
<div class="row"><span class="mk down">✕</span><span>看到在漲，沒想清楚就追</span></div>
<p style="margin-top:20px">沒寫下來，大腦只會記得<br>「下次一定會漲」。</p>
<div class="take">看不見的錯，改不了。</div>'''))
P.append(t.page(3, N, L, '''<div class="num">1</div><h2>為什麼進場？</h2>
<p>能不能用<b>一句話</b>寫出來？</p>
<div class="card"><span class="up"><b>✓</b></span>　突破前一天高點，收在上面<br><span class="down"><b>✕</b></span>　感覺要漲了<br><span class="down"><b>✕</b></span>　群組說會漲</div>
<div class="take">寫不出理由的單，<br>就是衝動單。</div>'''))
P.append(t.page(4, N, L, '''<div class="num">2</div><h2>有沒有照計畫出場？</h2>
<div class="row"><span class="mk acc">□</span><span>停損有沒有往下移？</span></div>
<div class="row"><span class="mk acc">□</span><span>是不是一有獲利就提早跑？</span></div>
<div class="row"><span class="mk acc">□</span><span>虧了是不是還抱著不放？</span></div>
<div class="take">這一單賺或虧不重要，<br>有沒有照計畫才重要。</div>'''))
P.append(t.page(5, N, L, '''<div class="num">3</div><h2>下一單要改什麼？</h2>
<p>只寫<b>一件</b>就好，寫多了做不到。</p>
<div class="card">例：下一單，停損設好就不動。<br>例：虧完先停 30 分鐘，不反手。</div>
<div class="take">一次只改一件事，<br>改得掉，才算數。</div>'''))
P.append(t.page(6, N, L, '''<h2>交易紀錄小抄</h2>
<table><colgroup><col style="width:15%"><col style="width:31%"><col style="width:22%"><col style="width:32%"></colgroup><tr><th>日期</th><th>為什麼進場</th><th>照計畫？</th><th>下次改什麼</th></tr>
<tr><td>11/12</td><td>突破前高<br>收在上面</td><td class="up">✓ 照做</td><td>—</td></tr>
<tr><td>11/13</td><td>感覺要跌了</td><td class="down">✕ 移停損</td><td>停損設好<br>就不動</td></tr>
<tr><td>　</td><td>　</td><td>　</td><td>　</td></tr></table>
<p class="note">每單結束，花 1 分鐘填一行就好</p>
<div class="take">📌 先收藏，今晚收盤就開始寫。</div>'''))
P.append(t.page(7, N, L, '''<h2>寫 7 天，你會看到<br>自己最常犯的那個錯</h2>
<p>怎麼從紀錄找出錯誤模式、<br>怎麼搭配 <b class="acc">3+1 指標</b>判斷進場，<br>新手班第一週就會練。</p>
<div class="cta">想學，看置頂留言 👆</div>
<p class="note" style="margin-top:40px">你最常犯的是哪一個？留言告訴我<br>僅供教學參考，非投資建議</p>'''))
t.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.html"), P, "收單 1｜處方篇")
