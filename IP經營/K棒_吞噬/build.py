import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "版型"))
from K棒教學 import *

S, N = "HANNA｜K 棒小教室", 8
P = []

# 01 封面：跌勢 4 根，最後一根大陽線吞噬
cov = "".join([candle(60,120,190,100,210), candle(170,180,250,165,270), candle(280,240,300,225,320),
               candle(390,290,330,280,350), candle(500,345,180,170,360, w=72)])
cov += text(620,200,"這根大陽線，",34,ACC,weight=700) + text(620,246,"把前一根",34,ACC,weight=700) + text(620,292,"整個吃掉",34,ACC,weight=700)
P.append(page(1,N,S,f'''<div class="kicker">想用交易替自己加薪？</div>
<h1>看到這<span class="acc">2根</span>K棒<br>趨勢可能<br>要反轉了</h1>
<div style="margin-top:60px">{svg(900,400,cov)}</div>
<p class="note">國中生都看得懂的「吞噬」型態</p>'''))

# 02 什麼是吞噬
d = candle(230,140,200,120,220) + candle(420,240,90,70,260,w=80)
d += dashed(200,140,540,140) + dashed(200,200,540,200)
d += text(258,320,"第 1 根",28,SOFT,"middle") + text(460,320,"第 2 根",28,SOFT,"middle")
d += text(600,150,"第 2 根的「身體」",30,INK) + text(600,192,"從上到下，",30,INK) + text(600,234,"把第 1 根整個包住",30,ACC,weight=700)
P.append(page(2,N,S,f'''<h2>什麼是「吞噬」？</h2>
<p>兩根 K 棒，<br>第 2 根的實體（身體），<br>把第 1 根的實體<b>整個包住</b>。</p>
<div class="card">{svg(860,340,d)}</div>
<div class="take">大的吃掉小的，力量換人了。</div>'''))

# 03 多頭吞噬
u = "".join([candle(40,60,110,45,125), candle(140,100,150,90,165), candle(240,145,190,130,205),
             candle(340,185,215,175,230), candle(440,225,120,105,240,w=72)])
u += text(476,290,"陽包陰",30,UP,"middle",700) + text(600,120,"跌了好幾天，",30,INK) + text(600,162,"買方突然反撲",30,INK)
P.append(page(3,N,S,f'''<h2><span class="up">多頭吞噬</span><br>跌到一半，買方反撲</h2>
<div class="card">{svg(860,310,u)}</div>
<p>出現在<b>一路下跌</b>之後：<br>小陰線，接著一根大陽線把它吃掉。</p>
<div class="take">可能是止跌、準備往上的訊號。</div>'''))

# 04 空頭吞噬
dn = "".join([candle(40,240,190,255,175), candle(140,200,150,215,135), candle(240,160,115,175,100),
              candle(340,120,90,130,80), candle(440,80,195,65,210,w=72)])
dn += text(476,260,"陰包陽",30,DOWN,"middle",700) + text(600,150,"漲了好幾天，",30,INK) + text(600,192,"賣方突然出手",30,INK)
P.append(page(4,N,S,f'''<h2><span class="down">空頭吞噬</span><br>漲到一半，賣方出手</h2>
<div class="card">{svg(860,290,dn)}</div>
<p>出現在<b>一路上漲</b>之後：<br>小陽線，接著一根大陰線把它吃掉。</p>
<div class="take">可能是漲不動、準備往下的訊號。</div>'''))

# 05 小抄
mu = svg(150,150, candle(25,40,90,25,105,w=34)+candle(80,100,20,10,120,w=44))
md = svg(150,150, candle(25,110,60,120,45,w=34)+candle(80,50,130,35,140,w=44))
P.append(page(5,N,S,f'''<h2>吞噬型態小抄</h2>
<table>
<tr><th></th><th class="up">多頭吞噬</th><th class="down">空頭吞噬</th></tr>
<tr><td>長相</td><td>{mu}</td><td>{md}</td></tr>
<tr><td>出現在</td><td>下跌之後</td><td>上漲之後</td></tr>
<tr><td>組合</td><td>小陰線 → 大陽線</td><td>小陽線 → 大陰線</td></tr>
<tr><td>代表</td><td>買方接手</td><td>賣方接手</td></tr>
<tr><td>停損</td><td>第 2 根最低點下方</td><td>第 2 根最高點上方</td></tr>
</table>
<div class="take">先收藏，看盤時拿出來對。</div>'''))

# 06 怎麼判斷準不準
P.append(page(6,N,S,f'''<h2>不是每次都準<br>先看這 4 件事</h2>
<div class="row"><span class="num">1</span><div>前面有明顯的漲或跌<small>盤整時出現，參考價值低</small></div></div>
<div class="row"><span class="num">2</span><div>第 2 根越大，越有力<small>包得越多，換手越明顯</small></div></div>
<div class="row"><span class="num">3</span><div>成交量有放大<small>有人真的在買賣，不是隨便晃一下</small></div></div>
<div class="row"><span class="num">4</span><div>隔天有沒有接著走<small>等一根確認，比急著進場安全</small></div></div>
<div class="take">型態是線索，不是保證。</div>'''))

# 07 新手常犯錯＋停損位置
sl = "".join([candle(80,60,110,45,125), candle(180,100,150,90,165), candle(280,145,185,130,200),
              candle(380,195,90,75,215,w=72)])
sl += dashed(40,240,820,240,DOWN) + text(470,280,"停損：第 2 根最低點下方",30,DOWN,"start",700)
P.append(page(7,N,S,f'''<h2>新手最常犯的錯</h2>
<p>✕ 只看型態，不看前面在漲還是在跌<br>✕ 一看到就重押<br>✕ 進場了，卻沒想好錯了怎麼辦</p>
<div class="card">{svg(860,300,sl)}</div>
<div class="take">進場前，先決定停損放哪裡。</div>'''))

# 08 結尾
P.append(page(8,N,S,f'''<h2>記住一句話就好</h2>
<p class="serif" style="font-size:44px;font-weight:900;line-height:1.6">大的 K 棒吃掉小的，<br>代表力量換人了。</p>
<div class="card"><b>留言告訴我：</b><br>你看盤時有注意過吞噬嗎？<br>① 有，常看到 ② 沒注意過 ③ 今天才知道</div>
<p>📌 先收藏，下次看盤時對照<br>👉 追蹤 @_hannapang，每天一個 K 棒觀念<br>📚 想從頭學會看盤？個人簡介有完整課程</p>
<p class="note">僅為教學分享，不構成投資建議</p>'''))

write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.html"), P, "K 棒吞噬")
