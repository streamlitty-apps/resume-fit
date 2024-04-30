Resume Fit
==============================

Resume Fit is a tool designed to help users improve their resume based on the job they're applying to. Using OpenAI GPT-3.5, the app generates a breakdown of a a given resume to a given job description.

Requirements
------------

* python: 3.11.0
* [OpenAI API-KEY](https://platform.openai.com/docs/api-reference/api-keys)

Getting Started
------------

1. `git clone git@github.com:streamlitty-apps/resume-fit.git`
2. `cd resume-fit`
3. `pip install -r requirements.txt`
4. `streamlit run app/streamlit_app.py`

Deploying to Streamlit Cloud
------------

1. Push this project to a [GitHub repository](https://github.com/)

2. [Create a free Streamlit Cloud account](https://share.streamlit.io/)

3. Click "New app" in the upper-right corner of your workspace

4. Connect your GitHub account

5. Choose the repository containing your project

6. Set the main file as `streamlit_app.py`

7. Deploy!

Project Organization
------------

Below is a breakdown of the files in this project, with additional information to help you understand their roles and how they fit into the overall structure:

    ├── app/
    │   ├── helpers/
    │   │   └── file_utils.py <- Helper module for uploading and parsing files
    │   │   └── openai_client.py <- Helper module for interacting with OpenAI services
    │   ├── views/
    │   │   └── analyze_resume_page.py <- The page where users analyze their resume
    │   │   └── initial_page_load.py <- What users see on the initial page load
    │   └── streamlit_app.py     <- This is the main file that runs the Streamlit app
    |
    ├── README.md                <- The main README file to help you get started
    |
    ├── .gitignore               <- This file tells Git which files and directories to ignore
    |
    ├── requirements.txt         <- A list of Python packages that the project depends on


Future Considerations
------------
As this project continues to evolve, here are some future considerations that could enhance its functionality, scalability, and user experience:

- **Multiple File Uploads**: Allow for files other than PDFs to be uploaded
- **Text Input**: Allow users the option to enter raw text as opposed to a file upload
- **Resume Resouces**: Add a page that provides links to resources based on the recommendations
- **Add Unit Test**: Add unit tests to the code functionality
------------

<p><small>Project started at 🐙<a target="_blank" href="https://www.lonelyoctopus.com/">Lonely Octopus</a>🐙 and updated by me!</small><p>