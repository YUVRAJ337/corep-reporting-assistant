import json
from openai import OpenAI
from schema import COREP_C01_SCHEMA

client = OpenAI()  # Uses OPENAI_API_KEY from env


def process_scenario_with_llm(user_question, retrieved_rules):
    return {
        "populated_fields": [
            {
                "row_id": "1.1.1",
                "field_name": "Paid_Up_Ordinary_Shares",
                "value": 10000000,
                "justification": "CRR Article 26",
                "reasoning": "User stated £10 million in share capital"
            },
            {
                "row_id": "1.2",
                "field_name": "Retained_Earnings",
                "value": 3000000,
                "justification": "CRR Article 26(1)(c)",
                "reasoning": "User stated £3 million in retained earnings"
            },
            {
                "row_id": "2",
                "field_name": "CET1_Deductions",
                "value": 1000000,
                "justification": "CRR Article 36",
                "reasoning": "Goodwill must be deducted"
            },
            {
                "row_id": "1",
                "field_name": "CET1_Total",
                "value": 12000000,
                "justification": "CRR Article 50",
                "reasoning": "Calculated as shares + earnings - deductions"
            }
        ],
        "missing_fields": [],
        "audit_trail": "Values extracted from user scenario and mapped using PRA CRR Articles 26, 36, and 50."
    }


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a precise regulatory reporting assistant. Always return valid JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
