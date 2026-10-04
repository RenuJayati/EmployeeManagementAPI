# Employee Management REST API

A full-stack employee management system built using Python, Django, and Django REST Framework.

## Overview

This project provides a web-based interface and REST API for managing employees and departments.

The system includes authentication, CRUD operations, search, ordering, pagination, and a dashboard for viewing employee information.

## Technologies

- Python
- Django
- Django REST Framework
- SQLite
- HTML
- CSS
- Bootstrap
- Git & GitHub

## Features

- Employee CRUD operations
- Department management
- RESTful API
- User authentication
- API permissions
- Employee search
- Employee ordering
- API pagination
- Django Admin
- Dashboard
- Employee management frontend
- Automated testing

## API Endpoints

### Employees

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | List employees |
| POST | `/api/employees/` | Create employee |
| GET | `/api/employees/{id}/` | Get employee |
| PUT | `/api/employees/{id}/` | Update employee |
| DELETE | `/api/employees/{id}/` | Delete employee |

### Departments

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/departments/` | List departments |
| POST | `/api/departments/` | Create department |
| GET | `/api/departments/{id}/` | Get department |
| PUT | `/api/departments/{id}/` | Update department |
| DELETE | `/api/departments/{id}/` | Delete department |

## Authentication

The API uses Django REST Framework authentication.

Only authenticated users can access the API.

Authentication methods:

- Session Authentication
- Basic Authentication

## Search

Employees can be searched using:

```text
/api/employees/?search=Riya