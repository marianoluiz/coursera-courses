virtualenv djangoenv
source djangoenv/bin/activate

pip install Django==4.2 psycopg2-binary

# make model

# generate migration scripts
python3 manage.py makemigrations crud

# run migrations
python3 manage.py migrate

# save
python3 write.py
        - This script is creating and adding records (objects) into your Django database using your models (User, Instructor, Course, Lesson, etc.).

# read
python3 read_courses.py
python3 read_instructors.py
python3 read_learners.py

