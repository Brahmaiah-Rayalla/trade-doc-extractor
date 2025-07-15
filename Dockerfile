FROM python:3.11

WORKDIR /app

COPY . .

# Install Poppler for pdf2image (provides pdfinfo, pdftoppm)
RUN apt-get update && apt-get install -y poppler-utils

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
