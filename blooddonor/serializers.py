from dataclasses import field
from pyexpat import model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import BloodDonorProfile


class DonorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonorProfile
        fields = ['firstName', 'lastName', 'email', 'age', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password='password')


class DonorViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonorProfile
        fields = ['firstName', 'lastName', 'email',
                  'age', 'BDDistrict', 'donorStatus', 'mobileNumber']
