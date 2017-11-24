#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:46:09 2017

@author: eric
"""

from django import forms
from .models import User


class SubmitUserName(forms.Form):
    user_name = forms.CharField(max_length = 20)
    fields = ['user_name']
    labels = {'user_name': ''} #no label b/c button


class SubmitUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['display_name', 'user_id']


