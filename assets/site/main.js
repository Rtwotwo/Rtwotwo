(() => {
  'use strict';
  const root = document.documentElement;
  const languageButtons = [...document.querySelectorAll('[data-language]')];
  const filterButtons = [...document.querySelectorAll('[data-filter]')];
  const papers = [...document.querySelectorAll('.paper[data-topic]')];
  const status = document.querySelector('#filter-status');
  let activeFilter = 'all';
  function announce() {
    const count = papers.filter(paper => !paper.hidden).length;
    status.textContent = root.lang === 'zh-CN' ? `显示 ${count} 项研究成果` : `Showing ${count} research works`;
  }
  function setLanguage(language) {
    if (!['en', 'zh-CN'].includes(language)) language = 'en';
    root.lang = language;
    languageButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.language === language)));
    document.title = language === 'zh-CN' ? '饶欣瑶 | 南京大学 · 世界模型与自动驾驶' : 'Xinyao Rao | World Models & Autonomous Driving';
    try { localStorage.setItem('xinyao-language', language); } catch (_) { /* Storage is optional. */ }
    announce();
  }
  languageButtons.forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language)));
  filterButtons.forEach(button => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter;
    filterButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    papers.forEach(paper => { paper.hidden = activeFilter !== 'all' && paper.dataset.topic !== activeFilter; });
    announce();
  }));
  document.querySelectorAll('.copy-citation').forEach(button => button.addEventListener('click', async () => {
    const citation = document.getElementById(button.dataset.copy).textContent;
    try {
      await navigator.clipboard.writeText(citation);
      button.textContent = root.lang === 'zh-CN' ? '已复制' : 'Copied';
    } catch (_) {
      const range = document.createRange();
      range.selectNodeContents(document.getElementById(button.dataset.copy));
      const selection = window.getSelection(); selection.removeAllRanges(); selection.addRange(range);
      button.textContent = root.lang === 'zh-CN' ? '已选中，请手动复制' : 'Selected — copy manually';
    }
  }));
  let language = 'en';
  try { language = localStorage.getItem('xinyao-language') || 'en'; } catch (_) { /* Use English without storage. */ }
  setLanguage(language);
  document.querySelectorAll('[data-enhanced]').forEach(element => { element.hidden = false; });
})();
