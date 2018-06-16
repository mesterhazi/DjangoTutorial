from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language
# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth']

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ['status', 'due_back']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
