# restit
Simple project to illustrate pulling validated data from the RESTful Destiny 2 api into your django project using forms and the django rest framework serializer. Based on the following:    
https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/

The project name is `restit`, and the main app is `d2_api`, which implements the business of showing pages for manually and programmatically pulling in data  (in `views.manual` and `views.automatic`, respectively). For this to work you need an api key from Destiny2, which is contained in `/d2_api/utils.py` as `D2_KEY`.

The home page is an introduction and discussion of the advantages of this approach. The Users page lists the users entered thus far.

Tested on Ubuntu 16.04 using Python 3.6.

### To do
0. Display code:
https://stackoverflow.com/questions/1514874/display-pretty-code-in-django

1. Just do all this in forms.
-Create two forms: one home-grown, just a formForm, for submission of username (SubmitUsername), and the other for saving user, that is a ModelForm (SubmitUser, with all the fields). Get rid of any bullshit in this application and just focus on the nub.

To bind data to a form just pass dictionary with
{'field_name1': data1, 'field_name2': data2}


2. Work out the problem with unique id...Either form-based on serializer-based:
- https://stackoverflow.com/questions/1780499/how-do-i-update-an-already-existing-row-when-using-modelforms
- https://stackoverflow.com/questions/29247811/supress-field-should-be-unique-error-in-django-rest-framework

Will I need an 'update_user' view for when we hit the 'user id already exists' error from the serializer?

From django docs for forms.save:
https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method
Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form. A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model

Probably just switch away from the serializer and just use forms.



2. Add more feedback about outcome of requests. Right now it is just showing in the terminal, which won't work in production.
3. Celery integration to automate checking clan.    
    - https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
    - http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
