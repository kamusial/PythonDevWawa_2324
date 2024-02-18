from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewFlashcardForm
from .models import Flashcard


def hello_view(request):
    return render(request, "flashcards_app/register.html")


def flashcards_list(request):
    """objects.all() zwraca wszystkie obiekty fiszek z db.sqlite3
    : list[Flashcard] określa typ flashcards (to tylko podpowiedź dla devów / Pycharma, nie zmienia to logiki w kodzie
    """
    if request.method == "POST":
        slug = request.POST.get("slug")
        flashcard_to_delete: Flashcard = Flashcard.objects.filter(slug=slug)
        flashcard_to_delete.delete()
    flashcards: list[Flashcard] = Flashcard.objects.all()
    return render(request, "flashcards_app/flashcards-list.html", context={"flashcards": flashcards})


def learn_flashcard(request, slug):
    flashcard = get_object_or_404(Flashcard, slug=slug)
    next_flashcards = Flashcard.objects.filter(pk__gt=flashcard.pk)
    if next_flashcards.exists():
        next_flashcard = next_flashcards.first()
    else:
        next_flashcard = Flashcard.objects.all().first()
    context = {"flashcard": flashcard, "next_flashcard_url": next_flashcard.learn_url}
    return render(request, "flashcards_app/learn-flashcard.html", context=context)


def add_flashcard(request):
    if request.method == "POST":
        filled_form = NewFlashcardForm(request.POST)
        if filled_form.is_valid():
            new_flashcard = Flashcard(**filled_form.cleaned_data)
            new_flashcard.save()
            return redirect("flashcards-collection")
    return render(request, "flashcards_app/add-flashcard.html", context={"formularz_do_dodania_fiszki": NewFlashcardForm()})
