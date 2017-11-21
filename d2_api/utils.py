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
from .serializer import SearchPlayerSerializer
#from .models import User


#Set some parameters
baseurl = 'https://bungie.net/Platform/Destiny2/'
baseurl_groupv2 = 'https://bungie.net/Platform/GroupV2/'
D2_KEY =  #  <YOUR API KEY HERE>  #

def search_destiny_player_url(user_name):
    """Main point is typically to get the user's id from their username.
        https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyPlayer.html
      Note for this example it's constrained to ps4 (platform = 2)
    """
    return baseurl + 'SearchDestinyPlayer/2/' + user_name + '/'


def add_user(save_user_form):
    """Tries to add user from completed form
    Returns 1 if successful, 0 if not, and None if that user is not a D2 player in PS4"""
    add_result = {'flag': 0, 'message': ''}
    if save_user_form.is_valid():
        user_name = save_user_form.cleaned_data['display_name']
        search_url = search_destiny_player_url(user_name)
        search_response = requests.get(search_url, headers = {"X-API-Key": D2_KEY})
        user_data = search_response.json()['Response'] #NB: this is a list
        if user_data:
            submission_data = {'display_name': user_data[0]['displayName'], 'user_id': user_data[0]['membershipId']}
            #print(repr(serializer))  #for debugging
            try:
                serializer = SearchPlayerSerializer(data =  submission_data)
                if serializer.is_valid():
                    serializer.save() #save data to database
                    add_result['flag'] = 1
                    add_result['message'] = 'Successfully added {0}'.format(user_name)
                else:
                    msg = "Invalid serializer. serializer.errors: {0}".format(serializer.errors)
                    add_result['message'] = msg

            except Exception as e:
                msg = "Exception using serializer: {0}. Exception type: {1}.".format(e, e.__class__.__name__)
                add_result['message'] = msg

        else:
            msg = "'{0}' is not a Destiny2 player on PS4".format(user_name)
            add_result['message'] = msg
    else:  #not valid
        msg = "save_user_form not valid. error: {0}".format(save_user_form.errors)
        add_result['message'] = msg

    return add_result






