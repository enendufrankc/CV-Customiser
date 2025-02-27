from openai import AzureOpenAI
from config.config import Config

config = Config()



def get_openai_client():
    endpoint = config.AZURE_OPENAI_ENDPOINT
    deployment = config.AZURE_OPENAI_DEPLOYMENT
    openai_api_key = config.AZURE_OPENAI_API_KEY
    
    openai_client = AzureOpenAI(
        azure_endpoint=endpoint,  
        api_key=openai_api_key,  
        api_version='2024-05-01-preview'
        )
    return openai_client