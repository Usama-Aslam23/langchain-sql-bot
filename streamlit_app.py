import streamlit as st
from sql_agent import build_sql_chain_from_path, get_schema_diagram
from utils.query_splitter import split_into_subqueries

st.set_page_config(page_title="LangChain SQL Bot", page_icon="🧠")

st.title("🧠 LangChain SQL Bot")
st.markdown("Ask questions about your Salesforce-style database.")

uploaded_file = st.file_uploader("📁 Upload a SQLite database", type=["db", "sqlite"])

if uploaded_file is not None:
    with open("temp_uploaded.db", "wb") as f:
        f.write(uploaded_file.read())
else:
    st.warning("Please upload a SQLite `.db` file to begin.")
    st.stop()

chain = build_sql_chain_from_path("temp_uploaded.db")

with st.expander("📚 View Schema Diagram"):
    dot = get_schema_diagram("temp_uploaded.db")
    st.graphviz_chart(dot)

query = st.text_input("💬 Ask a question:")

if query:
    st.markdown("### 💬 Results")
    subqueries = split_into_subqueries(query)

    for i, sub in enumerate(subqueries):
        with st.spinner(f"Running sub-query {i+1}: {sub}"):
            try:
                result = chain.invoke(sub)
                st.markdown(f"**Q{i+1}:** {sub}")
                if isinstance(result, dict) and "result" in result:
                    st.success(result["result"])
                else:
                    st.success(result)
            except Exception as e:
                st.error(f"⚠️ Error in sub-query {i+1}: {e}")