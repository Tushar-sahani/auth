# auth
Simple User Authentication using Django

## Functionality

- Registration
- Login
  - via username & password
- View Profile
- Log out

## Installing

### Clone the project

```git
git clone https://github.com/Tushar-sahani/auth.git
```

### Install dependencies & activate venv

unix / mac

``` python
python3 -m pip install --user virtualenv
```

windows

```python
python -m pip install virtualenv
```

create a virtual environment

unix / mac

```python
python3 -m venv env
```

windows

```python
python -m venv env
```

And tell pip to install all of the packages in this file using the -r flag:

unix / mac

``` python
python3 -m pip install -r requirements.txt
```

windows

```python
python -m pip install -r requirements.txt
```

### Configure the settings

1. Edit `auth/settings.py` if you want to use any other Database.

2. Apply migrations

### Run the Project

Just run this command:

``` python
python manage.py runserver
```
