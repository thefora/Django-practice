from django.shortcuts import render, get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserProfileView(APIView):
    def put(self, request, *args, **kwargs):
        user_obj = get_object_or_404(User, email=self.request.data['email'])
        request_user_s_email = request.user.email
        try:
            request.data['new_password_1'], request.data['new_password_2']
        except:
            return Response({"new password input error" : ["Input new_password1 & 2."]}, status=400)
        serializer = UserSerializer(user_obj ,data=request.data, 
            context=
            {
                'request_user_s_email' : request_user_s_email,
                'new_password_1' : request.data['new_password_1'],
                'new_password_2' : request.data['new_password_2'],
            }
        ) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)