# Getting started with Django
https://www.djangoproject.com/start/


This guide will walk you through installing Git, Python, and Django on a Windows computer. No prior experience is required.

---

## 1. Install Git

Git is a version control system that lets you track code changes and collaborate with others.

### Steps:
1. Go to the official Git website: [https://git-scm.com/download/win](https://git-scm.com/download/win)
2. The download should start automatically for Windows. Run the installer once it finishes.
3. During installation:
   - **Select default options** unless you know you need something specific.
   - Recommended: Keep **"Use Git from the command line"** option checked.
4. Finish installation and restart your computer if required.

### Verify Installation:
Open **Command Prompt** or **PowerShell** and type:
```sh
git --version
```
You should see something like:
```
git version 2.45.0.windows.1
```

---

## 2. Install Python

Python is the programming language Django runs on.

### Steps:
1. Download Python from the official website: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
   - Choose the latest stable release (not a beta).
2. Run the installer.
   - **Important:** Check the box **“Add Python to PATH”** before clicking *Install Now*.
3. Wait for installation to complete.

### Verify Installation:
Open **Command Prompt** and type:
```sh
python --version
```
Expected output:
```
Python 3.12.5
```
(or something similar)

Also verify `pip` (Python package manager) is installed:
```sh
pip --version
```

---

## 3. Install Django

Django is a web framework built with Python.

### Steps:
1. Open **Command Prompt**.
2. Create a project folder (optional but recommended):
```sh
mkdir django_projects
cd django_projects
```
3. (Optional but recommended) Create a virtual environment:
```sh
python -m venv .venv
```
Activate it:
```sh
.venv\\Scripts\\activate
```
4. Install Django using pip:
```sh
pip install django
```

### Verify Installation:
Check the installed version:
```sh
django-admin --version
```

---

## 4. Create Your First Django Project

1. Inside your project folder, run:
```sh
django-admin startproject my_test_01
cd my_test_01
```
2. Start the development server:
```sh
python manage.py runserver
```
3. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
   - You should see the Django welcome page

---

## 5. Summary

- **Git** helps you manage code versions.
- **Python** is the language Django uses.
- **Django** is the framework for building web apps.
- You’re now ready to start developing with Django on Windows!

---

## Next Steps

- Explore Django documentation: [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
- Clone this repository: `git clone https://github.com/jorgec/cpc_it300-2025-django_001.git`
