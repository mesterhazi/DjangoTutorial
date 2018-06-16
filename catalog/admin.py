from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language
# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
