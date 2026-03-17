# Lobster Insight

**Binance Square Sentiment Stripping & Contrarian Alpha Engine**

Lobster Insight is a lightweight, open-source demo kit for a Binance Square-native AI agent.
It is designed to turn noisy, hype-heavy social posts into a structured risk report:
- strip emotional language from facts
- detect overheated consensus
- trace minority high-quality viewpoints
- generate calm action guidance

This repository is intentionally lightweight and demo-friendly. It is not a trading bot and does not place orders.

## What this repo includes

- a reusable system prompt for OpenClaw or other LLM agent shells
- sample Binance Square-style hype inputs
- a Python mock pipeline that converts post batches into a structured report
- a CLI demo runner
- example outputs you can use for screenshots or demos

## Core modules

1. **Noise Filtration**  
   Separates hype, slogans, and manipulative language from verifiable facts.

2. **Contrarian Index**  
   Detects one-sided crowd behavior, euphoric language, and FOMO extremes.

3. **Narrative Saturation Monitor**  
   Measures repetition, low novelty, and overcrowded consensus.

4. **Smart Consensus Tracer**  
   Surfaces minority posts that contain mechanism analysis, data reasoning, or explicit risk discussion.

5. **Actionable Insight Composer**  
   Produces calm, explainable guidance such as “avoid chasing”, “wait for confirmation”, or “keep size disciplined”.

## Quick start

### 1) Use the Python demo

```bash
python -m src.demo --input examples/hype_wave_posts.json
```

### 2) Or paste the system prompt into OpenClaw

The reusable prompt lives here:

```text
prompts/system_prompt.md
```

Recommended first demo input:

```text
prompts/demo_input_1.md
```

## Example output

The CLI prints a structured JSON report and a human-readable markdown report.
A sample markdown report is included at:

```text
examples/sample_report.md
```

## Repository structure

```text
Lobster-Insight/
├─ README.md
├─ LICENSE
├─ requirements.txt
├─ prompts/
│  ├─ system_prompt.md
│  ├─ demo_input_1.md
│  └─ demo_input_2.md
├─ examples/
│  ├─ hype_wave_posts.json
│  ├─ product_card.json
│  └─ sample_report.md
├─ lobster_insight/
│  ├─ __init__.py
│  ├─ models.py
│  ├─ heuristics.py
│  ├─ engine.py
│  └─ render.py
└─ src/
   └─ demo.py
```

## Intended use

This project is built for:
- demo videos
- hackathon submissions
- prompt prototyping
- reproducible agent workflows
- future extensions into richer NLP pipelines

## Not included

This repository does **not** include:
- exchange connectivity
- order execution
- portfolio management
- live scraping of Binance Square
- financial advice

## Future extensions

- real post ingestion layer
- embedding-based viewpoint clustering
- stronger sentiment labeling
- event extraction from multilingual post streams
- score calibration from live community data

## License

MIT
