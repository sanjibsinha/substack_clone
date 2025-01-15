![The First Version](https://github.com/sanjibsinha/substack_clone/blob/main/Screenshot%20from%202025-01-15%2010-42-24.png)

## Step 1: Initialize the Project

### Backend (Django)
1. **Create the Project:**
   ```bash
   
   sudo apt install python3.10-venv
   python3.10 -m venv stackenv
   
   source stackenv/bin/activate  # For Mac/Linux
   stackenv\Scripts\activate  # For Windows
   
   pip install django

   django-admin startproject substack_clone
   cd substack_clone
   python manage.py startapp stack
   ```
2. **Update `settings.py`:**
   - Add `'stack'` to `INSTALLED_APPS`.
   - Set `DATABASES` to SQLite (default).

3. **Run Initial Setup:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser
   python3 manage.py runserver
   ```
   Your backend is now set up and running at `http://127.0.0.1:8000/`.

---

## Step 2: Frontend Structure (HTML, CSS, JS)

### Create Basic Directory Structure:
```plaintext
main/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── script.js
├── templates/
│   └── index.html
└── views.py
```

---

### **HTML Layout (`index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Substack Clone</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/subscribe/">Subscribe</a>
            <a href="/login/">Login</a>
        </nav>
    </header>

    <main>
        <section class="hero">
            <h1>Welcome to Substack Clone</h1>
            <p>Read, Write, and Share Stories</p>
            <a href="/subscribe/" class="cta-button">Subscribe Now</a>
        </section>
    </main>

    <footer>
        <p>© 2025 Substack Clone. All rights reserved.</p>
    </footer>
</body>
</html>
```

---

### **CSS (`styles.css`):**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    line-height: 1.6;
}

header {
    background: #333;
    padding: 1rem;
    text-align: center;
}

header nav a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}

.hero {
    text-align: center;
    padding: 100px;
    background: #f4f4f4;
}

.cta-button {
    display: inline-block;
    padding: 10px 20px;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}

footer {
    text-align: center;
    padding: 1rem;
    background: #333;
    color: white;
}
```

---

### **Django View (`views.py`):**
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

### **URL Configuration (`urls.py`):**
```python
from django.urls import path
from stack import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

---

### **Run Your Project:**
```bash
python manage.py runserver
```

- Visit `http://127.0.0.1:8000/` to see your homepage.
