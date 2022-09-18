from random import choices
from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

gender =(
    ('male', "남성"),
    ('female', '여성')
)

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    nickname = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=gender)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['gender'] = self.validated_data.get('gender', "")

        return data