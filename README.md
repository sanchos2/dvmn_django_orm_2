# Bank security console

This is an internal repository for Siyanie bank employees. If you got into this repository by accident, then you cannot 
start it without access to the database, but you can freely use 
the layout code or see how queries to the database are implemented.

The security console is a site that can be connected to a remote database with visits and pass cards of our bank employees.

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

### How to setup

Install python3

```sh
sudo apt install python3
sudo apt install python3-pip
```

Download the project, create virtual environment and install dependencies

```sh
git clone https://github.com/sanchos2/dvmn_django_orm_2.git
cd dvmn-django-orm_2
python -m venv venv
source venv/bin/activate.sh
pip install -r requirements.txt
```

Add environment variables:

```
DB_HOST=database server address
DB_PORT=database server port
DB_NAME=database name
DB_USER=database user
DB_PASSWORD=database password
SECRET_KEY=secret key
DEBUG=True
USE_L10N=True
LANGUAGE_CODE=en-US
TIME_ZONE=UTC
USE_TZ=True
```
note: on production environment setup DEBUG to False

### How to run

Run project

```sh
python manage.py runserver
```

GOTO http://127.0.0.1:8000

### Project Goals

The code is written for educational purposes on online-course for web-developers [devman](https://dvmn.org/modules/django-orm/) (lesson 2)