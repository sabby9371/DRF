from rest_framework import serializers
# from . models import Cast
from . import models

class CastSerializer(serializers.ModelSerializer):
    def validate_age(self,age):     #validate_
        if age < 0:
            raise serializers.ValidationError("Age should be positive")
        else:
            return age
# Hw name validation (no special charecters)
    class Meta:
        # model = Cast
        model = models.Cast
        fields= ['id','name','city','branch','age']




