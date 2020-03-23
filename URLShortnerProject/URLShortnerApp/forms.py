from django import forms

class URLDataForm(forms.Form):
	EnterURL=forms.CharField(max_length=1000)