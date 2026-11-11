import os
import importlib.util
spec = importlib.util.spec_from_file_location("t", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "版型", "米色教學圖卡.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
N, L = 7, "新手 Q&A"
P = []
chips = "".join(f'<span style="display:inline-block;border:2px solid #ddd2c1;background:#fbf8f2;border-radius:40px;padding:14px 30px;margin:0 16px 18px 0;font-size:38px">{s}</span>' for s in ["沒時間盯盤", "看不懂 K 線", "怕被騙", "參加條件", "怕虧損"])
P.append(t.page(1, N, L, f'<div class="kicker">想學很久，卻一直沒開始的你</div><h1>想學交易<br><span class="acc">一直沒開始？</span></h1><div class="sub">新手最常卡住的 5 件事</div><div style="margin-top:60px">{chips}</div>'))
QA = [
    ("我上班很忙，<br>沒時間盯盤", "新手陪跑每天 10 分鐘，<br>下班後就能練。<br>先學會看重點，不用一直盯著。", "缺的不是時間，是學習順序。"),
    ("我完全看不懂 K 線", "從一根 K 棒開始教。<br>看不懂也沒關係，工具會把方向、<br>進場和停損標在盤面上。", "看不懂，就從第一根開始。"),
    ("這會不會是詐騙？", "4 年 200+ 梯次新手班，<br>線下課程、路人教學、新聞採訪<br>都放在主頁，你可以先看。<br>不喊單、不帶單，也不碰你的帳戶。", "先看證據，再做決定。"),
    ("參加要什麼條件？", "課程有合作平台支持，<br>符合審核條件就能參加。<br>細節加 LINE@，我一個一個說明。", "條件先問清楚，再開始。"),
    ("我怕虧損", "新手班第一件事就是風控：<br>先學會停損和倉位，<br>再談什麼時候進場。", "先學會活下來，再談其他。"),
]
for k, (q, a, take) in enumerate(QA, 1):
    P.append(t.page(k + 1, N, L, f'<div class="num">{k}</div><div class="quote">「{q}」</div><p>{a}</p><div class="take">{take}</div>'))
P.append(t.page(7, N, L, '''<h2>你卡在哪一個？</h2>
<p>留言數字 1～5，<br>我會一個一個回你。</p>
<div class="card">想從第一步開始：<br><b>看主頁連結 → 加 LINE@</b><br>回「想了解」，我本人回覆你 🙌</div>
<div class="take">📌 先收藏，哪天想開始了，再打開這篇。</div>
<p class="note">僅供教學參考，非投資建議</p>'''))
t.write(os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides.html"), P, "收單 1｜抗拒篇")
