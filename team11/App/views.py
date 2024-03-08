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






def profile(request):
    user = request.user
    form = User_edit_form(instance=user)
    if request.method == 'POST':

        form = User_edit_form(request.POST, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'profile.html', context)






def logoutUser(request):
    logout(request)
    return redirect('login')










def admin_message_form(request, id=0):
    # creating new form for inserting or editing existed admin messages
    if request.method == "GET":
        if id == 0:
            form = AdminMessageForm()




        else:
            message = AdminMessage.objects.get(pk=id)

            form = AdminMessageForm(instance=message)

        return render(request, "admin_templates/admin_message_form.html", {'form': form})
    else:
        if id == 0:
            form = AdminMessageForm(request.POST)

        else:
            message = AdminMessage.objects.get(pk=id)
            form = AdminMessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
        return redirect('dashboard')


def admin_mesaage_delete(request, id):
    message = AdminMessage.objects.get(pk=id)
    message.delete()
    return redirect('dashboard')


def showAdminMessages(request):
    messages = list(AdminMessage.objects.all())
    return render(request, "admin_templates/all_messages.html", {'messages': messages})





def user_list(request):
    myFilter = userFilter(request.GET, queryset=User.objects.all())

    user_list = myFilter.qs

    context = {'user_list': user_list, 'myFilter': myFilter}

    return render(request, "user_list.html", context)


def user_form_edit(request, id):
    user = User.objects.get(pk=id)
    form = User_edit_form(instance=user)
    if request.method == 'POST':
        a = request.POST['username']
        form = User_edit_form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    context = {'form': form}
    return render(request, 'user_form_info.html', context)


def delete_user(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('user_list')


def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            curr_user = form.save()
            Teacher.objects.create(user=curr_user)
            return redirect('user_list')
    return render(request, "create_user.html", {"form": form})


def showUser(request, id):
    user = User.objects.get(pk=id)
    context = {'user': user}
    return render(request, 'show_details.html', context)


def addTeacher(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            curr_user = form.save() 
            Teacher.objects.create(user=curr_user)
            my_group = Group.objects.get(name='teachers')
            my_group.user_set.add(curr_user)
            return redirect('user_list')
    return render(request, "admin_templates/addTeacher.html", {"form": form})



def addStudent(request):
    form = UserCreationForm()
    teachers = ((teacher.user)
                for teacher in Teacher.objects.all())
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        teacherusername = request.POST.get('teacher')
        teacheruser = User.objects.get(username=teacherusername)
        teacher = Teacher.objects.get(user=teacheruser)
        if form.is_valid():
            user = form.save()
            Student.objects.create(user=user, teacher=teacher)
            my_group = Group.objects.get(name='students')
            my_group.user_set.add(user)
            return redirect('user_list')
    context = {'form': form, 'teachers': teachers}
    return render(request, 'admin_templates/addStudent.html', context)





