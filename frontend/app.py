import streamlit as st
from dotenv import load_dotenv
import os
import requests
import json

SEARCH_AGENT_ENDPOINT = os.getenv("SEARCH_AGENT_ENDPOINT")

def ai_search_agent_tab():
    st.header("AI Search Agent (Goodreads)")
    st.write("This agent can answer questions about books using the Goodreads API.")
    question = st.text_input("Ask a question about books:")
    if st.button("Ask"):
        response = requests.post(
            f"{SEARCH_AGENT_ENDPOINT}/ask",
            json={"question": question},
        )
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.write(answer)


#################################################################################
# MAIN FUNCTION
#################################################################################

def main():
    st.set_page_config(
        page_title="Manufacturing EOU - Azure AI Agent Service Demos",
        layout="wide",  # wide mode
    )
    st.title("Azure AI Agent Service Demos")

    # Sidebar for navigation
    page = st.sidebar.radio("Interact with agent:", ["AI Search Agent (Goodreads)", "Azure SQL Agent (Goodreads)", "Interactive Data Analysis Agent"])

    # with tabs[0]:
    if page == "AI Search Agent (Goodreads)":
        ai_search_agent_tab()

    # with tabs[1]:
    if page == "Azure SQL Agent (Goodreads)":
        azure_sql_agent_tab()

    # with tabs[2]:
    if page == "Interactive Data Analysis Agent":
        data_analysis_agent_tab()

    st.sidebar.success("Select an agent from the dropdown above.")


if __name__ == "__main__":
    main()
