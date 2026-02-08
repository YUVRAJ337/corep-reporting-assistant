# LLM-Assisted COREP Own Funds Reporting Assistant

## Overview
This project is a prototype of an LLM-assisted regulatory reporting assistant designed to support COREP C 01.00 (Own Funds) reporting under the PRA / CRR framework.

The goal of this prototype is to demonstrate how natural language financial scenarios can be transformed into structured COREP reporting outputs with clear regulatory justification and auditability.

---

## Problem Statement
Preparing COREP regulatory returns is complex and error-prone due to dense regulatory rules and manual interpretation.

This prototype demonstrates an end-to-end flow:
- User provides a natural language reporting scenario
- Relevant regulatory rules are applied
- COREP fields are populated in a structured format
- Validation checks and audit trail are generated

---

## Scope
This prototype focuses on:
- COREP Template: C 01.00 – Own Funds
- Capital elements:
  - Paid-up ordinary shares
  - Retained earnings
  - CET1 deductions (e.g. goodwill)
  - CET1 total (derived)

---

## Key Features
- Natural language scenario input
- Rule-based COREP field mapping
- Regulatory justification using CRR articles
- Validation of populated values
- Audit trail explaining calculations

---

## Example Scenario
Input:
We have £10 million share capital, £3 million retained earnings, and £1 million goodwill.

Output:
- Paid-up ordinary shares: £10,000,000 (CRR Article 26)
- Retained earnings: £3,000,000 (CRR Article 26(1)(c))
- CET1 deductions (goodwill): £1,000,000 (CRR Article 36)
- CET1 total: £12,000,000

Validation: Passed

---

## Project Structure
- backend: FastAPI backend handling processing, validation, and rule logic
- frontend: Streamlit-based user interface
- data/rules: Sample PRA / CRR regulatory rules
- requirements.txt: Python dependencies

---

## How to Run Locally
1. Create and activate virtual environment
2. Install dependencies from requirements.txt
3. Run backend using FastAPI
4. Run frontend using Streamlit

This prototype is intended to be run locally for evaluation purposes.

---

## Notes
- The project uses mock LLM logic to ensure reproducibility and avoid paid API dependencies.
- This is a prototype for demonstration purposes, not a production regulatory system.

---

## Author
Yuvraj Singh
