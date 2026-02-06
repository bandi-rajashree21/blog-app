# Django Blog Application

A full-featured Blog Application built with Django to understand core Django concepts like Models, Views, Templates, Forms, Authentication, Slugs, and CRUD operations.

This project was built step-by-step to learn Django by mapping concepts from Node.js + Prisma ORM into Django’s architecture.

---

## Features

- User authentication (login required to create/edit/delete posts)
- Create, Edit, Delete blog posts
- Slug-based SEO friendly URLs
- Post detail page
- Django Admin panel
- ModelForms for input handling
- CSRF protection
- Authorization (only author can edit/delete)
- Clean project structure

---

---

## Setup Instructions

1. Install Django
```
pip install django
```
2. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
4. Create superuser
```
python manage.py createsuperuser
```
6. Run server
```
python manage.py runserver
```
Visit:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/
