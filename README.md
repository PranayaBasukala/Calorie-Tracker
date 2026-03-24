# Calorie Tracker – Django Nutrition App

*4th Semester project*

A Django-based web application for tracking nutrition information using the API-Ninjas Nutrition API.

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd calorie_app
```
### 2. Create Virtual Environment & Activate
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
**macOS/Linux**
```
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

-Copy the example file:  
`cp .env.example .env`  
-Edit .env and add your API key:

NUTRITION_API_KEY=your_api_key_here

**Get your API key from:**
https://api-ninjas.com/api/nutrition

### 5. Apply Database Migrations
```bash
python manage.py migrate
```
### 6. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
### 7. Run Development Server
```bash
python manage.py runserver
```

**Access the app at:**
http://127.0.0.1:8000/

## ✨ Features
* User Authentication (Sign Up, Login, Logout)  
* Nutrition lookup via API  
* Food database with nutritional information  
* Admin dashboard for data management

## 🔐 Admin Panel

* Access:
http://127.0.0.1:8000/admin/  
* Login using your superuser credentials.

## 📁 Project Structure
```
Calorie-Tracker/
├── counter/                 # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   ├── admin.py            # Admin configuration
│   └── migrations/         # Database migrations
│
├── foodie/                 # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
│
├── templates/              # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── signup.html
│
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── manage.py               # Django management script
├── requirements.txt        # Dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
└── README.md               # Documentation
```

## 🔑 Requirements
* Python (3.8+ recommended)  
* Django  
* API-Ninjas Nutrition API Key

## 📌 Notes
* Ensure .env file is not committed to Git  
* Add .env to .gitignore  
* Activate virtual environment before running commands
