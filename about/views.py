from django.shortcuts import render
from django.views.generic import TemplateView


class About_View(TemplateView):
    template_name = 'weerget/about.html'
