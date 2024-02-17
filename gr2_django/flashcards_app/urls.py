from django.urls import path

from .views import hello_view, flashcards_list

urlpatterns = [
    path('', hello_view),
    path('flashcards', flashcards_list, name="flashcards-collection")
]
