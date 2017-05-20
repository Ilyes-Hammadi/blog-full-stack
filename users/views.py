# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
from rest_framework import viewsets

from users.serializer import UserSerializer


def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # Show success message
                messages.success(request, 'Welcome back {}'.format(user.username))
                return redirect('index')
            else:
                # Show error message
                messages.error(request, 'This user does not exists')
                return render(request, 'login.html')

    else:

        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'See you soon')
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # If user does not exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username exists')
            return render(request, 'signup.html')

        # Password correct
        if password != confirm_password:
            messages.error(request, 'Password dont match')
            return render(request, 'signup.html')
        
        # Create the user profile
        user = User.objects.create_user(username, email=None, password=password)
        
        # Login the created user
        user = auth.authenticate(request, username=username, password=password)
        auth.login(request, user)

        messages.success(request, 'Welcome to Djangostagram homie')
        
        return redirect('index')
    else:
        return render(request, 'signup.html')


##### API ######
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


