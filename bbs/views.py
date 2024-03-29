from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.core.exceptions import PermissionDenied


class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'


class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


def search(request):
    articles = None
    searchform = SearchForm(request.GET)
    if searchform.is_valid():
        query = searchform.cleaned_data['query']
        articles = Article.objects.filter(content__icontains=query)
    return render(request, 'bbs/results.html', {'searchform': searchform, 'articles': articles})
