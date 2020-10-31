from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
