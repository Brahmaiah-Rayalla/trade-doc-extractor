from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import traceback
from app.ocr_service import extract_text_from_pdf
from app.llm_extractor import extract_json_with_llm, extract_json_with_vertexai, extract_json_with_openai
from app.validator import validate_extraction

app = FastAPI()

class ExtractionResponse(BaseModel):
    extracted_data: dict
    flagged_fields: list

@app.post("/extract-json/", response_model=ExtractionResponse, tags=["LLM Extraction"], summary="Extract JSON using selected LLM provider", description="Extracts structured data from a PDF using the provider specified by the LLM_PROVIDER environment variable (OpenAI or Google Vertex AI).")
async def extract_json(file: UploadFile = File(...)):
    """Extract JSON using the provider specified by LLM_PROVIDER (OpenAI or Vertex AI)."""
    try:
        with open('temp.pdf', 'wb') as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf('temp.pdf')

        with open('app/templates/extraction_prompt.txt') as f:
            prompt_template = f.read()

        extracted_json = extract_json_with_llm(extracted_text, prompt_template)
        flagged_fields = validate_extraction(extracted_json)

        return ExtractionResponse(extracted_data=extracted_json, flagged_fields=flagged_fields)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "details": traceback.format_exc()
            }
        )

@app.post("/extract-json-vertex/", response_model=ExtractionResponse, tags=["LLM Extraction"], summary="Extract JSON using Google Vertex AI", description="Extracts structured data from a PDF using Google Vertex AI (Studio AI), regardless of environment variable settings.")
async def extract_json_vertex(file: UploadFile = File(...)):
    """Extract JSON using Google Vertex AI (Studio AI), regardless of environment variable settings."""
    try:
        with open('temp.pdf', 'wb') as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf('temp.pdf')

        with open('app/templates/extraction_prompt.txt') as f:
            prompt_template = f.read()

        extracted_json = extract_json_with_vertexai(extracted_text, prompt_template)
        flagged_fields = validate_extraction(extracted_json)

        return ExtractionResponse(extracted_data=extracted_json, flagged_fields=flagged_fields)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "details": traceback.format_exc()
            }
        )

@app.post("/extract-json-openai/", response_model=ExtractionResponse, tags=["LLM Extraction"], summary="Extract JSON using OpenAI", description="Extracts structured data from a PDF using OpenAI, regardless of environment variable settings.")
async def extract_json_openai(file: UploadFile = File(...)):
    """Extract JSON using OpenAI, regardless of environment variable settings."""
    try:
        with open('temp.pdf', 'wb') as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf('temp.pdf')

        with open('app/templates/extraction_prompt.txt') as f:
            prompt_template = f.read()

        extracted_json = extract_json_with_openai(extracted_text, prompt_template)
        flagged_fields = validate_extraction(extracted_json)

        return ExtractionResponse(extracted_data=extracted_json, flagged_fields=flagged_fields)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "details": traceback.format_exc()
            }
        )

@app.post("/extract-json-googleai/", response_model=ExtractionResponse, tags=["LLM Extraction"], summary="Extract JSON using Google Vertex AI (Studio AI)", description="Extracts structured data from a PDF using Google Vertex AI (Studio AI), regardless of environment variable settings.")
async def extract_json_googleai(file: UploadFile = File(...)):
    """Extract JSON using Google Vertex AI (Studio AI), regardless of environment variable settings."""
    try:
        with open('temp.pdf', 'wb') as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf('temp.pdf')

        with open('app/templates/extraction_prompt.txt') as f:
            prompt_template = f.read()

        extracted_json = extract_json_with_vertexai(extracted_text, prompt_template)
        flagged_fields = validate_extraction(extracted_json)

        return ExtractionResponse(extracted_data=extracted_json, flagged_fields=flagged_fields)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e),
                "details": traceback.format_exc()
            }
        )
