### Python Configuration:
1. You need to install Python from https://www.python.org/downloads/.
2. Once you install Python, run the following commands:
    In Windows:
```Shell
    python -m venv venv
    cd venv/scripts
    activate
    cd ..
    cd ..
    pip install -r requirements.txt
```
    In Linux:
```Shell
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
```
### Postgresql Configuration:
1. You need to install Postgresql in your machine from https://www.postgresql.org/download/.
2. Once you install Postgresql, run the following:

```Shell
    psql
```
```SQL
    CREATE DATABASE todo;
    CREATE USER todouser WITH ENCRYPTED PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE todo TO todouser;
```
### Environment variables configuration:
1. Create a file with the name .env and follow the structure of .env_example. E.g:
```Shell
DATABASE_USER=todouser
DATABASE_NAME=todo
DATABASE_PASSWORD=password
DATABASE_PORT=5432
```
### Migrate to database and run project:
1. Run the following command to insert your tables to the Postgresql database and run your projects:

```Shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

2. Open your browser into the following link; http://127.0.0.1:8000/api/schema/swagger-ui/#/.

### Navigating the API with Swagger UI
1. First, create your account in <a href="http://127.0.0.1:8000/api/schema/swagger-ui/#/sign-up/sign_up_create" target="_blank">/api/sign-up/</a>
