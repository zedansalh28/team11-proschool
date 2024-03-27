from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('createmessage/', views.admin_message_form, name='createmessage'),
    path('editAdminMessage/<int:id>', views.admin_message_form, name='editAdminMessage'),
    path('deleteAdminMessage/<int:id>', views.admin_mesaage_delete, name='deleteAdminMessage'),
    path('addStudent',views.addStudent,name="addStudent"),
    path('addTeacher',views.addTeacher,name="addTeacher"),
    path('showAdminMessages', views.showAdminMessages, name="showAdminMessages"),
    path('user_list/',views.user_list,name="user_list"),
    path('update/<int:id>',views.user_form_edit,name="update_user_info"),
    path('delete/<int:id>',views.delete_user,name="delete_user"),
    path('addStudent', views.addStudent, name="addStudent"),
    path('addTeacher', views.addTeacher, name="addTeacher"),
    path('user_list/', views.user_list, name="user_list"),
     path('studentdashboard', views.student_dashboard, name="student_dashboard"),
    path('bugreport', views.bugreport, name="bugreport"),
    path('showSolutions', views.showSolutions, name="showSolutions"),
    path('allstudies', views.showStudies, name='showAllStudies'),
    path('approveStudy/<int:id>', views.approveStudy, name="approve_study"),
    path('studiesTeacher', views.showStudiesTeacher, name="showStudentTeacher"),
    path('studyForm', views.study_form, name="addstudy"),
    path('studyform/<int:id>', views.study_form, name="study_update"),
    path('studyform_delete/<int:id>', views.study_delete, name="study_delete"),
    
]
