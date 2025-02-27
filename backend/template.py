import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# ------------------------------------------------------------------------
# Define the structure of the project here:
# ------------------------------------------------------------------------

TEMPLATES = [
    {
        "name": "resume_customiser",
        "files": [
            "src/__init__.py",
            "src/client/__init__.py",
            "src/client/llm_client.py",
            "src/scraper/__init__.py",
            "src/scraper/scraper_client.py",
            "src/components/__init__.py",
            "src/components/resume_customiser_components.py",
            "src/components/cover_letter_components.py",
            "src/agents/__init__.py",
            "src/agents/resume_agent.py",
            "src/prompt/__init__.py",
            "src/prompt/prompt_loader.py",
            "src/utils/__init__.py",
            "src/utils/common.py"
        ],
        "directories": [
            "src/prompt/templates",   # For storing prompt template files
        ],
    },
]

PROJECT_FILES = {
    "files": [
        "README.md",
        "LICENSE",
        ".gitignore",
        "setup.py",
        "tests/test_resume_customiser.py",
        ".env.example",
        ".github/workflows/ci.yml",
        "main.py",                 # Entry point if needed
        "requirements.txt",
        "config/config.yaml",
        "Dockerfile",
        "docs/GET_STARTED.md",     # A quickstart guide for new contributors
        "app.py",                  # Possible main Streamlit/FastAPI file
        "research/resume_experiment.ipynb",
        "research/scraper_experiment.ipynb",
        "data/sample_job_descriptions.txt",
    ],
    "directories": [
        "data/cache",
        "pages",                   # If using Streamlit "pages" approach
    ],
}

# ------------------------------------------------------------------------
# File and Directory creation logic:
# ------------------------------------------------------------------------

def create_file(file_path):
    full_path = Path(file_path)
    os.makedirs(full_path.parent, exist_ok=True)
    if not full_path.exists():
        full_path.touch()
        logging.info(f"Created file: {full_path}")

def create_directory(dir_path):
    full_path = Path(dir_path)
    os.makedirs(full_path, exist_ok=True)
    logging.info(f"Created directory: {full_path}")

def create_files(template_list, project_files):
    """
    Creates directories and files based on the specified lists/dictionaries.
    """
    # Create general project directories and files
    for dir_path in project_files["directories"]:
        create_directory(dir_path)

    for file_path in project_files["files"]:
        create_file(file_path)

    # Create template-specific directories and files
    for template in template_list:
        template_dir = Path(template["name"])
        for dir_path in template.get("directories", []):
            create_directory(template_dir / dir_path)
        for file_path in template.get("files", []):
            create_file(template_dir / file_path)

# ------------------------------------------------------------------------
# Main execution:
# ------------------------------------------------------------------------

if __name__ == "__main__":
    create_files(TEMPLATES, PROJECT_FILES)
