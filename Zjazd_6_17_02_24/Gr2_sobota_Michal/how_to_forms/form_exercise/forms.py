import re
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NameForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def clean_first_name(self):
        first_name: str = self.cleaned_data.get("first_name")
        first_name = first_name.lower().capitalize()
        if re.search(r"\d", first_name) is not None:
            raise forms.ValidationError("Name should not contain numbers!")
        return first_name


class CrispyNameForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("not important?", "SEND")
        )

    def clean_first_name(self):
        first_name: str = self.cleaned_data.get("first_name")
        first_name = first_name.lower().capitalize()
        if re.search(r"\d", first_name) is not None:
            raise forms.ValidationError("Name should not contain numbers!")
        return first_name
