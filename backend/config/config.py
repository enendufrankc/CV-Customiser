from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    
    SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")