from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.test import TestCase,tag
from django.urls import reverse
from django.test import Client
from App.models import *
import requests







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

    @tag('unit-test')
    def test_login(self):
        login = self.client.login(username='test', password='test')
        self.assertFalse(login)






class loginTest(TestCase):

    @tag('unit-test')
    def test_login_access_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_login_access_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_login_access_url_negative(self):
        response = self.client.get('/login/')
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_login_access_name_negative(self):
        response = self.client.get(reverse('login'))
        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def testLoginUsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'login.html')

    @tag('unit-test')
    def testLogin_NOT_UsedTemplate(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response,'home.html')

    @tag('unit-test')
    def testUserLogin(self):

        User.objects.create(username='aa', password='aa')

        data = {'username': 'a12', 'password': '1234'}
        response=self.client.post(reverse('login'),data=data,follow=True)
        self.assertEqual(response.status_code,200)
        '''the reason why it redircets to login that's this user doesnt belong to any group'''
        self.assertRedirects(response, reverse('login'))

    @tag('integration-test')
    def testLoginAndLogout(self):
        User.objects.create(username='aa', password='aa')

        data = {'username': 'a12', 'password': '1234'}
        response = self.client.post(reverse('login'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        '''the reason why it redircets to login that's this user doesnt belong to any group'''
        self.assertRedirects(response, reverse('login'))
        self.assertTemplateUsed(response, 'login.html')




        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)





class LogoutTest(TestCase):
   def testLogout(self):
       User.objects.create(username='username', password='username')
       self.client.login(username='username',password='password')

       response = self.client.get(reverse('logout'), follow=True)

       self.assertEqual(response.status_code, 200)
       self.assertFalse(response.context["user"].is_authenticated)


class ManageUsersTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', email='email',
                                        last_name='last_name',
                                        first_name='first_name')
        self.user.set_password('password')
        self.user.save()

    '''@tag('unit-test')'''
    '''def test_editUser_access_url(self):
        # Arrange
        self.client.force_login(self.user)

        response = self.client.get(reverse('update_user_info'),follow=True,data={"id":self.user.id})

        self.assertEqual(response.status_code, 200)'''

    @tag('unit-test')
    def test_editUser_access_name(self):
        # Arrange
        self.client.force_login(self.user)

        response = self.client.get('/profile')

        self.assertEqual(response.status_code, 200)

    @tag('unit-test')
    def test_editUser_access_url_Negateve(self):
        # Arrange
        self.client.force_login(self.user)

        response = self.client.get(reverse('profile'))

        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def test_editUser_access_name_Negateve(self):
        # Arrange
        self.client.force_login(self.user)

        response = self.client.get('/profile')

        self.assertNotEqual(response.status_code, 300)

    @tag('unit-test')
    def testeditUserUsedTemplate(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'profile.html')

    @tag('unit-test')
    def testeditUser_NOT_UsedTemplate(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response,'home.html')



