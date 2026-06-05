# 脱敏公开示例：中文文献周报邮件

> 这是一个脱敏后的公开 demo，用于展示 Research Agent Toolkit 预期生成的中文周报结构、信息密度和核验标准。
> 示例只保留公开论文、模型、代码仓库与项目页信息；不包含发件人、收件人、邮箱地址、私人日志、内部页面链接或任何个人信息。
> 正式运行时，所有条目应来自可核验来源；不得编造论文、链接、权重、代码、许可证状态或实验结论。

## 邮件标题

```text
[NeuroPET-MRI Weekly] MRI-to-PET / Tau PET / CLIP 文献更新 - YYYY-MM-DD
```

---

## 一、本周期最重要结论

检索窗口：最近 7 天；如果强相关结果不足，则按配置扩展到最近 30 天。

本周期重点检查：

- Journal of Nuclear Medicine；
- IEEE Transactions on Radiation and Plasma Medical Sciences；
- European Journal of Nuclear Medicine and Molecular Imaging；
- IEEE Transactions on Medical Imaging；
- Medical Image Analysis；
- PubMed / Europe PMC / Crossref / Semantic Scholar / DOI 页面；
- arXiv / OpenReview；
- GitHub releases；
- Hugging Face model cards and dataset cards。

### 摘要判断

- MRI-to-PET / Tau PET / Alzheimer's disease (AD, 阿尔茨海默病) 方向：如果检索窗口内强相关结果较少，应如实说明，不为了凑数降低标准。
- 医学 CLIP (Contrastive Language-Image Pretraining) / VLM (Vision-Language Model) 方向：优先关注有公开代码、公开权重、清晰模型卡、许可证明确、可复现实验路径的更新。
- 对当前 PET/MRI 研究最有迁移价值的方法学信号包括：3D medical vision-language model、patch-level / region-aware 对齐、医学图像 foundation model、开放权重与可复现实验 pipeline。

---

## 二、MRI-to-PET / Tau PET / Alzheimer's disease 强相关论文

### [1] Realistic PET image synthesis from MRI for automated inference of brain atrophy and Alzheimer's

- 类型：peer-reviewed journal article / iScience
- 相关性评分：95/100
- 可复用性评分：82/100
- 研究方向：MRI (Magnetic Resonance Imaging) to PET (Positron Emission Tomography) synthesis; Alzheimer's disease classification; synthetic PET evaluation
- 公开链接：
  - DOI: https://doi.org/10.1016/j.isci.2026.115747
  - PubMed: https://pubmed.ncbi.nlm.nih.gov/42164525/
  - GitHub: https://github.com/btheodorou99/MRI2PET/
  - Zenodo: https://zenodo.org/records/15089724
- 核验状态：标题、DOI、PubMed 条目、GitHub 仓库和 Zenodo 归档可交叉核验。
- 方法摘要：3D diffusion MRI2PET，从 T1-weighted MRI 生成 amyloid PET，并评估 synthetic PET 对 AD/MCI/normal control 分类和 cognitive-score prediction 的下游价值。
- 对当前课题的价值：与 MRI-to-PET generation 直接相关，建议优先阅读全文，并重点比较 diffusion 结构、数据拆分、下游任务评估和代码组织方式。
- 纳入理由：它同时满足强相关、公开代码/归档可访问、方法可迁移、下游评估明确等条件。

---

## 三、医学图像大模型 / 医学视觉语言模型更新

### [1] Hulu-Med: A Transparent Generalist Model towards Holistic Medical Vision-Language Understanding

- 类型：Hugging Face model update + GitHub repository + arXiv paper
- 相关性评分：90/100
- 可复用性评分：88/100
- 模型示例：Hulu-Med-Flash-Preview-27B / Hulu-Med-30A3
- 公开链接：
  - Hugging Face: https://huggingface.co/ZJU-AI4H/Hulu-Med-Flash-Preview-27B
  - Hugging Face: https://huggingface.co/ZJU-AI4H/Hulu-Med-30A3
  - GitHub: https://github.com/ZJUI-AI4H/Hulu-Med
  - arXiv: https://arxiv.org/abs/2510.08668
