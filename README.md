🐍 ManageMyDocument – Backend README (Django + DRF + Render)

A pragmatic backend that securely handles auth, documents, and AI Q&A.

✨ Overview

ManageMyDocument (Backend) is a Django REST API that supports:

JWT auth (register/login/logout)

Document CRUD (PDF/DOCX/TXT) linked per user

AI Q&A: extracts text and answers questions via Gemini; optional paraphrase via Hugging Face

Live (Render): e.g., https://ManageMyDocument-backend.onrender.com

Replace with your actual deployment URL.

👤 For Non‑Technical Users

You usually don’t access this service directly. Use the Frontend website. This API powers the app behind the scenes.

🧑‍💻 For Developers

Tech Stack

Django 5+, Django REST Framework

DB: SQLite (dev) / PostgreSQL (Render)

Auth: JWT (e.g., djangorestframework-simplejwt)

Storage: Local (dev) / Render disk or cloud storage

AI Services: Gemini API, Hugging Face Inference API

Prerequisites

Python ≥ 3.11, pip, virtualenv

PostgreSQL if using prod DB locally (optional)

Quick Start (Local)

# 1) Clone
git clone https://github.com/yourname/ManageMyDocument-backend-git.git
cd ManageMyDocument-backend-git

# 2) Create & activate venv
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3) Install deps
pip install -r requirements.txt

# 4) Env setup
cp .env.example .env
# edit .env with keys and DB URL (optional)

# 5) Migrate & run
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

Environment Variables

Create .env (load with django-environ or similar):

# Django
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# CORS
CORS_ALLOWED_ORIGINS=https://ManageMyDocument-frontend.netlify.app,http://localhost:5173

# Database (use sqlite by default; uncomment for Postgres)
# DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DBNAME

# File uploads
MAX_UPLOAD_MB=25

# AI keys (kept on server; never expose to client)
GEMINI_API_KEY=your_gemini_key
HF_API_KEY=your_huggingface_key

# JWT settings (if overriding defaults)
ACCESS_TOKEN_LIFETIME_MIN=30
REFRESH_TOKEN_LIFETIME_DAYS=7

File Handling

Accepts PDF/DOCX/TXT.

Extracts text (e.g., pdfminer.six, python-docx); plaintext as fallback.

Files linked to request.user and never exposed to others.

API Endpoints

Auth

POST /register/ → { email, password } → Creates user

POST /login/ → { email, password } → { access, refresh? }

POST /logout/ → Invalidates session/refresh (implementation-dependent)

Documents

GET /documents/ → List current user’s documents

POST /documents/ → Upload form-data: file=<binary>, name?=<string>

PUT /documents/<id>/ → Rename: { name: "New Name" }

DELETE /documents/<id>/ → Remove user’s document

AI

POST /ask/ → { document_id, question } → { answer, sources? }

Example Upload (curl)

curl -X POST \
  -H "Authorization: Bearer <ACCESS>" \
  -F "file=@/path/to/file.pdf" \
  -F "name=My Report" \
  https://ManageMyDocument-backend.onrender.com/documents/

Security

JWT required for all document/AI endpoints.

Validate ownership on every document operation.

Enforce size/type limits; scan or sanitize text extraction errors.

Rate-limit /ask/ to control AI spend; log prompts/responses with PII scrubbing.

Local Dev Tips

Enable CORS for Netlify preview & localhost.

Use DEBUG=True only locally.

Add sample data via Django admin or fixtures.

Write DRF tests for auth, uploads, and /ask/.

Deployment (Render)

Create Web Service → connect GitHub repo.

Build Command: pip install -r requirements.txt && python manage.py collectstatic --noinput

Start Command: gunicorn config.wsgi:application --preload --workers=2 --timeout=120

Set env vars from above in Render → Environment.

Add PostgreSQL (optional) → set DATABASE_URL.

Configure CORS_ALLOWED_ORIGINS to include your Netlify URL.

Persist uploads: use Render disk (basic) or external storage (S3, etc.).

Error Handling & Logging

Standard DRF error responses with helpful messages.

Structured logging (JSON) for server logs.

4xx for client issues, 5xx for server issues.

Testing

pytest -q
# or
python manage.py test

Rate Limits & Quotas

Implement per-user limits (e.g., N questions/day).

Cache answers per (doc, question) to reduce spend.

FAQ

Q: Where are files stored?A: Locally in dev; on Render disk or cloud storage in production.

Q: Do I need API keys locally?A: Only for the /ask/ endpoint. You can stub responses in dev.

Q: Can I extend supported file types?A: Yes—add a parser and update validation.

📚 References

Google AI Gemini (Free Tier)

Hugging Face Inference API

Django REST Framework

Netlify Docs

Render Docs
