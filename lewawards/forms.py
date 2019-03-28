from .models import  Profile
from django import forms



class NewCommentForm(forms.Form):
    comment = forms.CharField(label='Comment',max_length=600)

class Profileform(forms.ModelForm):
     class Meta:
         model= Profile
         exclude = ['user']