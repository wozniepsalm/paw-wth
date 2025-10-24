from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, Osoba, stanowisko
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba)
admin.site.register(stanowisko)