- 模态：medical text, 2D image, 3D volume, video；覆盖 CT, MRI, X-Ray, Ultrasound, PET 等医学模态。
- License：Apache-2.0。
- 与 BiomedCLIP 的关系：不是 CLIP-style dual encoder，而是 generalist medical vision-language model。
- 对 MRI-to-PET / Tau PET / AD 的潜在价值：可作为 3D 医学影像和多模态指令理解基座，适合探索影像-文本报告、病例级表征、prompt-based 质量控制。
- 纳入理由：公开度高、模型卡清晰、医学模态覆盖广，适合优先做小规模可运行验证。

### [2] Curia-2: Scaling Self-Supervised Learning for Radiology Foundation Models

- 类型：arXiv preprint + Hugging Face model
- 相关性评分：84/100
- 可复用性评分：86/100
- 公开链接：
  - arXiv: https://arxiv.org/abs/2604.01987
  - Hugging Face: https://huggingface.co/raidium/curia-2
- 模态：CT, MRI
- 模型结构：DINOv2-style self-supervised radiology foundation model
- License：research-only license; downstream use should be checked before redistribution or commercial use.
- 对当前课题的潜在价值：可作为 MRI encoder 或 radiology representation baseline，适合与 BiomedCLIP-style 表征、MRI-to-PET generation encoder 和 downstream AD classification 任务进行比较。
- 纳入理由：权重可访问，医学影像 foundation-model 属性明确，适合迁移实验。

---

## 四、间接相关但可能有启发的论文或模型

### [1] OpenMedQ: Broad Open Pretraining for Medical Vision-Language Models

- 类型：conference submission / OpenReview
- 相关性评分：80+/100
- 方法信号：开放数据混合预训练、医学视觉语言模型、reproducible pretraining recipe。
- 对 PET/MRI 的启发：虽然不直接解决 MRI-to-PET generation，但其开放数据组织方式和视觉语言模型训练流程可为 biomedical AI reproducibility 提供参考。

### [2] Patch-level or region-aware medical CLIP-style models

- 类型：method-oriented related work
- 方法信号：patch-level alignment, region prompt, interactive segmentation, local semantic grounding。
- 对 PET/MRI 的启发：适合迁移到脑区级 tau/amyloid burden、Braak staging、region-of-interest guided synthesis 或局部异常解释。

---

## 五、未纳入内容与原因

典型排除原因包括：

- 标题、DOI、模型卡或代码链接无法稳定核验；
- 日期不在检索窗口内，且没有明确更新；
- 与 MRI-to-PET / Tau PET / Alzheimer's disease 或 medical VLM 的关联较弱；
- 只有营销页或新闻稿，缺少论文、代码、模型卡或可复现实验信息；
- 模型卡信息不足，无法确认许可证、权重、训练模态或预期用途；
- 只属于医学文本问答、命名实体识别、语音识别或个人 LoRA 微调，与 neuroimaging/PET 迁移价值较低。

---

## 六、下周建议关注关键词

- MRI-to-PET synthesis; MRI2PET; synthetic PET; pseudo-PET generation
- tau PET synthesis; amyloid PET synthesis; FDG PET reconstruction
- Alzheimer's disease; MCI conversion; amyloid positivity prediction; tau burden prediction
- 3D diffusion model; cross-modal generation; PET/MRI multimodal fusion; SUVR prediction
- medical CLIP; radiology CLIP; patch-level contrastive learning; region-aware prompt integration
- medical VLM; 3D medical VLM; radiology foundation model; MRI foundation model; PET foundation model
- Hugging Face medical imaging model card; GitHub medical VLM release; reproducible biomedical AI workflow

---

## Demo privacy note

This file is intentionally sanitized. It does not contain email addresses, recipients, message IDs, private workspace links, private logs, or personal identifiers. Public links are included only when they point to papers, code repositories, model cards, or archives that are already publicly accessible.
