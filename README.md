# helix-agentic-recruiter

This project is a simple AI-powered recruiter assistant that:

- Lets you chat to create outreach sequences.
- Dynamically displays AI responses.
- Allows easy editing.

## Technologies Used

- Frontend: React + TypeScript
- Backend: Flask + Python
- Database: SQLite
- OpenAI API for AI responses
---

## Requirements / Dependencies

Make sure you have these installed **before** running:

- **Python 3.8+**
- **Node.js** (v16 or later recommended)
- **npm** (comes with Node.js)
- **OpenAI API key** (Set as environment variable `OPENAI_API_KEY`)
- (Optional) **Git** installed to clone the repository easily.

Backend dependencies (installed automatically by pip):
- Flask
- Flask-CORS
- openai
- sqlite3 (comes built-in with Python)

Frontend dependencies (installed automatically by npm):
- React
- React DOM
- TypeScript
- Axios

---

> ⚡ Tip: If you encounter any issues, double-check your Python or Node versions.


## How to run locally

```bash
## 1. Clone the repository
git clone https://github.com/Oshintiwari/helix-agentic-recruiter.git
cd helix-agentic-recruiter

## Backend Setup
cd backend
python -m venv venv
source venv/Scripts/activate  # (Windows)
pip install -r requirements.txt
python app.py
# Backend will run at: http://127.0.0.1:5000

# Open a new terminal for frontend

## Frontend Setup
cd ../frontend
npm install
npm start
# Frontend will run at: http://localhost:3000

---
