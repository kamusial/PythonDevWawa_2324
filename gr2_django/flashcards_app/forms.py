from django import forms


class NewFlashcardForm(forms.Form):
    name = forms.CharField(max_length=200)
    question = forms.CharField(max_length=500)
    answer = forms.CharField(max_length=1000)
