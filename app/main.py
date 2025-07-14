from fastapi import FastAPI, UploadFile, File
from app.ocr_service import extract_text_from_pdf
from app.llm_extractor import extract_json_with_llm
from app.validator import validate_extraction

app = FastAPI()

@app.post("/extract-json/")
async def extract_json(file: UploadFile = File(...)):
    with open('temp.pdf', 'wb') as f:
        f.write(await file.read())

    extracted_text = extract_text_from_pdf('temp.pdf')

    with open('app/templates/extraction_prompt.txt') as f:
        prompt_template = f.read()

    extracted_json = extract_json_with_llm(extracted_text, prompt_template)
    flagged_fields = validate_extraction(extracted_json)

    return {
        "extracted_data": extracted_json,
        "flagged_fields": flagged_fields
    }
