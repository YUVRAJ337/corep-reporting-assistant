def validate_corep_output(llm_output, schema):
    errors = []
    warnings = []

    populated = {f["row_id"]: f for f in llm_output["populated_fields"]}

    # Check required fields
    for field in schema["fields"]:
        if field["required"] and field["row_id"] not in populated:
            errors.append(f"Missing required field: {field['field_name']}")

    # Check CET1 calculation
    try:
        shares = populated["1.1.1"]["value"]
        earnings = populated["1.2"]["value"]
        deductions = populated.get("2", {}).get("value", 0)
        total = populated["1"]["value"]

        expected = shares + earnings - deductions
        if total != expected:
            warnings.append(
                f"CET1 mismatch: expected {expected}, got {total}"
            )
    except KeyError:
        warnings.append("Could not fully validate CET1 calculation")

    return {
        "is_valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings
    }
