# Django-CKEditor-tutorial
Example of using CKEditor rich text editor, code snippet and image uploader

[https://frombitstobytes.com/2017/07/02/what-you-see-what-you-get/](https://frombitstobytes.com/2017/07/02/what-you-see-what-you-get/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installation

Try it locally:

Download or "git clone" the package:
```
$ git clone https://github.com/casol/Django-CKEditor-tutorial.git
$ cd Django-CKEditor-tutorial
```
First install the module, preferably in a virtual environment:
```
$ pip install -r ../requirements.txt
```
Initiate the migration and then migrate the database:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Create an admin user:
```
$ python manage.py createsuperuser
```
Setup a local server:
```
$ python manage.py runserver
```

## Build with
* Django==1.11.5
* django-ckeditor==5.3.0
* django-js-asset==0.1.1
* olefile==0.44
* Pillow==4.2.1
* pkg-resources==0.0.0
* pytz==2017.2
