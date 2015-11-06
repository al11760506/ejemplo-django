from django.contrib import admin
from models import Publisher, Author, Book
from django.db import models

# Register your models here.

class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'publisher', 'publication_date')
        list_filter = ('publisher', 'publication_date')
        ordering = ('-publication_date',)
        search_fields = ('title',)

class AuthorAdmin(admin.ModelAdmin):
	  list_display= ('name','email','headshot')
	  search_fields= ('name',)

class PublisherAdmin(admin.ModelAdmin):
    list_display =('name','address','city')
    list_filter=('city','country','state_province')
    search_fields= ('name',)

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
