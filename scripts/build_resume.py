"""Generate the English resume HTML and Markdown with Python's standard library.
Run: python scripts/build_resume.py. Print the HTML at A4/100% without headers.
"""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PROJECTS=[
('DriveSTA','Learning from Scored Trajectory Alternatives for End-to-End Driving',
 'First author · arXiv:2611.27515 · 2026','https://arxiv.org/abs/2611.27515','https://github.com/Rtwotwo/DriveSTA',[
'<b>Richer supervision.</b> Constructed scored alternatives beyond one human demonstration through smooth deformations, execution evaluation, and diversity screening: <b>2.61M targets across 95,998 real scenes</b>.',
'<b>Temporal planning.</b> Combined autoregressive proposals, Hungarian matching, and multi-target residual diffusion; shared <b>JEPA video features</b> between refinement and rescoring, avoiding online VLM inference.',
'<b>Quality and efficiency.</b> Scale achieved <b>95.55 NAVTEST PDMS</b> and <b>46.7 HUGSIM HD-Score</b> (345 episodes). Mean forward latency fell <b>73% (1,295 to 349 ms)</b> versus ChainFlow-VLA in matched H20, batch-1 evaluation.']),
('DriveTTO','Search and Selection in Test-Time Trajectory Optimization',
 'First author · Manuscript · 2026','https://rtwotwo.github.io/DriveTTO/','https://github.com/Rtwotwo/DriveTTO',[
'<b>Training-free search.</b> Coupled proposal-supported endpoint search with bounded refinement and time-aligned fusion of proposal and control branches, keeping <b>all planners and scorers frozen</b>.',
'<b>Reliable selection.</b> Required both scorers to predict reference-relative gains before branch/fusion updates. Recovered <b>51.35% of native zero-PDMS cases</b> on average; net zero-score rate fell from <b>1.63% to 1.13%</b>.',
'<b>Generalization.</b> Reached <b>95.54 PDMS / 92.30 EPDMS</b> on NAVTEST and <b>57.10 EPDMS</b> on NAVHARD under benchmark-specific configurations. The single-scorer variant improved <b>all six evaluated planners</b> on both splits.']),
('Spark-H3','Adaptive Block Sparse Attention for Video Diffusion Models',
 'Co-author (4th author) · arXiv:2611.24256 · 2026','https://arxiv.org/abs/2611.24256',None,[
'<b>Adaptive grouping.</b> Co-authored a training-free attention method. <b>Spark-Reblock</b> recursively groups tokens by attention preference into regular tiles, combining adaptive sparsity with GPU-friendly block structure.',
'<b>Attention calibration.</b> <b>Spark-Reweight</b> uses a global query anchor to build weighted KV representatives and logit biases; exact and compressed branches share normalization to preserve attention mass.',
'<b>Measured acceleration.</b> Achieved <b>2.49× DiT speedup</b> with <b>24.81 dB PSNR</b> versus dense outputs on MiniMax-H3 at 10% exact-block density (20 steps, 345 frames, 1344×768; 4 dense warm-up steps).'])]
STYLE='''
:root{color-scheme:light;--ink:#17212b;--muted:#586572;--accent:#245782}*{box-sizing:border-box}body{margin:0;background:#edf0f3;color:var(--ink);font:10pt/1.37 Arial,"Microsoft YaHei",sans-serif}a{color:inherit;text-decoration:none}a:hover{text-decoration:underline}a:focus-visible,button:focus-visible{outline:2px solid #216c85;outline-offset:3px}.toolbar{max-width:210mm;margin:18px auto 12px;padding:0 15px;display:flex;justify-content:space-between;gap:12px;align-items:center;font:14px Arial,sans-serif}.actions{display:flex;gap:8px}.toolbar a,.toolbar button{font:inherit;border:1px solid #c3cdd4;border-radius:4px;background:white;color:var(--ink);padding:8px 12px;cursor:pointer}.sheet{width:210mm;min-height:297mm;margin:0 auto 30px;background:white;padding:12mm 14mm 10mm;box-shadow:0 6px 30px #00000012}.header{display:flex;justify-content:space-between;gap:20px;align-items:baseline}h1{font-size:26pt;line-height:1.1;margin:0 0 6pt;letter-spacing:.2pt}.target{color:var(--accent);font-size:10pt;text-align:right;font-weight:600}.contact{display:flex;flex-wrap:wrap;gap:4pt 12pt;font-size:9pt;margin:3pt 0}.contact a{color:#344a5a}.summary{color:#465a6e;font-size:9.5pt;line-height:1.45;margin:7pt 0 0;padding:5pt 8pt;background:#f3f6fa;border-left:2pt solid #7c9dbc}h2{font-size:11pt;letter-spacing:.2pt;color:var(--accent);margin:9pt 0 5pt;padding:3pt 7pt;background:#eaf0f7;border-left:2pt solid #537da3;border-bottom:0}h3{font-size:10pt;line-height:1.4;margin:0;font-weight:700}.row{display:flex;justify-content:space-between;align-items:baseline;gap:12pt}.date{font-size:9pt;color:var(--muted);white-space:nowrap}.school-note{font-size:9pt;color:var(--muted);margin:3pt 0 4pt}p{margin:3pt 0}.intern-note{font-size:9.5pt}.entry{margin-top:8pt;break-inside:avoid}.entry:first-of-type{margin-top:0}.project-name{display:inline-block;color:#214e78;background:#e8f0f9;border:0;border-radius:3pt;padding:1pt 5pt;margin-right:2pt;white-space:nowrap}.meta{font-size:8.7pt;color:var(--muted);margin:2pt 0 4pt}.meta a{color:#28536b;text-decoration:underline;text-underline-offset:2px}.entry ul{padding-left:12pt;margin:3pt 0 0}.entry li{padding-left:1pt;margin:0 0 3pt}.skills p{font-size:9.5pt;margin:3pt 0}b{font-weight:700}section{break-inside:avoid}.research{break-inside:auto}
@page{size:A4;margin:0}@media print{*{-webkit-print-color-adjust:exact;print-color-adjust:exact}body{background:white}.toolbar{display:none}.sheet{width:210mm;min-height:0;margin:0;box-shadow:none}a{color:inherit}}
@media(max-width:700px){body{font-size:11pt;line-height:1.5}.sheet{width:100%;min-height:0;margin:0;padding:25px 22px}.header{display:block}.target{text-align:left;margin:0 0 10px}.row{flex-wrap:wrap;gap:2pt 10pt}.toolbar>span{display:none}.toolbar{margin:12px 0}.entry li{margin-bottom:7pt}.summary{font-size:10pt}.date{font-size:9.5pt}}
'''
projects=''
for name,title,status,url,code,bullets in PROJECTS:
    label='Project' if name=='DriveTTO' else 'Paper'
    links=f'<a href="{url}">{label}</a>'+(f' · <a href="{code}">Code</a>' if code else '')
    projects+=f'<article class="entry"><h3><span class="project-name">{name}</span> | {title}</h3><p class="meta">{status} · {links}</p><ul>'+''.join(f'<li>{b}</li>' for b in bullets)+'</ul></article>'
