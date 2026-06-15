# 📝 TodoManager

A modern and responsive Todo Management Web Application built using **Django**, **MySQL**, and **Bootstrap/Crispy Forms**..

The application allows users to create accounts, securely log in, manage daily tasks, mark tasks as completed, edit existing tasks, and delete tasks with an attractive glassmorphism user interface.

---

## 🚀 Features

### 🔐 Authentication System

* User Registration
* User Login
* User Logout
* Password Validation
* Session Management

### ✅ Task Management

* Add New Tasks
* View Tasks
* Update Tasks
* Delete Tasks
* Mark Task as Completed
* Mark Task as Pending

### 🎨 Modern User Interface

* Glassmorphism Design
* Responsive Navigation Bar
* Mobile Friendly Layout
* Animated Components
* Beautiful Gradient Background

### 📄 Pagination

* Navigate through tasks efficiently
* Previous / Next Page Support
* First / Last Page Navigation

### 🔔 Notification System

* Success Messages
* Error Messages
* Warning Messages
* Auto-hide Alerts

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive Design

### Backend

* Django 5.x
* Python 3.x

### Database

* MySQL

### Authentication

* Django Authentication System

### Form Handling

* Django Crispy Forms
* Crispy Bootstrap 5

---

# 📂 Project Structure

```text
Todo_mag/
│
├── Todo_mag/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todolist/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── users/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   └── base.html
│
├── manage.py
└── requirements.txt
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/TodoManager.git

cd TodoManager
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv myenv
```

Activate Environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux/Mac

```bash
source myenv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install django
pip install mysqlclient
pip install django-crispy-forms
pip install crispy-bootstrap5
```

---

## 4️⃣ Configure Database

Open:

```python
settings.py
```

Configure MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_1_todolist',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 5️⃣ Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7️⃣ Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 📸 Screenshots

### Home Page

* Responsive Hero Section
* Animated Navbar
* Glassmorphism UI

### Todo Dashboard

* Task Listing
* Pagination
* CRUD Operations

### Login Page

* Secure Authentication
* Responsive Design

### Registration Page

* User Creation Form
* Password Validation

---

# 🔑 Authentication URLs

| URL                | Description   |
| ------------------ | ------------- |
| /account/register/ | Register User |
| /account/login/    | Login User    |
| /account/logout/   | Logout User   |

---

# 📌 Future Enhancements

* Profile Management
* Password Reset
* Email Verification
* Dark/Light Theme Toggle
* Search Tasks
* Task Categories
* Task Priorities
* Due Dates
* REST API Integration
* Docker Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork Repository
2. Create New Branch

```bash
git checkout -b feature-name
```

3. Commit Changes

```bash
git commit -m "Added New Feature"
```

4. Push Branch

```bash
git push origin feature-name
```

5. Open Pull Request

---

# 👨‍💻 Author

**Shubham Tidke**

Computer Engineering Student

Savitribai Phule Pune University (SPPU)

Passionate about:

* Web Development
* Django
* Data Science
* Competitive Programming

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

Happy Coding 🚀

