# Foodle
> A responsive web application for finding deals within walking distance built using Django and Angular. 

[![NPM Version][npm-image]][npm-url]

[![Build Status][travis-image]][travis-url]

[![Downloads Stats][npm-downloads]][npm-url]


[![PythonAnywhere][https://img.shields.io/badge/demo-blue.svg]](markglasgow148@pythonanywhere.com)


"Where Deals Become Meals"™️
![](NOTES/header.png)

# Running Locally

More info in readme/README.md

# Directory Structure

Foodle_dev/ :: main directory

* /angular_django/  :: local to your install. Django project and main settings.py  
    * __ init __.py
    * settings.py
    * urls.py
    * wsgi.py :: not needed on pythonanywhere 


* /foodle/ :: Our app within the project, containing the Django Rest Framework views and URL routing (urls.py)
    * migrations ::
    * static :: Main site build
        * front-end :: local package.json requirements (npm install)
    * templates :: base.html // index.html // etc
    * dist :: Compiled Angular App
    * Main Django app files apps.py, models,py, etc...

* NOTES/ :: misc. files

* readme/ :: shell configuration scripts (unix) 

* venv/ :: local environment (your install)

* Misc files

    * .gitignore :: Files to be ignored from git push

    * manage.py :: main python executable 

    * Pipfile :: pipenv dependencies? remove ? 

    * requirements.txt :: requirements set by django









References:

Nathan:
For a number of the bootstrap elements, this tutorial was used to understand and start implementing the basics of them
https://www.youtube.com/watch?v=9cKsq14Kfsw


Hassan:
Used to assist in implementing the dropdown on the submit form
https://stackovverflow.com/questions/31130706/dropdown-in-django-model

Used in implementing the sign in with google elements
https://developers.google.com/identity/sign-in/web/sign-in

Used as a base for styling the submit/login/register pages
https://bootsnipp.com/snippets/dldxB


Greg:
When researching how to use Google Maps API the following tutorials were very informative
https://developers.google.com/maps/documentation/javascript/tutorial
https://developers.google.com/maps/documentation/geocoding/intro
https://developers.google.com/maps/documentation/geolocation/intro
https://developers.google.com/maps/documentation/javascript/directions


Mark:



Finn:
Adapted for use:
https://wsvincent.com/django-contact-form/

Also this:
https://docs.djangoproject.com/en/2.1/topics/email/

Adapted to create FAQ page:
https://github.com/CodyHouse/faq-template
