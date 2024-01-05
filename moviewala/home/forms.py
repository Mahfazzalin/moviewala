from django import forms
from django.core import validators


class MovieRequest(forms.Form):
    From = forms.EmailField(initial='mahfazzalin1@gmal.com', disabled=True)
    To = forms.EmailField(label='Enter your Email', label_suffix=' ➡️', validators=[validators.MaxLengthValidator(30)])
    subject = forms.CharField(max_length=20, min_length=6, error_messages={'required':'Enter a Subject Name'})
    re_subject = forms.CharField(max_length=20, min_length=6, error_messages={'required':'Enter a Subject Name'})
    Moviename = forms.CharField(max_length=500, help_text='Enter your movie details', widget=forms.Textarea(attrs={'rows':4 ,'cols':40}))
    #checkbox = forms.CharField(widget=forms.CheckboxInput)
