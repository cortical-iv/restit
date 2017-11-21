# restit
Simple project to illustrate pulling validated data from the RESTful Destiny 2 api into your django project using forms and the django rest framework serializer. Based on the following:    
https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/

The project name is `restit`, and the main app is `d2_api`, which implements the business of showing pages for manually and programmatically pulling in data via forms and serializers (in the `manual` and `automatic` pages, respectively). For this to work you need an api key from Destiny2, which is contained in `/d2_api/utils.py` as `D2_KEY`.

The page `automatic`

Tested on Ubuntu 16.04 using Python 3.6.

### To do
1. Add more feedback about outcome of requests. Right now it is just showing in the terminal, which won't work in production.
2. Set primary keys and don't allow repeats of users.
3. Celery integration to automate checking clan.    
    - https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
    - http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
