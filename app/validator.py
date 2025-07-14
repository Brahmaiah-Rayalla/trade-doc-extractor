CONFIDENCE_THRESHOLD = 0.80

def validate_extraction(extracted_json):
    flagged_fields = []
    for key, field in extracted_json.items():
        if isinstance(field, dict) and 'confidence' in field:
            if field['confidence'] < CONFIDENCE_THRESHOLD:
                flagged_fields.append(key)
    return flagged_fields
