pip install Django

### create a new project. firstproject – This is your project
django-admin startproject firstproject

### create app inside project. firstapp – This is your app
python3 manage.py startapp firstapp

### Before starting the app, you will to perform migrations to create necessary database tables:


python3 manage.py makemigrations

python3 manage.py runserver


### Then start a development server hosting apps in the firstproject:

python3 manage.py runserver


### Find INSTALLED_APPS section, and add a new app entry as

'firstapp.apps.FirstappConfig',

### Next, we need to add the urls.py of firstapp to firstproject so that views of firstapp can be properly routed.

- Create an empty urls.py under firstapp folder

cd firstapp
touch urls.py

path('firstapp/', include('firstapp.urls')),

### Now you can create your first view to receive HTTPRequest and return a HTTPResponse wrapping a simple HTML page as its content.

- Open firstapp/views.py, write your first view after the comment # Create your views here.

### Open firstapp/urls.py, add the routes in firstapp

### run django server
python3 manage.py runserver

### containerize the app

- open the setting.py file and change the ALLOWED_HOSTS = [] code to:

ALLOWED_HOSTS = ['*','.us-south.codeengine.appdomain.cloud']


pip install pipreqs
pipreqs .

touch Dockerfile

- create a local docker image and then run
sudo docker build . -t my-django-app:latest
sudo docker run -e PYTHONUNBUFFERED=1 -p  8000:8000 my-django-app 
