from fastapi import FastAPI
from schema import COREP_C01_SCHEMA
from retrieval import retrieve_relevant_rules
from llm_processor import process_scenario_with_llm
from validator import validate_corep_output

app = FastAPI(title="COREP Reporting Assistant")

@app.post("/process")
def process_scenario(question: str):
    rules = retrieve_relevant_rules(question)
    llm_output = process_scenario_with_llm(question, rules)
    validation = validate_corep_output(llm_output, COREP_C01_SCHEMA)

    return {
        "corep_output": llm_output,
        "validation": validation
    }
