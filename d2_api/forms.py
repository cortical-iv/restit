#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:46:09 2017

@author: eric
"""

from django import forms
from .models import User


class SubmitUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['display_name']
        labels = {'display_name': ''}  #no label because there's a button
