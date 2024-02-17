from django.shortcuts import render
from .models import Flashcard


def hello_view(request):
    return render(request, "hello.html")


def flashcards_list(request):
    """objects.all() zwraca wszystkie obiekty fiszek z db.sqlite3
    : list[Flashcard] określa typ flashcards (to tylko podpowiedź dla devów / Pycharma, nie zmienia to logiki w kodzie
    """
    flashcards: list[Flashcard] = Flashcard.objects.all()
    return render(request,
                  "flashcards-list.html",
                  context={
                      "flashcards": flashcards})
