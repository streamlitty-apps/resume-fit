import streamlit as st
from helpers.openai_client import validate_openai_api_key


def initial_page_load():
    st.title("Welcome to Resume Fit!")
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

    api_key = st.text_input("Please enter your OpenAI API key:", type="password")
    if api_key:
        is_valid = validate_openai_api_key(api_key)
        if is_valid:
            st.session_state["api_key"] = api_key
            st.rerun()
        else:
            st.error("Incorrect or invalid OpenAI API key")
            st.stop()
    else:
        st.info("Your OpenAI API key required to continue")
        st.stop()
