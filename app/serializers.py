from rest_framework import serializers
from . import models


class SerializedAuto(serializers.ModelSerializer):
    class Meta:
        model = models.Auto
        fields = ['label', 'year', 'description', 'price']

class SerializedOwner(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = ['first_name', 'last_name']

class SerializedAuto_Passport(serializers.ModelSerializer):
    class Meta:
        model = models.Auto_Passport
        fields = ['related_auto', 'number', 'prefix']