from openai import OpenAI


DEFAULT_MODEL = "gpt-3.5-turbo"
SYSTEM_PROMPT = "You're an expert in resume analysis with expertise in matching candidates to job requirements."

resume_analysis_schema = {
    "skills_from_resume": list,
    "skills_from_job_description": list,
    "matches": list,
    "gaps": list,
    "qualification_percentage": int,
    "recommendations": list,
}


def validate_openai_api_key(api_key):
    try:
        client = get_openai_client(api_key=api_key)
        client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "this is a test",
                }
            ],
            max_tokens=1,
            n=1,
        )
        return True
    except Exception:
        return False


def get_openai_client(api_key):
    """
        Retrieves an instance of the OpenAI client using the provided API key.
    walk
        Args:
            - api_key (str): The API key for accessing the OpenAI service.

        Returns:
            - OpenAI: An instance of the OpenAI client.

        Raises:
            - ValueError: If the API key is not provided.
    """
    if not api_key:
        raise ValueError(
            "OpenAI API key is not set. Please set it in your environment variables."
        )
    return OpenAI(api_key=api_key)


def get_openai_response(client, resume, job_description, model=DEFAULT_MODEL):
    """
    Retrieves a response from the OpenAI chat model based on the given text prompt.

    Args:
        - client (OpenAI.Client): The OpenAI client object used to make API requests.
        - resume (str): The resume text.
        - job_description (str): The job description text.
        - model (str, optional): The model to use for generating the response. Defaults to DEFAULT_MODEL.

    Returns:
        - str: The generated response from the chat model.

    Raises:
        - ValueError: If resume or job_description is empty or None.
    """
    if not resume and not job_description:
        raise ValueError("Both resume and job description must be provided.")

    prompt = f"""
    Given the following resume and job description:

    Resume:
    {resume}

    Job Description:
    {job_description}

    Compare the resume against the job description, and provide a response that follows the exact structure / format as below:

    {{
    "qualification_match_percentage": MATCH_PERCENTAGE,
    "resume_gaps": LIST OF GAPS ON RESUME COMPARED TO JOB DESCRIPTION,
    "top_5_resume_keywords": LIST TOP 5 RESUME KEYWORDS,
    "top_5_job_keywords": LIST TOP 5 JOB DESCRIPTION KEYWORDS,
    "resume_experience": LIST OF SUMMARIZED RESUME HIGHLIGHTS AND EXPERIENCES,
    "job_requirements": LIST OF SUMMARIZED JOB REQUIREMENTS AND SKILLS,
    "recommendations": LIST OF RECOMMENDATIONS TO MAKE RESUME BETTER FIT THE JOB DESCRIPTION
    }}

    Ensure your response adheres to this exact structure. Verify all components are included before submission.
    """

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0, n=1
    )

    return response.choices[0].message.content
