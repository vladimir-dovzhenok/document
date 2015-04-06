from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
from matan.models import  Author, Theorem, Categories, Term
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(
        template_name='matan/base.html')),
    url(r'^author/$', ListView.as_view(
        model=Author,
        template_name='matan/author.html',
        context_object_name='author')),
    url(r'^theorem/$', ListView.as_view(
        model=Theorem,
        template_name='matan/theorem_list.html',
        context_object_name='theorem_list')),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(
        model=Theorem,
        template_name='matan/theorem_detail.html',
        context_object_name='theorem_detail')),
    url(r'^term/$', ListView.as_view(
        model=Term,
        template_name='matan/term_list.html',
        context_object_name='term_list')),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Term,
        template_name='matan/term_detail.html',
        context_object_name='term_detail')),
    )