from django.shortcuts import render
from .models import Article 
# Create your views here.
def articles_list(request):
    articles = Article.objects.all().order_by('date_published')
    return render(request, 'articles/articles_list.htm', {'articles': articles})