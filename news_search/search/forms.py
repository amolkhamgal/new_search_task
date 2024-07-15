from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter keyword'}))
