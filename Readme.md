
# Little Lemon Web Application

Little Lemon is a python application, using the Django framework 

## Setup
1. Clone this repository 
2. Create a python environment by typing: ```python -m venv venv```
3. Activate the Virtual Environment by typing : On Windows: ```.\venv\Scripts\activate``` On Linux: ```source tutorial-env/bin/activate```
4. Install Dependencies: ```pip install -r requirements.txt ```
5. Update the ```settings.py``` file.
6. Run database migrations: ```python manage.py migrate```
7. Create a super user by running : ```python manage.py createsuperuser```
7. Run the development server: ```python manage.py runserver```

## Database

For this application to run correctly , please update the settings.py to reflect the correct database configuration. The below is an example of the the database configuration, please update zhe user and password.

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "littlelemon",
        "USER": "your_user",
        "PASSWORD": "your_password",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "OPTIONS": {"init_command": "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}
```


## Testing
```python manage.py test```

