from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

from .models import Greeting


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'hello/index.html', context)


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
