from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse
from django.test import Client
from App.models import *
import requests


# Create your tests here.


# ------------tests for some admin functionality  ------     -- ------------------
@tag("unit_test")
class AdminMessageFormTests(TestCase):
    @tag('unit-test')
    def test_Add_Message_GET(self):
        c = Client()
        response = c.get(reverse('createmessage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_templates/admin_message_form.html')

    @tag('unit-test')
    def test_Add_Message_GET2(self):
        c = Client()
        response = c.get(reverse('createmessage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'teacher_templates/message_form.html')

    @tag('unit-test')
    def test_Add_Teacher_Message_GET(self):
        c = Client()
        response = c.get(reverse('create_teacher_message'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'teacher_templates/message_form.html')





    '''
    def test_deleteTeacher_message_POST(self):
        url = "http://127.0.0.1:8000/deleteTeacherMessage/4"
        response = requests.delete(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 403)
    def test_delete_homework(self):
        url = "http://127.0.0.1:8000/delete_homework/4"
        response = requests.delete(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 403)

    def test_delete_study(self):
        url = "http://127.0.0.1:8000/studyform_delete/4"
        response = requests.delete(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 403)

    def test_update_homework(self):
        url = "http://127.0.0.1:8000/homework_update1"
        response = requests.get(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 404)

    def test_delete_user(self):
        url = "http://127.0.0.1:8000/delete/4"
        response = requests.delete(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 403)
    def test_update_user(self):
        url = "http://127.0.0.1:8000/update/4"
        response = requests.get(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 200)

    def test_update_study(self):
        url = "http://127.0.0.1:8000/studyform/4"
        response = requests.get(url)
        print(response.status_code)
        self.assertEquals(response.status_code, 200)
        '''
# -----------------------------tests for  Teacher user functionality --------------------

class TeacherMessageFormTests(TestCase):

    @tag('unit-test')
    def test_Add_Message_Template(self):
        c = Client()
        response = c.get(reverse('create_teacher_message'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'login.html')





# -----------------------------tests for  homeworks  functionality --------------------

class homeworkTest(TestCase):



















