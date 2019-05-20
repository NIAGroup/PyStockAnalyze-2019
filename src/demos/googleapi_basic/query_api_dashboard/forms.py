from django import forms

class MainForm(forms.Form):
	post = forms.CharField()
