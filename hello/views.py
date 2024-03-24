from django.shortcuts import render
from django.views import generic
from .models import Article

from .models import Greeting


class IndexView(generic.ListView):
    model = Article


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
