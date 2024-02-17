from django import forms


class NameForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    def clean_first_name(self):
        first_name: str = self.cleaned_data.get("first_name")
        first_name = first_name.lower().capitalize()
        return first_name
