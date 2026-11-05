<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=1000&color=6C63FF&center=true&vCenter=true&random=false&width=700&lines=Hi%2C+I%27m+Yolo+Redal;You+can+also+call+me+Rtwotwo;Welcome+to+my+GitHub%21" alt="Typing SVG" />
  <br>
  <img src="https://komarev.com/ghpvc/?username=Rtwotwo&color=6C63FF&style=flat-square&label=Visitors" alt="Visitor count" />
</div>

<!-- BEGIN PROFILE DETAILS -->

# Xinyao Rao

**Autonomous Driving · Foundation Models · Learning & Planning**

Also known as **Yolo Redal / Rtwotwo**.

[![Resume](https://img.shields.io/badge/Resume-English_PDF-087E8B?style=flat-square)](assets/Xinyao_Rao_Resume.pdf)
[![Email](https://img.shields.io/badge/Email-Contact-536575?style=flat-square)](mailto:744044292@qq.com)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Rtwotwo-FFD21E?style=flat-square)](https://huggingface.co/Rtwotwo)
[![Kaggle](https://img.shields.io/badge/Kaggle-yoloredal-20BEFF?style=flat-square)](https://www.kaggle.com/yoloredal)

- I am a graduate student at **[Nanjing University](https://www.nju.edu.cn/)** (Sep 2026 - Sep 2029, expected), affiliated with the **[CITE Lab](https://cite.nju.edu.cn/)** and **[3D Vision Lab (NJU-3DV)](https://nju-3dv.github.io/)**, advised by **[Xun Cao](https://cite.nju.edu.cn/People/Faculty/20190621/i5054.html)** and **[Wei Li](https://is.nju.edu.cn/lw/main.htm)**.
- I completed my undergraduate studies at **[Northwestern Polytechnical University](https://www.nwpu.edu.cn/)** (Sep 2022 - Jun 2026).
- My research centers on **autonomous driving and foundation models**, especially test-time trajectory optimization, camera-based end-to-end planning, and controlled policy improvement. I am also interested in **vision-language-action models and driving world models**.
- **Ranked #1 on both official NAVSIM leaderboards as EABOT.AI:** [NAVTEST v1](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) (**96.1906 PDMS**) and [NAVHARD v2](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard) (**64.5806 EPDMS**), verified November 5, 2026.
- I enjoy building research systems with clear evaluation protocols and inspectable results. For collaboration, reach me at **[744044292@qq.com](mailto:744044292@qq.com)**.

## Selected Research

| Project | Research focus | Public resources |
| :--- | :--- | :--- |
| **[DriveTTO](https://github.com/Rtwotwo/DriveTTO)** | Training-free trajectory optimization with structured search and reference-relative selection using frozen driving models. | [Project page & results](https://rtwotwo.github.io/DriveTTO/), NAVSIM visualizations, HUGSIM rollout gallery. |
| **[CoFiDrive](https://github.com/Rtwotwo/DriveCoFi)** | Scene-conditioned camera registers, dual-memory trajectory scoring, and training-only control-space augmentation for end-to-end driving. | Training, evaluation, ablation configurations, and visualization code. |
| **[DriveRSI-R0](https://github.com/Rtwotwo/DriveRSI-R0)** | A research platform linking failure diagnosis, experience retrieval, consistent branch generation, native training, and evaluation gates. | Source snapshot, model adapters, DriveHarness, and CPU verification tests. |
| **[DriveTraj](https://github.com/Rtwotwo/DriveTraj)** | Trajectory-planning research with base and scale entries on the official NAVSIM leaderboard. | Official benchmark entries; method documentation and implementation are not yet in the public repository. |

### Official Benchmark Results

Public leaderboard snapshot checked on **November 5, 2026**. Rankings may change.

| Linked project / entry | Benchmark | Score | Current rank |
| :--- | :--- | ---: | ---: |
| **EABOT.AI** · Xinyao Rao | [NAVSIM v1 NAVTEST](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) | **96.1906 PDMS** | **1** |
| **EABOT.AI** · Xinyao Rao | [NAVSIM v2 NAVHARD](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard) | **64.5806 EPDMS** | **1** |
| **DriveTTO** · EABOT.AI&NJU | [NAVSIM v1 NAVTEST](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) | **95.6055 PDMS** | **3** |
| **DriveTTO** · EABOT.AI&NJU | [NAVSIM v2 NAVHARD](https://huggingface.co/spaces/AGC2025/e2e-driving-navhard) | **58.6340 EPDMS** | **5** |
| **DriveTraj-scale** | [NAVSIM v1 NAVTEST](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) | **95.5520 PDMS** | **6** |
| **DriveTraj-base** | [NAVSIM v1 NAVTEST](https://huggingface.co/spaces/AGC2024-P/e2e-driving-navtest) | **94.9290 PDMS** | **10** |

I submit under **EABOT.AI**. The separate **EABOT.AI&NJU** entries link to DriveTTO, and the DriveTraj entries link to its repository. CoFiDrive additionally reports **92.4 PDMS** on NAVSIM-v1 navtest with train85k, 10 training epochs, and a three-seed mean; see its [experiment settings](https://github.com/Rtwotwo/DriveCoFi/blob/main/docs/experiments.md).

<details>
<summary><b>More projects & research resources</b></summary>

- **[FF3DR](https://github.com/Rtwotwo/FF3DR)** — LoRA adaptation of Depth Anything 3 and long-sequence aerial 3D reconstruction.
- **[Visual-Locator](https://github.com/Rtwotwo/Visual-Locator)** — UAV visual localization through image retrieval, local matching, and geographic coordinate conversion.
- **[OSTrack](https://github.com/Rtwotwo/OSTrack)** — Infrared UAV detection and tracking practice with desktop video demonstrations.
- **[TinyRM](https://github.com/Rtwotwo/TinyRM)** — A grid-navigation demo of reward learning, PPO, and held-out policy acceptance.
- **[Awesome Autonomous Driving Research](https://github.com/Rtwotwo/Awesome-Autonomous-Driving-Research)** — Source-linked papers, datasets, code, and evaluation protocols for end-to-end driving, VLA, and world models.

</details>

<sub>Upstream models, licenses, implementation scope, and release status are documented in each repository.</sub>

## Resume

**[View / download my English resume (PDF)](assets/Xinyao_Rao_Resume.pdf)** · [Markdown version](assets/Xinyao_Rao_Resume.md) · [HTML file](assets/Xinyao_Rao_Resume.html)

<sub>Target roles: Autonomous Driving / Foundation Model Algorithms. Download the HTML file to view or print it in a browser.</sub>

## Tools & Activity

<!-- END PROFILE DETAILS -->

<p align="center">
  <img src="https://skillicons.dev/icons?i=vscode,git,github,docker,linux,python&perline=6" alt="Tools & Languages" />
</p>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Rtwotwo/Rtwotwo/output/github-contribution-grid-snake-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Rtwotwo/Rtwotwo/output/github-contribution-grid-snake.svg">
    <img alt="GitHub contribution grid snake animation" src="https://raw.githubusercontent.com/Rtwotwo/Rtwotwo/output/github-contribution-grid-snake.svg">
  </picture>
</div>
