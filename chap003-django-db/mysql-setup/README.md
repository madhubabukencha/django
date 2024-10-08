# MySQL setup for Django
In this document, I will try to provide adequate information to setup
connection between MySQL and Django. I will also cover, how to migrate
existing data from SQLite to MySQL.

## Dependencies (for Windows)
- I am assuming that, you have already installed [Python](https://www.python.org/) and [Django](https://pypi.org/project/Django/) in your local system and you also able to run django server.

- Make sure you have installed [MySQL](https://dev.mysql.com/downloads/mysql/) and [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) on your machine. I found a good Youtube video which explain all the installation steps for MySQL<br>
"[How To Install MySQL on Windows 11 (2024)](https://www.youtube.com/watch?v=a3HJnbYhXUc)"

- Don't use the root user, create a seperate user and allowcate all the necessary permissions to it. If you are not sure about them, give all the permissions just like root user has. Lack of permission might create issue while applying migrations. This [Page](https://github.com/madhubabukencha/Databases/blob/main/MySQL/MySQL_Configurations.md) gives you basic idea about new user creation.

## SQLite to MySQL Migration
Follow below steps if you are using SQLite already and wanted to migrate to MySQL. Ignore these steps if you are building your project from scratch.
- To avoid data loss, first you need to dump your SQLite data. Use below command to do that.
  ```
  python manage.py dumpdata > backup.json
  ```
  If you are facing any encoding related errors try any one of the below commands,
  ```
  python -Xutf8 ./manage.py dumpdata > data.json
  ```
  or
  ```
  ./manage.py dumpdata -o data.json
  ```

## Configure Django to Use MySQL
- Modify your `settings.py` file to use MySQL as the database backend instead of SQLite.
  ```
  # New MySQL configuration:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306'
    }
  }
  ```
- Login with your mysql username and password in MySQL Workbench and create a new database that Django will connect to.
  ```
  CREATE DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```
  Make sure this database is empty(no tables) to avoid issues at the time of migration.
- Run Django’s migration system to create the schema in MySQL
  ```
  python manage.py migrate
  ```
- Now that the schema is set, load the data from the SQLite backup (backup.json) into the MySQL database:
  ```
  python manage.py loaddata backup.json
  ```
  This will insert all the previously backed-up data into your MySQL database.
- Finally verify for any data loss by looking at the migrated tables.





