from rest_framework import serializers
from .models import Student
############33
class StudentSerializer(serializers.ModelSerializer):
    class Meta:  
        model=Student
        fields=['id','name','address','roll_number']
