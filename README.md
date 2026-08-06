# `x402-0mod-tools`

Python tools for **0mod API Gateway** (`api.0mod.com`) supporting LangChain, CrewAI, and AutoGPT autonomous agent loops.

## Installation

```bash
pip install x402-0mod-tools
```

## Tools Included

- `StealthDomTool`: Fetches web page HTML from Cloudflare edge.
- `AirgapScrubTool`: Redacts SSNs, phone numbers, emails, and ZIP codes using Workers AI.
- `RagShrinkTool`: Strips HTML boilerplate down to clean Markdown/headings for RAG.
