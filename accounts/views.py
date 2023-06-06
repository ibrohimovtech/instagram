from django.shortcuts import render

from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=400)
