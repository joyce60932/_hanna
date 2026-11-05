import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "版型"))
from K棒教學 import *

S, N, F = "BISANCOS・Hanna｜K 棒小教室", 8, "BISANCOS・Hanna｜帶你看懂市場"
P = []
pg = lambda i, inner: page(i, N, S, inner, footer=F)

def zig(points, x0=60, step=95, w=44):
    """依序畫一串 K 棒：points = [(開, 收)]，影線自動往外延伸 12。"""
    return "".join(candle(x0 + i*step, o, c, min(o, c)-12, max(o, c)+12, w) for i, (o, c) in enumerate(points))

# 01 封面：一團看不懂的 K 棒
seq = [(200,160),(160,215),(215,175),(175,235),(235,180),(180,150),(150,210),(210,170),(170,230),(230,185),(185,140),(140,200),(200,165),(165,220),(220,190),(190,150)]
mess = "".join(candle(20 + i*55, o, c, min(o, c)-18, max(o, c)+18, 30) for i, (o, c) in enumerate(seq))
P.append(pg(1, f'''<h1 style="font-size:82px">下班才有空看盤<br>打開圖表<br>只看到一堆<br><span class="acc">紅紅綠綠？</span></h1>
<div style="margin-top:50px;opacity:.85">{svg(900,360,mess)}</div>'''))

# 02 共感
P.append(pg(2, '''<h2>晚上 10 點<br>終於有空打開 App</h2>
<p>K 棒密密麻麻，你盯了 10 分鐘。</p>
<p>「現在到底是要漲，還是要跌？」</p>
<p>看不出來，最後關掉 App，<br>跟自己說：明天再看。</p>
<div class="take">有沒有很熟悉？</div>'''))

# 03 後果
P.append(pg(3, '''<h2>隔天，它漲了 8%</h2>
<p>你錯過了。</p>
<p>下次不想再錯過，<br>看到在漲就趕快追。</p>
<p>結果，買在最高點。</p>
<div class="take">不是不努力，是每次都在猜。</div>'''))

# 04 轉折
P.append(pg(4, '''<h2>這不是你<br>不夠聰明</h2>
<p>盤面上的資訊太多了。</p>
<p>你沒有 8 小時可以盯盤，<br>下班後只剩一點點時間，<br>本來就很難靠感覺判斷。</p>
<div class="take">先學會看一件事就好。</div>'''))

# 05 一招：看高點低點
up = zig([(300,240),(250,270),(270,190),(200,225),(220,140),(150,180),(170,90)], x0=60, step=85)
up += dashed(82,228,592,78,UP) + dashed(167,282,507,192,UP)
up += text(630,80,"高點越來越高",30,UP,"start",700) + text(560,250,"低點也越來越高",30,UP,"start",700)
P.append(pg(5, f'''<h2>只看一件事：<br>高點和低點，往哪走？</h2>
<div class="card">{svg(860,330,up)}</div>
<p>高點、低點都一直墊高，<br>就是<b class="up">往上的趨勢</b>。反過來就是往下。</p>
<div class="take">股票、幣、黃金都一樣，這是共通語言。</div>'''))

# 06 小抄
mini_up = svg(170,120, zig([(100,70),(80,90),(90,50),(60,75),(70,25)], x0=5, step=33, w=18))
mini_dn = svg(170,120, zig([(30,60),(50,40),(40,80),(70,55),(60,100)], x0=5, step=33, w=18))
mini_fl = svg(170,120, zig([(50,80),(75,45),(45,80),(78,48),(50,82)], x0=5, step=33, w=18))
P.append(pg(6, f'''<h2>趨勢小抄</h2>
<table>
<tr><th>長相</th><th>怎麼判斷</th><th>新手先這樣做</th></tr>
<tr><td>{mini_up}<b class="up">往上</b></td><td>高點、低點都在墊高</td><td>順著方向，找做多機會</td></tr>
<tr><td>{mini_dn}<b class="down">往下</b></td><td>高點、低點都在變低</td><td>不要急著抄底</td></tr>
<tr><td>{mini_fl}<b>盤整</b></td><td>忽高忽低，沒有方向</td><td>先不要動，等方向出來</td></tr>
</table>
<div class="take">先收藏，看盤時拿出來對。</div>'''))

# 07 想像＋工具
P.append(pg(7, '''<h2 style="font-size:46px;margin-bottom:22px">但每天下班，還要自己畫線、判斷……</h2>
<p style="font-size:34px"><b>如果打開盤面，方向、進場、停損、目標<br>都已經標好了呢？</b></p>
<div style="display:flex;gap:28px;margin-bottom:12px">
 <div style="flex:1"><img src="eth.png" style="width:100%;height:540px;object-fit:cover;object-position:top;border-radius:14px;border:1.5px solid var(--line)"><p style="font-size:26px;margin:10px 0 0" class="up"><b>往上：標出做多＋停損</b></p></div>
 <div style="flex:1"><img src="btc.png" style="width:100%;height:540px;object-fit:cover;object-position:top;border-radius:14px;border:1.5px solid var(--line)"><p style="font-size:26px;margin:10px 0 0" class="down"><b>往下：標出做空＋停損</b></p></div>
</div>
<p style="font-size:32px;margin-top:14px">我們用 AI 把這些判斷，做成了一套工具：3+1 指標。</p>'''))

# 08 收尾
P.append(pg(8, '''<h2>你不需要變成專家<br>才能看懂盤面</h2>
<p>會用工具，一樣看得懂走勢，<br>不再憑感覺亂下單。</p>
<div class="card"><b>工具的領取方式，放在簡介 portal 👆</b></div>
<div class="card"><b>留言告訴我：</b><br>你一天能花多少時間看盤？<br>① 10 分鐘內 ② 30 分鐘 ③ 1 小時以上</div>
<p style="font-size:30px">📌 先收藏，看盤時對照<br>👉 追蹤 @_hannapang，每天一個 K 棒觀念</p>
<p class="note">僅為教學分享，不構成投資建議；指標為輔助工具，仍需自行控管風險</p>'''))

write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.html"), P, "K 棒趨勢")
