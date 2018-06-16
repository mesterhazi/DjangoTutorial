from django.db import models
from django.urls import reverse  # to generate URLs for DB records
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Science fiction, Romance)')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a short summary about the book')
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField(Genre, help_text='Genre of the book')

    def __str__(self):
        """String representation of a Book object"""
        return "{}: {}".format(self.author,  self.title)

    def get_absolute_url(self):
        """Returns a URL to access a detailed view for the record"""
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID of a particular copy of a book')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability status')

    class Meta:
        ordering = ['due_back']

    def __Str__(self):
        return '{} ({})'.format(self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns a URL to access a detailed view for the record"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)

class Language(models.Model):
    LANGS = (
        ('eng', 'English'),
        ('ger', 'German'),
        ('hun', 'Hungarian'),
        ('lat', 'Latin'),
        ('esp', 'Spanish')
    )
    name = models.CharField('Book language', max_length=3, choices=LANGS, null=True, blank=True)

    def __str__(self):
        return self.name