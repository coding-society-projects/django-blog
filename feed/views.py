from django.http import HttpResponse
from django.shortcuts import render

from feed.models import Article


def home(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'feed/home.html', context)


def category(request, slug):
    return render(request, 'feed/category.html')


def article(request, slug):
    context = {'article': Article.objects.filter(slug=slug).first()}
    return render(request, 'feed/article.html', context)
