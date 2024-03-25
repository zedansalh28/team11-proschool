from django import forms
from .models import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User









class addUserForm(UserCreationForm):
   def clean_username(self,*args,**kwargs):
       user_name=self.cleaned_data.get('username')
       if User.objects.filter(username=user_name).exists():
           raise forms.ValidationError("this name is already exist")

class User_edit_form(UserChangeForm):
    password = ReadOnlyPasswordHashField(

    )
    class Meta:
        model=User
        fields=('username','email',)
class TeacherMessageForm(forms.ModelForm):
    class Meta:
        model = TeacherMessage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeacherMessageForm, self).__init__(*args, **kwargs)


class SolutionForm(forms.ModelForm):
    class Meta:
        model = StudentSolution
        fields = ('student','homeWork','solutionContent')

    def __init__(self, *args, **kwargs):
        super(SolutionForm, self).__init__(*args, **kwargs)

class studyForm(forms.ModelForm):
    class Meta:
        model = Studies
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(studyForm, self).__init__(*args, **kwargs)
class BugReportForm(forms.ModelForm):
    class Meta:
        model = Bugreport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BugReportForm, self).__init__(*args, **kwargs)



