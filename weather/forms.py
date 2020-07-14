from django import forms

class SearchBox(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    country = forms.CharField(max_length=3, required=False)

    