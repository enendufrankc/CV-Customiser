# Project Overview

## Introduction
The **Resume Customiser** is an AI-powered application designed to help job seekers tailor their CVs to specific job descriptions. By leveraging advanced Large Language Model (LLM) capabilities, users can upload their existing CVs alongside a job description, and the system will generate **three optimized resume versions**. This ensures higher compatibility with Applicant Tracking Systems (ATS) and better alignment with employer expectations.

## Key Flow

1. **User Uploads Resume & Job Description**  
   - Users provide an existing CV (PDF/DOCX) and the target job description.

2. **AI Processing & Customisation**  
   - The system extracts key information from the CV.  
   - It analyzes the job description to identify important keywords and requirements.  
   - AI then generates three variations of the CV:
     - **ATS-Optimized Version:** Focused on keyword matching for ATS systems.  
     - **Concise Professional Version:** Highlights core strengths in a streamlined format.  
     - **Creative Version:** Offers a visually engaging layout suitable for more design- or networking-oriented roles.

3. **User Review & Refinement**  
   - Users can preview all three versions.  
   - Optional manual edits before finalizing.

4. **Download & Application**  
   - Users download the customized resumes in preferred formats (PDF/DOCX).  
   - Optionally, the system can provide **cover letter suggestions** if needed.

## Tech Stack

