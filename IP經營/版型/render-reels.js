const { chromium } = (() => { try { return require('playwright'); } catch { return require('/opt/node-tools/node_modules/playwright'); } })();
const path = require('path');
// 用法：node render-reels.js <資料夾>  → 產出 cover-01.png（上傳用）與 cover-01-grid.png（主頁 3:4 預覽），多張時再加 grid.png（主頁整排預覽）
(async () => {
  const dir = process.argv[2];
  const browser = await chromium.launch(require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {});
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto('file://' + path.join(dir, 'cover.html'), { waitUntil: 'networkidle' });
  await page.waitForSelector('body[data-ready="1"]', { timeout: 60000 });
  const reels = await page.$$('.reel');
  for (let i = 0; i < reels.length; i++) {
    const n = String(i + 1).padStart(2, '0');
    await reels[i].screenshot({ path: path.join(dir, `cover-${n}.png`) });
    const box = await reels[i].boundingBox();
    await page.screenshot({ path: path.join(dir, `cover-${n}-grid.png`), clip: { x: box.x, y: box.y + 240, width: 1080, height: 1440 } });
  }
  // 多張時另外輸出 grid.png：模擬 IG 主頁一排 3 格的樣子
  if (reels.length > 1) {
    const files = reels.map((_, i) => 'file://' + path.join(dir, `cover-${String(i + 1).padStart(2, '0')}-grid.png`));
    await page.setViewportSize({ width: 1080, height: 1440 });
    await page.setContent(`<body style="margin:0;background:#fff;display:grid;grid-template-columns:repeat(3,358px);gap:3px">${files.map(f => `<img src="${f}" style="width:358px;height:477px;object-fit:cover">`).join('')}</body>`);
    await page.waitForLoadState('networkidle');
    const rows = Math.ceil(reels.length / 3);
    await page.screenshot({ path: path.join(dir, 'grid.png'), clip: { x: 0, y: 0, width: 1080, height: rows * 480 - 3 } });
  }
  console.log('rendered', reels.length);
  await browser.close();
})();
