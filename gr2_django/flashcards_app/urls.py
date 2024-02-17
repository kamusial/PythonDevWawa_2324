from django.urls import path

from .views import hello_view, flashcards_list, learn_flashcard

urlpatterns = [
    path('', hello_view),
    path('flashcards', flashcards_list, name="flashcards-collection"),
    path('flashcards/learn/<slug:slug>', learn_flashcard, name="learn-flashcard")
]
