#  necesary tamplet for the viewrs (controller)
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

# import the models and serializer
from .models import Student
from .serializers import StudentSerializer