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
]
