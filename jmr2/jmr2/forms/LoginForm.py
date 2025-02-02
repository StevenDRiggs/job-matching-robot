from django import forms


class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email', max_length=200)
    password = forms.CharField( max_length=100)
