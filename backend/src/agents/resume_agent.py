from config.config import Config
from src.client.llm_client import get_openai_client
from src.prompt.prompt_model import CV
from src.prompt.prompt_loader import system_prompt
from src.tool.tool import customiser_content
import json

config = Config()
client = get_openai_client()


def get_completion(cv_text, job_description):
    base_system_prompt = system_prompt()
    json_schema = json.dumps(CV.model_json_schema(), indent=2)
    system_msg = base_system_prompt.replace("{schema}", json_schema)

    retrieved_text = f"**this is the CV Text**\n{cv_text}\n\n**this is the Job Description**\n{job_description}"
    deployment = config.AZURE_OPENAI_DEPLOYMENT
    completion = client.chat.completions.create(
        model=deployment,
        response_format={"type": "json_object"}, 
        messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": (
            f"Please call the generate_custom_resume function with the following inputs:\n\n"
            f"CV Text: {cv_text}\n\n"
            f"Job Description: {job_description}"
        )}
    ],
        max_tokens=4096,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    content = completion.choices[0].message.content
    content = json.loads(content.strip("```"))
    return content