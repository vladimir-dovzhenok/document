from django.contrib import admin
from matan.models import Author,Categories, Term, Theorem

admin.site.register(Author)
admin.site.register(Theorem)
admin.site.register(Term)
admin.site.register(Categories)
