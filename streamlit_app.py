import json
import textwrap
import streamlit as st
from PyPDF2 import PdfReader
from streamlit_option_menu import option_menu
from openai_client import get_openai_client, get_openai_response


def get_openai_api_key():
    if "api_key" not in st.session_state:
        st.session_state.api_key = None

    if not st.session_state.api_key:
        api_key = st.text_input(
            "Enter your OpenAI API key to get started:", type="password"
        )
        if api_key:
            st.session_state.api_key = api_key
            st.experimental_rerun()


def parse_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    pdf_text = ""

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()

    return pdf_text


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
            st.title("Analyze Resume")
            st.write("Upload your resume and job description for response.")

            api_key = st.session_state.api_key
            client = get_openai_client(api_key)

            st.header("Step 1: Upload Your Resume")

            resume_file = st.file_uploader("Upload your PDF resume", type=["pdf"])

            resume_text = ""
            if resume_file is not None:
                try:
                    resume_text = parse_pdf(resume_file)
                    st.success("Resume uploaded and parsed successfully!")
                except Exception as e:
                    st.error(f"Error parsing the resume: {e}")

            st.header("Step 2: Enter the Job Description")

            job_description_file = st.file_uploader(
                "Upload your job description", type=["pdf"]
            )

            job_description_text = ""
            if job_description_file is not None:
                try:
                    job_description_text = parse_pdf(job_description_file)
                    st.success("Job description uploaded and parsed successfully!")
                except Exception as e:
                    st.error(f"Error parsing the job description: {e}")

            st.header("Resume and Job Description Breakdown")
            if resume_text and job_description_text:
                with st.spinner("Analyzing Your Resume..."):
                    try:
                        result = get_openai_response(
                            client, resume_text, job_description_text
                        )

                        response = json.loads(result)

                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("% of Qualifications Met")
                            st.text(f'{response["qualification_match_percentage"]}%')

                        with col2:
                            st.subheader("Resume Gaps")
                            for skill_gap in response["resume_gaps"]:
                                wrapped_text = textwrap.fill(
                                    textwrap.dedent(skill_gap),
                                    width=35,
                                    subsequent_indent=" " * 2,
                                )
                                st.text("• " + wrapped_text)

                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("Top 5 Resume Keywords")
                            for resume_keyword in response["top_5_resume_keywords"]:
                                st.text(f"• {resume_keyword}")

                        with col2:
                            st.subheader("Top 5 Job Keywords")
                            for resume_keyword in response["top_5_job_keywords"]:
                                st.text(f"• {resume_keyword}")

                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("Resume Experience")
                            for skill in response["resume_experience"]:
                                wrapped_text = textwrap.fill(
                                    textwrap.dedent(skill),
                                    width=35,
                                    subsequent_indent=" " * 2,
                                )
                                st.text("• " + wrapped_text)

                        with col2:
                            st.subheader("Job Requirements")
                            for skill in response["job_requirements"]:
                                wrapped_text = textwrap.fill(
                                    textwrap.dedent(skill),
                                    width=35,
                                    subsequent_indent=" " * 2,
                                )
                                st.text("• " + wrapped_text)

                        st.subheader("Recommendations")
                        for recommendation in response["recommendations"]:
                            wrapped_text = textwrap.fill(
                                textwrap.dedent(recommendation),
                                width=75,
                                subsequent_indent=" " * 2,
                            )
                            st.text("• " + wrapped_text)

                    except Exception as e:
                        st.error(f"Error during response: {e}")
            else:
                st.warning(
                    "Please ensure you have entered both the resume and job description."
                )

    elif selected == "Resume Resources":
        st.title("Resume Resources")
        st.write("Access useful resources for creating a great resume.")


if __name__ == "__main__":
    run_streamlit_app()
