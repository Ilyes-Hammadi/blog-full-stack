# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # Redirect to a success page.
                return redirect('index')

    else:

        return render(request, 'login.html')

# Return an 'invalid login' error message.


def logout(request):

    if request.COOKIES.has_key('sessionid'):
        session_id = request.COOKIES.get('sessionid')

        session = Session.objects.get(pk=session_id)
        session.delete()

    #auth.logout(request)

    return redirect('index')