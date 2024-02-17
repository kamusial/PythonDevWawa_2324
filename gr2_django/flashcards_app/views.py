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
    return render(request, "flashcards-list.html", context={"flashcards": flashcards})


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    all_flashcards = Flashcard.objects.all()
    all_flashcards_ids = [flashcard.pk for flashcard in all_flashcards]
    current_index = all_flashcards_ids.index(flashcard.pk)
    if current_index + 1 == len(all_flashcards):
        next_flashcard = all_flashcards[0]
    else:
        next_flashcard = all_flashcards[current_index + 1]

    context = {"flashcard": flashcard, "next_flashcard_url": next_flashcard.learn_url}
    return render(request, "learn-flashcard.html", context=context)
