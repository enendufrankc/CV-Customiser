from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
import tempfile
from src.tool.tool import customiser_content
from src.agents.resume_agent import get_completion

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(
    url: str = Form(...),
    source: UploadFile = File(...)
):
    # Save the uploaded file temporarily
    suffix = os.path.splitext(source.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await source.read())
        tmp_path = tmp.name

    # Process the temporary file along with the provided URL
    job_description, resume_content = customiser_content(tmp_path, url)
    result = get_completion(resume_content, job_description)
    
    # Remove the temporary file after processing
    os.remove(tmp_path)
    
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
