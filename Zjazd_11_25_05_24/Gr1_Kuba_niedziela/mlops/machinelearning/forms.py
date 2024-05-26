from django import forms


class ModelForm(forms.Form):
    factor = forms.DecimalField(min_value=0.0, max_value=1.0)
    noise = forms.DecimalField(min_value=0.0, max_value=1.0)


class CategoriseForm(forms.Form):
    x = forms.DecimalField(min_value=-5.0, max_value=5.0)
    y = forms.DecimalField(min_value=-5.0, max_value=5.0)