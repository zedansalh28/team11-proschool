from django.contrib import auth
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout, authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django import template
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect, BadHeaderError, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import UpdateView

from App.forms import *
from App.models import *
from App.filters import *


def adminPage(request):
    userList = User.objects.all()[:3]
    messageList = AdminMessage.objects.all()[:3]
    totalusers = User.objects.all().count()
    countTeacher = Teacher.objects.all().count()
    countStudent = Student.objects.all().count()
    context = {'userList': userList, 'messageList': messageList, 'totalusers': totalusers, 'countTeacher': countTeacher,
               'countStudent': countStudent}
    return render(request, 'dashboard.html', context)


def home(requset):
    return render(requset, 'home.html')


def profile(request):
    user = request.user
    form = User_edit_form(instance=user)
    if request.method == 'POST':

        form = User_edit_form(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'profile.html', context)
