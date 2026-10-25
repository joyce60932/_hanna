const { chromium } = (() => { try { return require('playwright'); } catch { return require('/opt/node-tools/node_modules/playwright'); } })();
const path = require('path');
// 用法：node render-reels.js <資料夾>  → 產出 cover-01.png（上傳用）與 cover-01-grid.png（主頁 3:4 預覽）
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
  console.log('rendered', reels.length);
  await browser.close();
})();
