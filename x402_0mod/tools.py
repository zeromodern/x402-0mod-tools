import requests
from pydantic import BaseModel, Field

GATEWAY_BASE = "https://api.0mod.com"

class StealthDomInput(BaseModel):
    url: str = Field(description="Target URL to fetch from edge")
    userAgent: str = Field(default=None, description="Custom User-Agent header")

class StealthDomTool:
    name: str = "stealth_dom_fetch"
    description: str = "Fetches web page HTML from Cloudflare edge bypassing simple IP blocks"
    args_schema = StealthDomInput

    def run(self, url: str, userAgent: str = None) -> dict:
        payload = {"url": url}
        if userAgent:
            payload["userAgent"] = userAgent
        res = requests.post(f"{GATEWAY_BASE}/api/v1/stealth-dom", json=payload)
        return res.json()

class AirgapScrubInput(BaseModel):
    text: str = Field(description="Input text containing potential PII")
    strictMode: bool = Field(default=False, description="Enable Workers AI Llama 3.1 redaction")

class AirgapScrubTool:
    name: str = "airgap_pii_scrub"
    description: str = "Redacts SSN, phone, email, ZIP using Cloudflare Workers AI"
    args_schema = AirgapScrubInput

    def run(self, text: str, strictMode: bool = False) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/airgap-scrub", json={"text": text, "strictMode": strictMode})
        return res.json()

class RagShrinkInput(BaseModel):
    html: str = Field(description="Raw HTML string to parse")

class RagShrinkTool:
    name: str = "rag_shrink_html"
    description: str = "Compresses HTML to markdown headings and paragraphs for RAG"
    args_schema = RagShrinkInput

    def run(self, html: str) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/rag-shrink", json={"html": html})
        return res.json()
