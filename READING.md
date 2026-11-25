# Reading List

[Back to my profile](README.md)

A curated directory of technical blogs and long-form articles on model foundations, pretraining, world models, agents, and ML systems. The emphasis is on clear derivations, practical training recipes, and implementation details; papers and code serve as companion references.

Recent additions (November 25, 2026) focus on data quality, reproducible training recipes, distributed systems, and video representation learning. Suggested order: **FineWeb → OLMo 2 → Ultra-Scale Playbook → TorchTitan**, followed by **V-JEPA 2 → video foundation model pipelines**.

## Core Blogs

- **Theory and generative models:** [Jianlin Su — Scientific Spaces](https://kexue.fm/), [Sander Dieleman](https://sander.ai/), and [Yang Song](https://yang-song.net/blog/).
- **LLMs and training practice:** [Sebastian Raschka](https://sebastianraschka.com/blog/), [Ahead of AI](https://magazine.sebastianraschka.com/), and the [Hugging Face Blog](https://huggingface.co/blog).
- **Research surveys and systems:** [Lilian Weng — Lil’Log](https://lilianweng.github.io/), [Chip Huyen](https://huyenchip.com/blog/), and [Edward Z. Yang](https://blog.ezyang.com/).

The topic sections below collect specific articles, reading priorities, and implementation links. The pretraining and world-model additions are kept here together with the established blog directory.

## Browse by Topic

- [Model Foundations and Mathematics](#model-foundations-and-mathematics)
- [Foundation Model Pretraining and Scaling](#foundation-model-pretraining-and-scaling)
- [Multimodal and World Model Pretraining](#multimodal-and-world-model-pretraining)
- [LLMs, Agents and Post-training](#llms-agents-and-post-training)
- [ML Systems and Engineering](#ml-systems-and-engineering)

## Model Foundations and Mathematics

- **[Jianlin Su — Scientific Spaces](https://kexue.fm/)** · Mathematical derivations, attention mechanisms, and language models (Chinese)
- **[Sander Dieleman](https://sander.ai/)** · Generative models · [Perspectives on diffusion](https://sander.ai/2023/07/20/perspectives.html)
- **[Yang Song](https://yang-song.net/blog/)** · Score-based models · [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/)
- **[Francis Bach](https://francisbach.com/)** · Optimization and statistical learning · [Scaling laws of optimization](https://francisbach.com/scaling-laws-of-optimization/) · [Jensen's inequality](https://francisbach.com/jensen-inequality/)
- **[Gregory Gundersen](https://gregorygundersen.com/blog/)** · Probability, statistics, and linear algebra · [The Log-Sum-Exp Trick](https://gregorygundersen.com/blog/2020/02/09/log-sum-exp/)
- **[Transformer Circuits](https://transformer-circuits.pub/)** · Mechanistic interpretability · [A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)
- **[Chris Olah — colah's blog](https://colah.github.io/)** · Visual explanations · [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/)

## Foundation Model Pretraining and Scaling

Selected for explicit data decisions, training recipes, reproducibility, and implementation detail.

- **[FineWeb: decanting the web for the finest text data at scale](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1)** — Hugging Face.<br>
  Study filtering, MinHash deduplication, and controlled data-quality ablations before choosing a pretraining corpus. Pair the article with [DataTrove](https://github.com/huggingface/datatrove) to inspect the processing pipeline.
- **[OLMo 2](https://allenai.org/blog/olmo2)** — Ai2.<br>
  Study training stability, late-stage data curricula, learning-rate annealing, and evaluation. The [technical report](https://arxiv.org/abs/2501.00656) documents the recipe; [OLMo-core](https://github.com/allenai/OLMo-core) provides a companion training implementation.
- **[The Ultra-Scale Playbook: Training LLMs on GPU Clusters](https://huggingface.co/spaces/nanotron/ultrascale-playbook)** — Hugging Face.<br>
  Build a working understanding of data, tensor, pipeline, context, and expert parallelism. Focus on memory budgets, communication costs, and how combinations of parallelism affect throughput.
- **[Training a 1T-Parameter MoE with PyTorch and TorchTitan](https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/)** — EUROPA consortium / PyTorch.<br>
  Follow a concrete systems case study: FSDP and expert placement, optimizer communication, activation offloading, and compute/communication overlap. Read after the playbook, alongside [TorchTitan](https://github.com/pytorch/torchtitan).

## Multimodal and World Model Pretraining

Selected for their connection to video representations, world models, and autonomous-driving research.

- **[V-JEPA 2: video pretraining and world models](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/)** — Meta.<br>
  Study action-free video pretraining followed by action-conditioned training, and how predicted representations support planning. Pair the article with the [official implementation](https://github.com/facebookresearch/vjepa2).
- **[Accelerate Custom Video Foundation Model Pipelines with NVIDIA NeMo](https://developer.nvidia.com/blog/accelerate-custom-video-foundation-model-pipelines-with-new-nvidia-nemo-framework-capabilities/)** — NVIDIA.<br>
  Study video clipping and sharding, multimodal data loading, sequence packing, and distributed video-model training. Especially useful for connecting video data preparation to GPU utilization in generative world-model pipelines.

## LLMs, Agents and Post-training

- **[Lilian Weng — Lil'Log](https://lilianweng.github.io/)** · Research surveys · [Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) · [Diffusion Models](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) · [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/)
- **[Sebastian Raschka](https://sebastianraschka.com/blog/)** · LLM mechanisms and implementation · [Ahead of AI](https://magazine.sebastianraschka.com/) · [Coding the KV Cache from Scratch](https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms)
- **[Chip Huyen](https://huyenchip.com/blog/)** · AI system design · [Agents](https://huyenchip.com/2025/01/07/agents.html)
- **[Hamel Husain](https://hamel.dev/)** · Evaluation and error analysis · [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)
- **[Simon Willison](https://simonwillison.net/)** · Coding agents and developer workflows · [Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/) · [How coding agents work](https://simonwillison.net/guides/agentic-engineering-patterns/how-coding-agents-work/)
- **[Nathan Lambert — Interconnects](https://www.interconnects.ai/)** · RLHF, GRPO, and reasoning · [GRPO tweaks, base model RL, and data curation](https://www.interconnects.ai/p/papers-im-reading-base-model-rl-grpo)
- **[Anthropic Engineering](https://www.anthropic.com/engineering)** · Agent infrastructure, context management, and evaluation

## ML Systems and Engineering

- **[Edward Z. Yang — ezyang's blog](https://blog.ezyang.com/)** · Framework internals · [PyTorch internals](https://blog.ezyang.com/2019/05/pytorch-internals/)
- **[RossiXYZ's Blog](https://www.cnblogs.com/rossiXYZ)** · Distributed training and source-code analysis (Chinese) · [PyTorch ZeroRedundancyOptimizer](https://www.cnblogs.com/rossiXYZ/p/15782054.html)
- **[Li Li (fancyerii)](https://fancyerii.github.io/)** · Implementation and performance optimization (Chinese) · [Companion code](https://github.com/fancyerii/blog-codes) · Blog unavailable as of Nov 5, 2026
- **[Hugging Face Blog](https://huggingface.co/blog)** · Open-source models, training, and inference
