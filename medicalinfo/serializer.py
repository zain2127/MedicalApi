from rest_framework import serializers
from .models import Doctor
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude=['id','name','education','specialtiy','rating','image']
        feilds = "__all__"