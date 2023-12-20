from django import forms


class MovieRequest(forms.Form):
    From = forms.EmailField(initial='mahfazzalin1@gmal.com')
    To = forms.EmailField()
    subject = forms.CharField(max_length=150)
    Moviename = forms.CharField(max_length=500)
