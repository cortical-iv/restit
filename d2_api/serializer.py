#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Serializer for data from api
"""

from rest_framework import serializers
from .models import User

class SearchPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['display_name', 'user_id']