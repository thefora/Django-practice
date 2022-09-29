from random import choices
from .models import User
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

gender =(
    ('male', "남성"),
    ('female', '여성')
)

class CustomRegisterSerializer(RegisterSerializer):
    username = None
    nickname = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=gender)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname', '')
        data['name'] = self.validated_data.get('name', '')
        data['gender'] = self.validated_data.get('gender', "")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if self.instance is not None:
            # request's email & token's email check if match
            
            if attrs['email'] == self.context['request_user_s_email']:

                # password check if correct
                if not (check_password(attrs['password'], self.instance.password)):
                    raise ValidationError({"password incorrect error" : "Incorrect password."})
                
                # new password check if match
                if self.context['new_password_1'] == self.context['new_password_2']:
                    return attrs
                else:
                    raise ValidationError({"password dismatch error" : "New password is not match."})
            else:
                raise ValidationError({"Permission denied." : "user dismatch error."})
            
        else:
            return super().validate(attrs)
    
    def update(self, instance, validated_data):
        new_password = self.context['new_password_1']
        if new_password is None:
            new_password = validated_data['password']
        instance.set_password(new_password)
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance
