const { chromium } = (() => { try { return require('playwright'); } catch { return require('/opt/node-tools/node_modules/playwright'); } })();
const path = require('path');
(async () => {
  const dir = process.argv[2];
  const browser = await chromium.launch(require('fs').existsSync('/opt/pw-browsers/chromium') ? { executablePath: '/opt/pw-browsers/chromium' } : {});
  const page = await browser.newPage({ viewport: { width: 1080, height: 1400 } });
  await page.goto('file://' + path.join(dir, 'slides.html'), { waitUntil: 'networkidle' });
  await page.waitForSelector('body[data-ready="1"]', { timeout: 60000 });
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++) {
    const over = await slides[i].evaluate(s => { const b = s.querySelector('.body'); return b ? b.scrollHeight > s.clientHeight - 320 : false; });
    await slides[i].screenshot({ path: path.join(dir, String(i + 1).padStart(2, '0') + '.png') });
    if (over) console.log('overflow on slide', i + 1);
  }
  console.log('rendered', slides.length);
  await browser.close();
})();
