# COREP C 01.00 – Own Funds template (simplified for prototype)

COREP_C01_SCHEMA = {
    "template_id": "C_01.00",
    "template_name": "Own Funds",
    "description": "COREP Own Funds reporting template",
    "fields": [
        {
            "row_id": "1",
            "field_name": "CET1_Total",
            "description": "Common Equity Tier 1 (CET1) Capital",
            "required": True
        },
        {
            "row_id": "1.1.1",
            "field_name": "Paid_Up_Ordinary_Shares",
            "description": "Paid-up ordinary shares",
            "required": True
        },
        {
            "row_id": "1.2",
            "field_name": "Retained_Earnings",
            "description": "Retained earnings",
            "required": True
        },
        {
            "row_id": "2",
            "field_name": "CET1_Deductions",
            "description": "Deductions from CET1 capital",
            "required": False
        }
    ]
}
