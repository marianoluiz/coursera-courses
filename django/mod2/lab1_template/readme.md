### create virtual env:
```bash
$ pip install virtualenv
$ virtualenv djangoenv
$ source djangoenv/Scripts/activate
```

### due to error in install psycopg2 in requirements, i did:

```bash
$ pip install --only-binary :all: psycopg2-binary
$ pip install -r requirements.txt
```

### guide

- makemigrations: Generates migration files based on changes in your models.
- migrate: Applies the migration files to the database, updating the schema.


First, you will need to generate migration scripts for orm app

```bash
$ python3 manage.py makemigrations orm
```

You can check the SQL statements by running:
```bash
$ python3 manage.py sqlmigrate orm 0001
```

Next, you can perform the migration to create orm_user table by running:
```bash
$ python3 manage.py migrate
```

You could run the test.py to test your model:
```bash
$ python3 test.py
```
