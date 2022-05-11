from django import forms
class SRegister(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
