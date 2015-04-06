# -*- coding: utf-8 -*-
from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Категория')
    theorem = models.ForeignKey('Theorem', verbose_name=u'Теорема')
    term = models.ForeignKey('Term', verbose_name=u'Термин')

    def __unicode__(self):
        return self.title

class Theorem(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Теорема')
    substantiation = models.TextField(verbose_name=u'Доказательство')
    author = models.ManyToManyField('Author', verbose_name=u'Автор')
    term = models.ManyToManyField('Term', verbose_name=u'Термин')

    def __unicode__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u'Имя')
    last_name = models.CharField(max_length=100, verbose_name=u'Фамилия')
    biagrafiya = models.TextField(verbose_name=u'Биаграфия')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Term(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'Термин')
    determination = models.TextField(verbose_name=u'Определение')

    def __unicode__(self):
        return self.title


