# 快速开始（v1.0）

本页面面向第一次使用 Research Agent Toolkit 的科研用户。

v1.0 只包含：

- 文献自动监控
- 中文周报生成
- 邮件发送（默认关闭）

不包含 Notion 自动化。

---

## 1. 环境准备

```bash
python --version
```

建议：

```text
Python >= 3.11
```

安装：

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

---

## 2. 创建配置文件

```bash
cp config.example.yaml config.yaml
```

关键字段：

```yaml
email:
  enabled: false

safety:
  dry_run: true
```

默认不会发邮件。

---

## 3. 配置 LLM

例如 DeepSeek：

```bash
export LLM_BASE_URL="https://api.deepseek.com"
export LLM_API_KEY="your_api_key"
export LLM_MODEL="deepseek-chat"
```

---

## 4. 验证配置

```bash
rat validate-config --config config.yaml
```

---

## 5. 运行 dry-run

```bash
rat literature-monitor --config config.yaml --dry-run
```

输出：

```text
outputs/YYYY-MM-DD/
```

---

## 6. 启用邮件发送

```yaml
email:
  enabled: true

safety:
  dry_run: false
```

---

## 7. GitHub Actions

路径：

```text
.github/workflows/literature-monitor.yml
```

默认：

```text
每周一运行
```

---

## 安全提醒

- 不要提交 API key
- 不要提交邮箱密码
- 建议先 dry-run
