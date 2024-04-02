from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.adminPage, name='dashboard'),
    path('login/', views.login, name='login'),
    path('Teacher_Register/', views.Teacher_Signup, name='Teacher_Signup'),
    path('Student_Register/', views.Student_Signup, name='Student_Signup'),
    path('teacher', views.teacher_dashboard, name='teacher'),
    path('delete_homework/<int:id>/', views.homework_delete, name='homework_delete'),
    path('homeworkform/', views.homework_form, name='homework_form'),
    path('SolutionForm/', views.Solution_form, name='Solution_form'),
    path('homeowrk<int:id>/', views.homework_form, name='homework_update'),
    path('profile', views.profile, name='profile'),
    path('createmessage/', views.admin_message_form, name='createmessage'),
    path('editAdminMessage/<int:id>', views.admin_message_form, name='editAdminMessage'),
    path('deleteAdminMessage/<int:id>', views.admin_mesaage_delete, name='deleteAdminMessage'),
    path('createTeacherMessage', views.teacher_message_form, name='create_teacher_message'),
