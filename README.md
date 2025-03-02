# Resume Customiser

## Introduction
The Resume Customiser is an AI-powered application designed to help job seekers tailor their CVs to specific job descriptions.

## Getting Started

### Prerequisites
- Git
- Python 3.8+
- Node.js and npm

### Clone the Repository
```bash
git clone https://github.com/enendufrankc/CV-Customiser.git
cd CV-Customiser
```

### Backend Setup

1. Navigate to the backend directory:
    ```bash
    cd backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file from the `.env.example` file and fill in the necessary environment variables:
    ```bash
    cp .env.example .env
    ```

5. Run the backend server:
    ```bash
    python app.py
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the required npm packages:
    ```bash
    npm install
    ```

3. Run the frontend development server:
    ```bash
    npm run dev
    ```

### Access the Application
- The frontend will be running at `http://localhost:5174`
- The backend API will be running at `http://localhost:8000`

## Additional Information
- Ensure that the backend server is running before starting the frontend server.
- Refer to the documentation for more details on the project structure and functionality.
