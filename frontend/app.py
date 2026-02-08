import streamlit as st
import requests

# Page Configuration
st.set_page_config(
    page_title="COREP Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling (optional but good for polish)
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title and Subtitle
st.title("🏦 COREP C 01.00 – Own Funds Reporting Assistant")
st.markdown("##### AI-powered regulatory reporting, compliance rule justification, and audit trail generation.")

# 1. Input Scenario Section
st.header("Input Scenario")
st.markdown("Describe the financial situation for the reporting period below.")

col1, col2 = st.columns([2, 1])

with col1:
    scenario = st.text_area(
        "Reporting Text",
        height=150,
        placeholder="e.g., We have £10m share capital, £3m retained earnings, and £1m goodwill deduction..."
    )

    generate_btn = st.button("Generate Regulatory Report", type="primary")

if generate_btn:
    if not scenario.strip():
        st.warning("⚠️ Please enter a scenario description to proceed.")
    else:
        with st.spinner("🤖 Analyzing regulations & generating report..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/process",
                    params={"question": scenario}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    corep_output = data.get("corep_output", {})

                    # 2. Populated COREP Fields Section
                    st.divider()
                    st.header("Populated COREP Fields")
                    st.info("The following values have been extracted and mapped to C 01.00 fields.")

                    populated_fields = corep_output.get("populated_fields", [])
                    missing_fields = corep_output.get("missing_fields", [])
                    audit_trail = corep_output.get("audit_trail", "")

                    if populated_fields:
                        for field in populated_fields:
                            with st.container():
                                c1, c2, c3 = st.columns([1, 2, 1])
                                with c1:
                                    st.caption(f"Row {field.get('row_id', 'N/A')}")
                                    st.markdown(f"**{field.get('field_name', 'Unknown').replace('_', ' ')}**")
                                with c2:
                                    st.caption("Reasoning")
                                    st.write(field.get("reasoning", "N/A"))
                                    st.caption("Regulatory Check")
                                    st.markdown(f"*{field.get('justification', 'N/A')}*")
                                with c3:
                                    val = field.get("value", 0)
                                    display_val = f"£{val:,.2f}" if isinstance(val, (int, float)) else str(val)
                                    st.metric("Value", display_val)
                                st.divider()
                    else:
                        st.write("No fields populated.")

                    # Missing Fields Section
                    if missing_fields:
                        st.warning(f"⚠️ Missing Data: {', '.join(missing_fields)}")
                    else:
                        st.success("✅ All required fields found.")

                    # 3. Audit Trail Section
                    st.header("Audit Trail")
                    st.write(audit_trail)
                    with st.expander("📄 View Full JSON Response"):
                        st.json(data)

                    # 4. Validation Results Section
                    st.divider()
                    st.header("Validation Results")
                    
                    validation_data = data.get("validation", {})
                    
                    if isinstance(validation_data, dict):
                         # If validation returns simple pass/fail or dict of checks
                         is_valid = validation_data.get("is_valid", False)
                         if is_valid:
                             st.success("✅ Validation Passed")
                         else:
                             st.error("❌ Validation Failed")
                             
                         errors = validation_data.get("errors", [])
                         warnings = validation_data.get("warnings", [])
                         
                         if errors:
                             for err in errors:
                                 st.error(f"Error: {err}")
                         if warnings:
                             for warn in warnings:
                                 st.warning(f"Warning: {warn}")
                                 
                         # Fallback if structure is different
                         if not errors and not warnings and not isinstance(is_valid, bool):
                            st.json(validation_data)
                    else:
                        st.json(validation_data)

                else:
                    st.error(f"❌ Backend Error ({response.status_code}): {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the backend. Please ensure the FastAPI server is running.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")