body=f'''<header><div class="header"><h1>Xinyao Rao</h1><div class="target">Algorithm Engineering<br>Foundation Models · Autonomous Driving</div></div>
<div class="contact"><a href="tel:+8619829265306">+86 198 2926 5306</a><a href="mailto:744044292@qq.com">744044292@qq.com</a><a href="https://github.com/Rtwotwo">github.com/Rtwotwo</a><a href="https://scholar.google.com/citations?user=zRt1tLAAAAAJ&amp;hl=en">Google Scholar</a></div>
<p class="summary">Research interests: World Models · Foundation Models · Vision-Language Models<br>Autonomous Driving · Pre-/Mid-/Post-training</p></header>
<section><h2>EDUCATION</h2><div class="row"><h3>Nanjing University | Master’s studies</h3><span class="date">Sep 2026 - Sep 2029 (expected)</span></div><p class="school-note">CITE Lab / NJU-3DV · Advisors: Xun Cao and Wei Li</p><div class="row"><h3>Northwestern Polytechnical University | Undergraduate studies</h3><span class="date">Sep 2022 - Jun 2026</span></div></section>
<section><h2>EXPERIENCE</h2><div class="row"><h3>EABOT | Intern</h3><span class="date">Jul 2026 - present · Ends Jan 2027 (expected)</span></div><p class="intern-note">Research focus: autonomous driving and trajectory planning.</p></section>
<section class="research"><h2>RESEARCH CONTRIBUTIONS</h2>{projects}</section>
<section class="skills"><h2>TECHNICAL SKILLS</h2><p><b>Tools:</b> Python, PyTorch, NumPy, OpenCV, Linux, Git.</p><p><b>Modeling & evaluation:</b> Vision Transformers, DINOv2/LoRA, JEPA, diffusion models, trajectory scoring, NAVSIM/HUGSIM, reproducible ablations, and experiment recovery.</p></section>'''
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Xinyao Rao — Algorithm Engineering Resume"><title>Xinyao Rao | Algorithm Engineering Resume</title><style>{STYLE}</style></head><body><nav class="toolbar" aria-label="Resume actions"><span>Xinyao Rao / Résumé</span><div class="actions"><a href="../index.html">Homepage</a><a href="cv.pdf" download>Download PDF</a><button type="button" onclick="window.print()">Print</button></div></nav><main class="sheet">{body}</main></body></html>'''
(ROOT/'assets/resume.html').write_text(html,encoding='utf-8')
md='''# Xinyao Rao

**Algorithm Engineering | Foundation Models · Autonomous Driving**

+86 198 2926 5306 · 744044292@qq.com · [GitHub](https://github.com/Rtwotwo) · [Google Scholar](https://scholar.google.com/citations?user=zRt1tLAAAAAJ&hl=en)

Research interests: World Models, Foundation Models, Vision-Language Models, Autonomous Driving, and Pre-/Mid-/Post-training.

## Education

**Nanjing University | Master’s studies** · Sep 2026 - Sep 2029 (expected)<br>
CITE Lab / NJU-3DV · Advisors: Xun Cao and Wei Li

**Northwestern Polytechnical University | Undergraduate studies** · Sep 2022 - Jun 2026

## Experience

**EABOT | Intern** · Jul 2026 - present; planned end Jan 2027<br>
Research focus: autonomous driving and trajectory planning.

## Research Contributions
'''
for name,title,status,url,code,bullets in PROJECTS:
    label='Project' if name=='DriveTTO' else 'Paper'
    md+=f'\n### {name} | {title}\n\n{status} · [{label}]({url})'+(f' · [Code]({code})' if code else '')+'\n\n'
    md+=''.join('- '+b.replace('<b>','**').replace('</b>','**')+'\n' for b in bullets)
md+='\n## Technical Skills\n\n- **Tools:** Python, PyTorch, NumPy, OpenCV, Linux, Git.\n- **Modeling & evaluation:** Vision Transformers, DINOv2/LoRA, JEPA, diffusion models, trajectory scoring, NAVSIM/HUGSIM, reproducible ablations, experiment recovery.\n'
(ROOT/'assets/resume.md').write_text(md.replace('  \n', '<br>\n'),encoding='utf-8')
print('Generated English resume.html and resume.md')
