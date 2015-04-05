# -*- coding: utf-8 -*-
from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=100)
    theorem = models.ForeignKey('Theorem')
    term = models.ForeignKey('Term')

    def __unicode__(self):
        return self.title

class Theorem(models.Model):
    title = models.CharField(max_length=100)
    substantiation = models.TextField()
    author = models.ManyToManyField('Author')
    term = models.ManyToManyField('Term')

    def __unicode__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biagrafiya = models.TextField()

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Term(models.Model):
    title = models.CharField(max_length=100)
    determination = models.TextField()

    def __unicode__(self):
        return self.title


