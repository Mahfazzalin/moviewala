from django import forms


class MovieRequest(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    Moviename = forms.CharField(max_length=500)
