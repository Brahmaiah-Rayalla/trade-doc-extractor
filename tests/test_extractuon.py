from app.validator import validate_extraction

def test_validate_extraction():
    sample_json = {
        "document_type": {"value": "Invoice", "confidence": 0.95},
        "issuing_bank": {"value": None, "confidence": 0.0},
        "beneficiary": {"value": "XYZ Corp", "confidence": 0.85}
    }
    flagged = validate_extraction(sample_json)
    assert "issuing_bank" in flagged
    assert "document_type" not in flagged
    assert "beneficiary" not in flagged
