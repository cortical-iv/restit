# restit
Example of how to use forms to help pull data from api requests into a Django database. In this case, we are pulling data from the [Destiny 2 api](https://github.com/Bungie-net/api). For this to work you need an api key from Destiny2, which is contained in `/d2_api/utils.py` as `D2_KEY`.

Tested on Ubuntu 16.04 using Python 3.6.

### To do
1. Build version with something more realistic/complex that changes daily, and automate it with something like cron.
2. Improve messaging. I followed this for the basics:    
https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html
3. Not sure why field label is showing up:
https://www.reddit.com/r/django/comments/7fakjq/using_bootstrap3_i_want_no_label_on_form_element/

#### Note
In a full-fledged project, you will want to update, not just add, new rows. [The docs say](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method):    

    > Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form. A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model

#### Acknowledgments
Initial version of restit was based on https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/.
