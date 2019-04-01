from .models import  Profile, Project, Grade
from django import forms
from .choices import *



class NewCommentForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=600)

class Profileform(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']

class Projectform(forms.ModelForm):
     class Meta:
         model= Project
         exclude = ['user','overall_grade']

class Gradeform(forms.ModelForm):
     design= forms.ChoiceField(choices=VOTE_CHOICES)
     usability= forms.ChoiceField(choices=VOTE_CHOICES)
     content= forms.ChoiceField(choices=VOTE_CHOICES)
     class Meta:
         model= Grade
         exclude = ['user','project','total','avg']
    