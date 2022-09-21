from django.urls import path, include
from rest_framework import urls
from . import views

urlpatterns = [
    path('api-auth/', include(urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('registration', include('dj_rest_auth.registration.urls')),
    path('user-profile', views.UserProfileView.as_view())
]