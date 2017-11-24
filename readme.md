# restit
Simple project to illustrate pulling data from the RESTful Destiny 2 api into django using forms.

Structure: the project name is `restit`, and the main app is `d2_api`, which implements the business of triggering the process of adding a user to the database. For this to work you need an api key from Destiny2, which is contained in `/d2_api/utils.py` as `D2_KEY`.

Tested on Ubuntu 16.04 using Python 3.6.

### Notes
1. In a full-fledged project, you will want to update, not just add, new rows. Docs on this:
https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method   
    >Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form. A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model

### To do
1. Build version with something more interesting, that changes daily, and automate it with something like cron.
2. Improve messaging. For messaging here I largely followed:    
https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html

#### Acknowledgments
Initial version of restit was based on https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/.
