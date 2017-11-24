from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .forms import SubmitUserName
from .models import User

#import utils  #I have no idea why this doesn't work
from .utils import add_user


def index(request):
    return render(request, 'd2_api/index.html')


def submit(request):
    """User will manually fill out form and submit data."""
    if request.method == 'POST':
        submit_name_form = SubmitUserName(request.POST)
        #do validation here not in add_user!
        if submit_name_form.is_valid():
            user_name = submit_name_form.cleaned_data['user_name']
            save_outcome = add_user(user_name)
            msg = save_outcome['message']
            if save_outcome['flag'] == 1:
                messages.success(request, msg)
                return HttpResponseRedirect(reverse('d2_api:submit'))
            else:
                messages.warning(request, msg)
        else:  #not valid
            msg =  submit_name_form.errors
            messages.warning(request, msg)
            submit_name_form = SubmitUserName()
    else:  #if GET request just show empty form
        submit_name_form = SubmitUserName()

    return render(request, 'd2_api/submit.html', {'submit_name_form': submit_name_form})


def users(request):
    """Display list of users successfully entered."""
    users = User.objects.order_by('display_name')
    context = {'users': users}
    return render(request, 'd2_api/users.html', context)


#def automatic(request):
#    """Add multiple users without user having to enter user name into form field."""
#    if request.method == 'POST':
#        user_names = ['cortical_iv', 'stinky', 'MuricanCheese', 'nujamint', 'bobbyMcGet', 'vex', 'bubble']
#        for user_name in user_names:
#            save_outcome = add_user(user_name)
#            print(save_outcome['message'])
#        return HttpResponseRedirect(reverse('d2_api:index'))
#
#    return render(request, 'd2_api/automatic.html')  #if get request