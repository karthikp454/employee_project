##Employee Management System (Django + DRF)

A Django + Django REST Framework project for managing **Employees**, **Departments**, **Attendance**, and **Performance** with JWT auth, filtering, pagination, and Swagger documentation.

##Features

- CRUD APIs for Employees, Departments, Attendance, Performance
- Filtering, search, ordering, and pagination
- JWT Authentication (obtain/refresh)
- Swagger UI at `/swagger/`
- Fake data seeding via management command
- (Optional) PostgreSQL; SQLite fallback included

##Tech Stack

- Python 3.11+
- Django 4.x, Django REST Framework
- Postgres (psycopg2-binary) or SQLite
- drf-yasg (Swagger), django-filter, django-environ, Faker
- djangorestframework-simplejwt (JWT)

##Quick Start

> **Prerequisites:** Python 3.11+.  
> **Database:** You can use **PostgreSQL** (recommended) or **SQLite** (fallback, no setup).

##Clone and Open

```bash
git clone https://github.com/karthikp454/employee_project
cd <your-repo>
```
