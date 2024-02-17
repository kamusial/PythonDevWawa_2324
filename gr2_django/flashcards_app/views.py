from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

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


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    context = {"flashcard": flashcard}
    return render(request,
                  "learn-flashcard.html",
                  context=context)
