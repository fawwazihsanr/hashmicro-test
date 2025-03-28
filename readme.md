# Hashmicro backend test

## Requirements
- Python 3.9
  
## Features

- **Product Management**
  - Create, Read, Update, and Delete (CRUD) operations
  - Barcode and stock management
  - Price tracking

- **User Roles**
  - Manager: Full CRUD access
  - User: Create, Read, Update access
  - Guest: Read-only access

- **Authentication**
  - User login/logout
  - Guest access
  - Role-based permissions

## Installation

1. Install virtualenv: ``pip install virtualenv``
2. Create virtualenv in the directory you are in: ``virtualenv venv`
3. ``source .venv/bin/activate``
4. ``pip install -r requirements.txt``
5. ``./manage.py runserver``
6. go to ```http://localhost:8000/auth/login/```

## Authentication
Use this credentials for login

1. Manager (username: manager, password: manager)
2. User (username: user, password: useraccess)
3. Login as guest

## Module
In this project already have 1 module called stock_opname, with manager access we can install and uninstall.

## Test
run
``manage.py test`` to run all test case