### Frontend
- **Framework:** [Streamlit](https://streamlit.io/)  
- **UI Components:** [shadcn/ui](https://ui.shadcn.com/)  
- **Styling:** [Tailwind CSS](https://tailwindcss.com/)  
- **Icons:** [Lucide Icons](https://lucide.dev/)

### Backend
- **Language:** Python  
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (for high-performance API development)

### Authentication
- **Streamlit-Authenticator** for user login and access control.

### AI & NLP
- **LLM API:** [Azure OpenAI API](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service) (for text generation, keyword analysis, and optimization)


# Core Functionality

## 1. User Registration & Login
- **Email/Password Registration**  
  - Users can create an account with a valid email address and a secure password.
- **Social Login**  
  - Users may sign up or log in via **Google** or **LinkedIn**.
- **Account Management**  
  - Once registered, users can update personal details (e.g., name, email) within the application.

## 2. Home Page / Profile Dashboard
- **User Profile Overview**  
  - Displays user information and a summary of previously generated or edited resumes.
- **Upload CV & Job Description**  
  - Users upload their existing resume in PDF or DOCX format.
  - Job description can be:
    - **Pasted as text**, or
    - **Provided as a URL** (the system scrapes the job listing page to extract relevant content).

## 3. Template Recognition & Preservation
- **Layout Analysis**  
  - The AI scans the uploaded resume to understand its existing formatting (section headings, bullet points, fonts, etc.).
- **Preserve Structure**  
  - While tailoring the text to the new job description, the system retains the original layout and design elements of the user’s CV.
- **Adaptive Editing**  
  - If the user opts for a creative or alternative style, the system can still maintain key structural elements (e.g., sections, headings) to keep the document organized.

## 4. Web Scraping for Job Description
- **Link Parsing**  
  - Upon receiving a URL, the system automatically fetches the job description from the web page.
- **Content Cleaning**  
  - The text is scrubbed of extraneous ads, HTML tags, or unrelated content, ensuring only relevant details are extracted.

## 5. Resume Generation & AI Processing
- **Analysis of CV & Job Description**  
  - The system parses the existing CV for relevant sections (education, experience, skills) and identifies key terms from the job description.
- **Three Tailored Variations**  
  - **ATS-Optimized Version:** Emphasizes keywords and phrasing for effective applicant tracking system scans.  
  - **Concise Professional Version:** A streamlined, business-friendly style focusing on major accomplishments.  
  - **Creative Version:** A visually distinctive layout, particularly suited for design or networking roles.
- **Maintaining the Original Template**  
  - Each variation can preserve the user’s existing layout/branding unless the user chooses to adopt a different style.

## 6. Editing & Customization
- **Comparison & Preview**  
  - Users review all three AI-generated variations side by side.
- **Section-by-Section Editing**  
  - Users can update any text area (summary, work experience, skills) while keeping the document structure intact.
- **Live Preview**  
  - Changes reflect in real time, allowing the user to see exactly how the final resume will look.

## 7. Download & Finalization
- **Export Options**  
  - Users can download the chosen (or edited) resume(s) in PDF or DOCX format.
- **Historical Versions**  
  - The system stores multiple versions of the resume for easy reference and future updates.
- **Optional Cover Letter Support**  
  - The AI can generate a relevant cover letter draft based on the final resume and job description.


# Documentation

Below is a collection of resources, links, and references critical for developing, testing, and deploying the Resume Customiser application.

## 1. Code Repositories
- **Project GitHub Repository:** [GitHub.com/username/resume-customiser](#)  
  - Contains the main application codebase (frontend + backend).
  - Issues, pull requests, and project documentation (README, CONTRIBUTING) are managed here.

## 2. Framework & Library Documentation

### Frontend
- **Streamlit**  
  - [Official Documentation](https://docs.streamlit.io/)  
  - Guidance on building interactive UI elements and deploying Streamlit apps.
- **Shadcn/ui**  
  - [Official Documentation](https://ui.shadcn.com/)  
  - Provides pre-built, accessible components; usage guides and component customization.
- **Tailwind CSS**  
  - [Official Documentation](https://tailwindcss.com/docs)  
  - Usage instructions for utility-first CSS classes, theming, and responsive design.
- **Lucide Icons**  
  - [Official Documentation](https://lucide.dev/)  
  - Icon library usage, installation methods, and customization tips.

### Backend
- **Python**  
  - [Python 3 Official Docs](https://docs.python.org/3/)  
  - Reference for language syntax, standard library modules, and best practices.
- **FastAPI**  
  - [Official Documentation](https://fastapi.tiangolo.com/)  
  - Covers API routing, dependency injection, async I/O, security, and deployment.

### Authentication
- **Streamlit-Authenticator**  
  - [Streamlit-Authenticator GitHub](https://github.com/mkhorasani/Streamlit-Authenticator)  
  - Setup and usage instructions for user authentication within Streamlit applications.

### AI & NLP
- **Azure OpenAI API**  
  - [Azure OpenAI Service Docs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/)  
  - Guidance on API endpoints, authentication, usage quotas, and best practices for text generation.

## 3. Additional Documentation & References
- **Resume Template Preservation**  
  - Internal guidelines on how to parse and maintain PDF/DOCX structure (linked from your repository's Wiki or a dedicated documentation folder).
- **Web Scraping**  
  - If using a Python library like [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) or [Requests-HTML](https://requests-html.kennethreitz.org/), reference official docs for scraping best practices.
- **Continuous Integration / Continuous Deployment (CI/CD)**  
  - Documentation for your chosen CI/CD pipeline (e.g., [GitHub Actions Docs](https://docs.github.com/en/actions), Jenkins, or Azure DevOps).

## 4. Internal Team Notes
- **Project Wiki**  
  - A dedicated Wiki (or Notion/Confluence space) for architecture diagrams, detailed user stories, and sprint documentation.
- **Meeting Notes & Roadmap**  
  - Hosted in your preferred project management tool (e.g., Jira, Trello, or GitHub Projects).  
  - Outlines planned features, timelines, milestones, and retrospective findings.

---

**Note:**  
All documentation should be kept updated to reflect any changes in technology, libraries, or architectural decisions throughout the development lifecycle. This ensures the entire team remains aligned on how to build, maintain, and scale the Resume Customiser application.


## Current File Structure

.
├── README.md
├── LICENSE
├── .gitignore
├── setup.py
├── tests
│   └── test_resume_customiser.py
├── .env.example
├── .github
│   └── workflows
│       └── ci.yml
├── main.py
├── requirements.txt
├── config
│   └── config.yaml
├── Dockerfile
├── docs
│   └── GET_STARTED.md
├── app.py
├── research
│   ├── resume_experiment.ipynb
│   └── scraper_experiment.ipynb
├── data
│   ├── sample_job_descriptions.txt
│   └── cache
├── pages
│   # (Place any Streamlit pages or additional files here)
└── resume_customiser
    └── src
        ├── __init__.py
        ├── client
        │   ├── __init__.py
        │   ├── llm_client.py
        │   └── db_client.py
        ├── scraper
        │   ├── __init__.py
        │   └── scraper_client.py
        ├── components
        │   ├── __init__.py
        │   ├── resume_customiser_components.py
        │   └── cover_letter_components.py
        ├── agents
        │   ├── __init__.py
        │   └── resume_agent.py
        ├── prompt
        │   ├── __init__.py
        │   ├── prompt_loader.py
        │   └── templates
        └── utils
            ├── __init__.py
            └── common.py

