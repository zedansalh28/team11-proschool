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


def login(request):
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None and user.groups.filter(name='admins').exists():
                auth.login(request, user)
                return redirect('dashboard')
            elif user is not None and user.groups.filter(name='students').exists():
                auth.login(request, user)
                return redirect('student_dashboard')
            elif user is not None and user.groups.filter(name='teachers').exists():
                auth.login(request, user)
                return redirect('teacher')
            else:
                messages.info(request, 'error')
                return redirect('login')
        else:

            return render(request, 'login.html')
    else:
        if request.user.groups.filter(name='admins'):
            return redirect('dashboard')
        if request.user.groups.filter(name='students'):
            return redirect('student_dashboard')
        if request.user.groups.filter(name='teachers'):
            return redirect('teacher')


def Teacher_Signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        id = request.POST['id']
        email = request.POST['email']
        if password1 == password2:
            if not TeacherId.objects.filter(teacherId=id).count() == 1:
                messages.error(request, 'your id is wrong')
            elif User.objects.filter(username=username):
                messages.error(request, 'username is taken')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                last_name=last_name,
                                                first_name=first_name)
                user.save()
                Teacher.objects.create(user=user)
                my_group = Group.objects.get(name='teachers')
                my_group.user_set.add(user)
                print("user is created")
                return redirect('login')
        else:
            messages.error(request, 'passwords doesnt mach')




    return render(request, 'teacher_templates/teacher_register.html')


def Student_Signup(request):
    teachers = ((teacher.user)
                for teacher in Teacher.objects.all())
    context = {'teachers': teachers}

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        teacherusername = request.POST.get('teachers')
        teacheruser = User.objects.get(username=teacherusername)
        teacher = Teacher.objects.get(user=teacheruser)
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.error(request, 'username is taken')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1,
                                                last_name=last_name,
                                                first_name=first_name)
                user.save()
                Student.objects.create(user=user, teacher=teacher)
                my_group = Group.objects.get(name='students')
                my_group.user_set.add(user)
                print("user is created")
                return redirect('login')
        else:
            messages.error(request, 'passwords doesnt mach')

    return render(request, 'student_templates/student_register.html', context)


def createSolution(request, id):
    SolutionFormSet = inlineformset_factory(Student, StudentSolution, fields=('solutionContent',), extra=1,
                                            can_delete=False)
    student = Student.objects.get(user=request.user)
    homeWork = HomeWork.objects.get(pk=id)
    teacher = student.teacher
    initial = {'homeWork': homeWork, 'teacher': teacher, 'student': student}
