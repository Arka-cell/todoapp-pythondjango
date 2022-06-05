### Python Configuration:
1-You need to install Python from https://www.python.org/downloads/.
2-Once you install Python, run the following commands:
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
1-You need to install Postgresql in your machine from https://www.postgresql.org/download/.
2-Once you install Postgresql, run the following:

```Shell
    psql
```
```SQL
    CREATE DATABASE todo;
    CREATE USER todouser WITH ENCRYPTED PASSWORD 'password';
    GRANT ALL PRIVILEGES ON DATABASE todo TO todouser;
```
### Environment variables configuration:
Create a file with the name .env and follow the structure of .env_example. E.g:
```Shell
DATABASE_USER=todouser
DATABASE_NAME=todo
DATABASE_PASSWORD=password
DATABASE_PORT=5432
```