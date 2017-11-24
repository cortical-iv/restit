#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hook for interacting with d2 api
"""

"""
URL GENERATORS
The following functions create urls in the format that the bungie servers want them.
In the docs for each function I give the url to bungie docs, partly to help but also so
you can see what I may have left out --- I'm not always including all possible query strings.
I named each url generator according to the bungie end point (e.g., if the end point is X
then the function is X_url)
"""
##Imports
import requests
from .forms import SubmitUser
#from .models import User


#Set some parameters
baseurl = 'https://bungie.net/Platform/Destiny2/'
baseurl_groupv2 = 'https://bungie.net/Platform/GroupV2/'
D2_KEY = '2c967fcb4299479aac4b5414dff5ee5e'    #  <YOUR API KEY HERE>   #

def search_destiny_player_url(user_name):
    """Main point is typically to get the user's id from their username.
        https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyPlayer.html
      Note for this example it's constrained to ps4 (platform = 2)
    """
    return baseurl + 'SearchDestinyPlayer/2/' + user_name + '/'


def add_user(user_name):
    """
    Validate form data containing 'display_name', request their info from server,
    and pull in via a serializer. Returns dictionary, add_user_results, with two keys:
        'flag': 1 if successful, 0 if not, and None if that user is not a D2 player in PS4.
        'message': message about the outcome (success, validation error, etc).
    """
    add_user_results = {'flag': 0, 'message': ''}
    search_url = search_destiny_player_url(user_name)
    player_search_request = requests.get(search_url, headers = {"X-API-Key": D2_KEY})
    player_search_response = player_search_request.json()['Response']
    print(player_search_response)
    if player_search_response:
        #Create dictionary of data and bind it to the SubmitUser form.
        user_data = {'display_name': player_search_response[0]['displayName'], \
                     'user_id': player_search_response[0]['membershipId']}
        submit_user_form = SubmitUser(user_data)
        #Validate and save data
        if submit_user_form.is_valid():
            submit_user_form.save() #save data to database
            add_user_results['flag'] = 1
            add_user_results['message'] = 'Successfully added {0}'.format(user_name)
        else:
            msg = "Invalid submit_user_form. form.errors: {0}".format(submit_user_form.errors)
            add_user_results['message'] = msg
    else:
        msg = "'{0}' is not a Destiny2 player on PS4".format(user_name)
        add_user_results['message'] = msg


    return add_user_results






