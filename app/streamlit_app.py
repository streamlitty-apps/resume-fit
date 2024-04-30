import streamlit as st
from streamlit_option_menu import option_menu
from views.analyze_resume_page import analyze_resume_page
from views.resume_resources_page import resume_resources_page


def get_openai_api_key():
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

    if not st.session_state.api_key:
        api_key = st.text_input(
            "Enter your OpenAI API key to get started:", type="password"
        )
        if api_key:
            st.session_state.api_key = api_key
            st.rerun()


def run_streamlit_app():
    st.set_page_config(page_title="Resume Fit", page_icon=":clipboard:")

    with st.sidebar:
        selected = option_menu(
            menu_title="Resume Fit",
            options=["Analyze Resume", "Resume Resources"],
            icons=["upload", "book"],
            menu_icon="clipboard",
            default_index=0,
        )

    if selected == "Analyze Resume":
        if "api_key" not in st.session_state or not st.session_state.api_key:
            st.title("Welcome to Resume Fit!")
            st.info("Your personal assistant for landing the perfect job!")
            get_openai_api_key()
        else:
            analyze_resume_page()

    elif selected == "Resume Resources":
        resume_resources_page()


if __name__ == "__main__":
    run_streamlit_app()
