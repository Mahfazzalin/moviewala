from django import forms


class MovieRequest(forms.Form):
    From = forms.EmailField(initial='mahfazzalin1@gmal.com', disabled=True)
    To = forms.EmailField(label='Enter your Email', label_suffix=' ➡️')
    subject = forms.CharField(max_length=150, widget=forms.PasswordInput)
    Moviename = forms.CharField(max_length=500, help_text='Enter your movie name', widget=forms.Textarea)
    checkbox = forms.CharField(widget=forms.CheckboxInput)
