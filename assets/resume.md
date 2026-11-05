# Xinyao Rao

Autonomous Driving | Foundation Models | Learning & Planning

[744044292@qq.com](mailto:744044292@qq.com) | [github.com/Rtwotwo](https://github.com/Rtwotwo)

## Education

**Nanjing University** | Sep 2026 - Sep 2029 (expected)<br>
*Graduate studies | Autonomous Driving & Foundation Models*<br>
[CITE Lab](https://cite.nju.edu.cn/) | [3D Vision Lab (NJU-3DV)](https://nju-3dv.github.io/)<br>
Advisors: [Xun Cao](https://cite.nju.edu.cn/People/Faculty/20190621/i5054.html) and [Wei Li](https://is.nju.edu.cn/lw/main.htm)

**Northwestern Polytechnical University** | Sep 2022 - Jun 2026<br>
*Undergraduate studies*<br>

## Selected Achievement

**NAVSIM Dual-Leaderboard #1** | As of Nov 5, 2026

Ranked **1st as EABOT.AI**: [NAVTEST v1](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) **96.1906 PDMS**; [NAVHARD v2](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard) **64.5806 EPDMS**.

## Research & Engineering Projects

### DriveTTO | Test-Time Trajectory Optimization

[Project / Results](https://rtwotwo.github.io/DriveTTO/)

- Developed **training-free trajectory optimization** for frozen driving planners, retaining a complete reference plan while exploring endpoint, cross-planner, and bounded control-residual proposals.
- Used **reference-relative selection** to compare candidates; built NAVSIM visualizations and a HUGSIM closed-loop rollout gallery to inspect search decisions and driving behavior.
- Reached **95.6055 PDMS on NAVTEST (#3)** and **58.6340 EPDMS on NAVHARD (#5)** with the official EABOT.AI&NJU entry linked to DriveTTO.

### CoFiDrive | Camera-Based End-to-End Planning

[Code](https://github.com/Rtwotwo/DriveCoFi)

- Extended a DrivoR-based planner with **DINOv2 / LoRA**, six scene-conditioned experts over 64 camera registers, and gated fusion of scene and spatial patch memories for trajectory scoring.
- Added **192 training-only control-space augmentation slots** to expand scorer supervision; kept inference at 64 proposals with no extra learned parameters from augmentation.
- Reported **92.4 PDMS** on NAVSIM-v1 navtest (train85k, 10 epochs, mean of three training seeds); released training, evaluation, ablation configurations, and planning visualizations.

### DriveRSI-R0 | Controlled Policy Improvement

[Code](https://github.com/Rtwotwo/DriveRSI-R0)

- Built **DriveHarness** to connect failure diagnosis, training-experience retrieval, branch generation, sample admission, native model training, and evaluation with explicit budgets and data provenance.
- Integrated model adapters, checkpoint recovery, and promotion / rollback gates with train/test separation and image-object-trajectory consistency checks; documented **191 selected CPU tests** in release verification.

### DriveTraj | NAVSIM Trajectory Planning

[Leaderboard](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest)

- Submitted **DriveTraj-scale (95.5520 PDMS, #6)** and **DriveTraj-base (94.9290 PDMS, #10)** to the official NAVSIM-v1 NAVTEST leaderboard.

## Technical Skills & Open Source

- **Programming & Tools:** Python, PyTorch, NumPy, OpenCV, Git, Linux
- **Modeling:** Vision Transformers, DINOv2, LoRA / adapters, trajectory scoring, reward modeling, PPO / GAE
- **Research Engineering:** NAVSIM evaluation, experiment recovery, data provenance, reproducible ablations

**Open Source:** Curate [AutoDrive Research](https://github.com/Rtwotwo/Awesome-Autonomous-Driving-Research): source-linked papers, code, and evaluation protocols for end-to-end driving, VLA, and world models.

*Official leaderboard ranks checked November 5, 2026.*
