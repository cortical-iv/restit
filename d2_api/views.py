from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import SubmitUser
from .models import User

#import utils  #I have no idea why this doesn't work
from .utils import add_user


def index(request):
    return render(request, 'd2_api/index.html')


def manual(request):
    """User will manually fill out form and submit data."""
    if request.method == 'POST':
        save_user_form = SubmitUser(request.POST)
        save_outcome = add_user(save_user_form)
        print(save_outcome['message'])
        if save_outcome['flag'] == 1:
            return HttpResponseRedirect(reverse('d2_api:manual'))
        #if you want to go back to blank form, uncomment the following:
        #else:
            #save_user_form = SubmitUser()
    else:  #if GET request just show empty form
        save_user_form = SubmitUser()

    return render(request, 'd2_api/manual.html', {'save_user_form': save_user_form})


def automatic(request):
    """Add multiple users without user having to enter user name into form field."""
    if request.method == 'POST':
        display_names = ['cortical_iv', 'stinky', 'MuricanCheese', 'nujamint', 'bobbyMcGet', 'vex', 'bubble']
        for name in display_names:
            automatic_data ={'display_name': name}
            save_user_form = SubmitUser(automatic_data)
            save_outcome = add_user(save_user_form)
            print(save_outcome['message'])
        return HttpResponseRedirect(reverse('d2_api:index'))

    return render(request, 'd2_api/automatic.html')  #if get request


def users(request):
    """Display list of users successfully entered."""
    users = User.objects.order_by('display_name')
    context = {'users': users}
    return render(request, 'd2_api/users.html', context)