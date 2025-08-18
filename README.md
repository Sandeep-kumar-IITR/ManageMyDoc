# ManageMyDocument Backend

This is the **backend** repository for the Document Management Portal with AI Integration.  
Built using **Django + Django REST Framework**, deployed on **Render**.

---

## 🚀 Features
- JWT-based authentication (login, logout, register)
- Document management API (upload, update, delete, list)
- AI-powered Q&A endpoint using Gemini & Hugging Face APIs
- Secure per-user document storage

---

## 🛠️ Tech Stack
- **Django**
- **Django REST Framework**
- **PostgreSQL (or SQLite for local)**
- **JWT Authentication**
- **Render** (Hosting)

---

## 📦 Installation (Local Development)
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ManageMyDocument-backend.git
   cd ManageMyDocument-backend
   ```

2. Create a virtual environment & activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations & start server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## ⚙️ Environment Setup
Create a `.env` file in the project root with the following:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
GEMINI_API_KEY=your_gemini_api_key
HF_API_KEY=your_huggingface_api_key
```

---

## 📡 API Endpoints
| Method | Endpoint             | Description                |
|--------|----------------------|----------------------------|
| POST   | `/register/`         | Register a new user        |
| POST   | `/login/`            | Obtain JWT token           |
| POST   | `/logout/`           | Invalidate token/session   |
| GET    | `/documents/`        | List user documents        |
| POST   | `/documents/`        | Upload a document          |
| PUT    | `/documents/<id>/`   | Update document name       |
| DELETE | `/documents/<id>/`   | Delete a document          |
| POST   | `/ask/`              | Ask AI about a document    |

---

## 🌐 Deployment
- Hosted on **Render**  
  URL: `https://ManageMyDocument-backend.onrender.com`

---

## 📚 References
- [Django REST Framework Docs](https://www.django-rest-framework.org/)
- [Render Deployment Guide](https://render.com/docs)
