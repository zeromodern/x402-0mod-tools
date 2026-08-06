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

class CodeDenoiseInput(BaseModel):
    code: str = Field(description="Code string to strip comments and docstrings from")
    language: str = Field(default="javascript", description="Programming language")

class CodeDenoiseTool:
    name: str = "code_denoise"
    description: str = "Strips comments, docstrings, whitespace, and sourcemaps from code files"
    args_schema = CodeDenoiseInput

    def run(self, code: str, language: str = "javascript") -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/code-denoise", json={"code": code, "language": language})
        return res.json()

class DomainCheckInput(BaseModel):
    domain: str = Field(description="Domain name to check RDAP availability")

class DomainCheckTool:
    name: str = "domain_check"
    description: str = "Queries global RDAP registry from edge for domain availability and WHOIS status"
    args_schema = DomainCheckInput

    def run(self, domain: str) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/domain-check", json={"domain": domain})
        return res.json()

class DexPriceInput(BaseModel):
    query: str = Field(description="Token symbol or contract address")

class DexPriceTool:
    name: str = "dex_price_summary"
    description: str = "Fetches real-time DEX price, 24h volume, liquidity, and top pair stats across chains"
    args_schema = DexPriceInput

    def run(self, query: str) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/dex-price-summary", json={"query": query})
        return res.json()

class XSentimentInput(BaseModel):
    topic: str = Field(description="Topic, ticker, or text sample to analyze")

class XSentimentTool:
    name: str = "x_sentiment"
    description: str = "Analyzes market & social sentiment for topics/tokens using Workers AI Llama 3.1"
    args_schema = XSentimentInput

    def run(self, topic: str) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/x-sentiment", json={"topic": topic})
        return res.json()

class ImageOcrInput(BaseModel):
    imageUrl: str = Field(description="Public image URL to extract text and tables from")

class ImageOcrTool:
    name: str = "image_ocr_shrink"
    description: str = "Extracts clean text and table markdown from images via Workers AI Vision Llama 3.2"
    args_schema = ImageOcrInput

    def run(self, imageUrl: str) -> dict:
        res = requests.post(f"{GATEWAY_BASE}/api/v1/image-ocr-shrink", json={"imageUrl": imageUrl})
        return res.json()
