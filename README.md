# trade-doc-extractor
OCR + extraction tool pull required data from uploaded trade documents

# International Trade Document Extractor

## Features:
- OCR with Tesseract + pdf2image
- JSON Extraction with OpenAI GPT
- Confidence Scoring & Validation
- GitHub Actions + Render Deployment

## Deployment:
- Add OPENAI_API_KEY to Render & GitHub Secrets
- Push to `main` — GitHub Actions deploys automatically
- Expose endpoint: POST /extract-json/

## Local Run:
