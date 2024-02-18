from django.contrib import admin
from .models import Flashcard, UserFlashcardOwnership


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(UserFlashcardOwnership)
class UserFlashcardOwnershipAdmin(admin.ModelAdmin):
    ...
