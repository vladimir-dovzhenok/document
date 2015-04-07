# -*- coding: utf-8 -*-
from django.contrib import admin
from matan.models import Author, Categories, Term, Theorem

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class TheoremAdmin(admin.ModelAdmin):
    list_display = ('title', 'substantiation', 'author_name')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Theorem, TheoremAdmin)
admin.site.register(Term)
admin.site.register(Categories)
