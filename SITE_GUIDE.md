# 个人学术主页使用说明

本仓库同时保留 GitHub 个人资料 README 与纯静态学术主页，无需 npm 安装或前端构建。

## 本地查看

直接打开 `index.html`，或在仓库根目录执行 `python -m http.server 8080`，访问 `http://localhost:8080`。中英文切换、研究分类、BibTeX 展开和复制均可使用；没有 JavaScript 时仍可阅读全部英文内容。

## 发布到 GitHub Pages

当前 Git remote 是 `Rtwotwo/Rtwotwo`。启用后的默认地址为 **https://rtwotwo.github.io/Rtwotwo/**。

1. 提交并推送本次文件到 `main`。
2. 在 GitHub 仓库的 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
3. 在 Actions 中运行 **Deploy academic homepage**。以后主页、样式或简历文件的变更推送到 `main` 后将自动部署。

原有贡献图动画 workflow 保持独立，Pages 部署只打包主页、配图与简历，不包含本地备份、脚本、阅读笔记或 Git 元数据。

如果要使用不带 `/Rtwotwo/` 的地址 `https://rtwotwo.github.io/`，应另建或使用 `Rtwotwo/rtwotwo.github.io` 仓库。请保留当前 `Rtwotwo/Rtwotwo`，它用于 GitHub 个人资料展示。将网站文件复制到根域名仓库、开启同一 Pages workflow，并修改 README 的主页地址即可；页面资源均使用相对路径。

## 日常维护

- `index.html`：个人介绍、动态、论文、项目、教育信息。中英文本分别标有 `lang="en"` 和 `lang="zh-CN"`。
- `assets/site/style.css`：页面视觉样式、移动端与打印样式。
- `assets/site/main.js`：语言切换、研究分类与引用复制。
- `README.md`：GitHub 个人资料自我介绍。
- `assets/cv.pdf`：英文单页投递版。
- `assets/resume.html`：可在线阅读、打印的简历。
- `scripts/build_resume.py`：简历内容的单一维护入口，生成 HTML 与 Markdown。运行后需从 HTML 重新导出 PDF（A4、100% 比例、关闭浏览器页眉页脚）。

提交前执行：

```sh
python scripts/check_site.py
node --check assets/site/main.js
```

## 素材与内容来源

头像使用本人提供的照片；DriveSTA 配图取自本人项目仓库。Spark-H3 与 DriveTTO 缩略图截取自原始论文中的方法图/概览图。论文作者、状态与链接见 arXiv 页面；DriveTTO 使用本人提供的论文稿件核对贡献与作者，仅展示论文介绍和项目链接，不上传稿件 PDF；正式 arXiv 链接为 https://arxiv.org/abs/2611.29205。

设计与简历取舍、论文指标定位见 `RESUME_NOTES.md`。原简历备份位于本地 `.local-backups/`，不参与 Git 追踪和 Pages 发布。

## 设计参考

参考 [Jon Barron](https://jonbarron.info/) 的横向论文条目、完整作者和独立资源链接，参考 [Yang Song](https://yang-song.net/) 的简洁个人介绍与精选成果层级。版式和代码重新实现；按照用户最终选择，背景使用纯白，采用大留白、统一无衬线字体、克制的蓝色链接、无卡片边框的论文条目，没有复制他人的照片、论文内容或页面源码。

Google Scholar 与小红书链接由本人提供，保留原始 URL。主页图像均存放于本地，访问时不依赖图床。
