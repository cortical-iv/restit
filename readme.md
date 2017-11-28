# restit
A simple example of how to use forms to pull data from a RESTful api into a django project. In this case, we are pulling data from the [Destiny 2 api](https://github.com/Bungie-net/api). For this to work you need an api key from Destiny2, which is assumed to be in your environment variables (see  'Secret Stuff' discussion below).

Tested locally on Ubuntu 16.04/Python 3.6, and remotely at Heroku. For a working deployment, see:    
http://restit.herokuapp.com

### To do
1. Build version with something more realistic/complex that changes daily (SVM).
2. Improve status message formatting. I followed this for the basics:    
https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html
3. Not sure why field label is showing up for user submit form:
https://www.reddit.com/r/django/comments/7fakjq/using_bootstrap3_i_want_no_label_on_form_element/


#### Notes
##### 1. Secret stuff
The Django SECRET_KEY and the Destiny 2 api-key (D2_KEY) need to be kept secret. As is common practice, and recommended in Two Scoops of Django (Section 5.3), for `restit` we are storing the secrets as environment variables. To set them locally (in Linux) just use:  

    export SECRET_KEY=*secret key value*    
    export D2_KEY=*your d2 api key value*

If you are using conda distribution of Python (which I am), things are a bit different:   
https://conda.io/docs/user-guide/tasks/manage-environments.html#saving-environment-variables    
For conda, in the virtual environment named `r_est`, I did the following:    

    cd ~/anaconda3/envs/r_env    
    mkdir -p ./etc/conda/activate.d    
    mkdir -p ./etc/conda/deactivate.d    
    touch ./etc/conda/activate.d/env_vars.sh    
    touch ./etc/conda/deactivate.d/env_vars.sh     
Then in `./etc/conda/activate.d/env_vars.sh`:    

    #!/bin/sh
    export SECRET_KEY=*secret key value*    
    export D2_KEY=*your d2 api key value*
Obviously, replace the placeholders with strings containing your actual keys. Next, in `./etc/conda/activate.d/env_vars.sh`:    

    #!/bin/sh
    unset SECRET_KEY
    unset D2_KEY    
Then when you activate the virtual environment, the relevant variables will be seen in conda, and when you deactivate it, they will be erased.

The D2_KEY is pulled in `restit/settings.py` with the helper function `get_env_variable`, and can be imported elsewhere in the project with `from django.conf import settings` and then accessed with `settings.D2_KEY`. You can see this in `/d2_api/utils.py`

On Heroku things are much simpler:    

    heroku config:set SECRET_KEY=*secret key value*
    heroku config:set D2_KEY=*your d2 api key value*    
And things should just work.

##### 2. **Saving versus updating the db**    
In a full-fledged project, you will want to update, not just add, new rows. [The docs say](https://docs.djangoproject.com/en/1.11/topics/forms/modelforms/#the-save-method):    
> Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form. A subclass of ModelForm can accept an existing model instance as the keyword argument instance; if this is supplied, save() will update that instance. If it’s not supplied, save() will create a new instance of the specified model    

#### Acknowledgments
Initial version of restit was based on https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/.
