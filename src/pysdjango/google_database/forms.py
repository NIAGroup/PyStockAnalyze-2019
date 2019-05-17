from django import forms

class Search(forms.Form):
    search = forms.CharField(label='Search', max_length=20, required=False)