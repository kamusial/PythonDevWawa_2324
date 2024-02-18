from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from flashcards_app.models import Flashcard


class NewFlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ["name", "question", "answer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit("new-flashcard-submit",
                   "Add",
                   css_class="rounded-pill mt-4")
        )
