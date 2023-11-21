from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstance, Publisher


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'data_of_birth', 'photo')


# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')

