from django import forms

class ListCreator(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    