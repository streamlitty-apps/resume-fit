import streamlit as st
from streamlit_option_menu import option_menu
from views.initial_page_load import initial_page_load
from views.analyze_resume_page import analyze_resume_page


def run_streamlit_app():
    st.set_page_config(page_title="Resume Fit", page_icon=":clipboard:")

    with st.sidebar:
        selected = option_menu(
            menu_title="Resume Fit",
            options=["Analyze Resume"],
            icons=["upload", "book"],
            menu_icon="clipboard",
            default_index=0,
        )

    if selected == "Analyze Resume":
        if not st.session_state.get("api_key"):
            initial_page_load()
        else:
            analyze_resume_page()


if __name__ == "__main__":
    run_streamlit_app()
