# Quickstart

This guide is the shortest path from a fresh clone to a first dry-run.
If you want the broader project overview, see [README.md](../README.md).
For the Chinese version, see [docs/quickstart.zh-CN.md](quickstart.zh-CN.md).

## 1. Install Python

Python 3.11 or newer is recommended. Confirm your local version first:

```bash
python --version
```

Then install the project in editable mode:

```bash
git clone https://github.com/linshuijin6/research-agent-toolkit.git
cd research-agent-toolkit
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## 2. Create `config.yaml`

Start from the example config and keep the safety defaults in place while you test:

```bash
cp config.example.yaml config.yaml
```

The default example keeps email delivery disabled and dry-run enabled. If you edit the file manually, make sure the first run still looks like this:

```yaml
email:
  enabled: false

safety:
  dry_run: true
```

## 3. Set up your LLM provider

The toolkit uses an OpenAI-compatible backend. Set the provider values as environment variables or GitHub Actions secrets instead of hard-coding them in the repository.

Example for an OpenAI-compatible service:

```bash
export LLM_BASE_URL="https://api.openai.com/v1"
export LLM_API_KEY="your_api_key"
export LLM_MODEL="gpt-4o"
```

Example for DeepSeek:

```bash
export LLM_BASE_URL="https://api.deepseek.com"
export LLM_API_KEY="your_api_key"
export LLM_MODEL="deepseek-chat"
```

## 4. Validate the config and run dry-run

Check the configuration before sending anything:

```bash
rat validate-config --config config.yaml
```

Run the monitor in dry-run mode next:

```bash
rat literature-monitor --config config.yaml --dry-run
```

A successful run writes artifacts under:

```text
outputs/YYYY-MM-DD/
```

## 5. Use GitHub Actions

The repository ships with [`.github/workflows/literature-monitor.yml`](../.github/workflows/literature-monitor.yml).
That workflow installs Python 3.11, prepares `config.yaml` if needed, and runs the monitor in dry-run mode.

Before enabling it in a real repository, add the required secrets in GitHub instead of committing them:

```text
LLM_BASE_URL
LLM_API_KEY
LLM_MODEL
SEMANTIC_SCHOLAR_API_KEY
HUGGINGFACE_TOKEN
SMTP_HOST
SMTP_PORT
SMTP_USERNAME
SMTP_PASSWORD
SMTP_FROM
```

`GITHUB_TOKEN` is provided automatically by GitHub Actions.

## 6. SMTP safety notes

Keep SMTP delivery disabled until the dry-run looks correct.

**Warning:** `rat send-test-email` sends a real email immediately. It does **not** honor `email.enabled: false` or `safety.dry_run: true`.

Use these rules when you are ready to test email delivery:

- leave `email.enabled: false` during initial setup;
- keep `safety.dry_run: true` until you have reviewed the generated output;
- store all SMTP credentials as secrets, not in `config.yaml`;
- change `email.recipient` from the example value to an address you control before running `rat send-test-email`;
- verify the recipient, sender, and subject prefix before enabling delivery;
- use `rat send-test-email` only after the configuration is validated and only when you intend to send a real test message.

## Acceptance criteria

You are ready when all of the following are true:

- Python 3.11 or newer is installed;
- `config.yaml` exists and starts from `config.example.yaml`;
- LLM credentials are available through environment variables or GitHub Actions secrets;
- `rat validate-config --config config.yaml` passes;
- `rat literature-monitor --config config.yaml --dry-run` completes successfully;
- GitHub Actions runs the same dry-run workflow without sending email;
- SMTP remains disabled until you explicitly choose to enable delivery.
