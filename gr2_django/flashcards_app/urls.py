from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_view),
    path('flashcards', views.flashcards_list, name="flashcards-collection"),
    path('flashcards/learn/<slug:slug>', views.learn_flashcard, name="learn-flashcard"),
    path('flashcards/add', views.add_flashcard, name="add-flashcard"),
]