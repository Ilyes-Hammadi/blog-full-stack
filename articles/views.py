from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import ArticleCreateForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
       'articles' : articles
    }
    return render(request, 'index.html', context)

def detail(request, id):

    article = get_object_or_404(Article, pk=id)

    context ={
        'article' : article
    }
    return render(request, 'detail.html', context)

def create(request):
    
    # If request is POST then save the data
    if(request.method == 'POST'):
        form = ArticleCreateForm(request.POST, request.FILES)
        
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
        
        return redirect('index')
    # If request is not POST then return the form
    else:
        form = ArticleCreateForm()
        context = {
            'form' : form
        }
        return render(request, 'form.html', context)


def update(request, id):
    
    # Get the article to update
    article = get_object_or_404(Article, pk=id)

    # If request is POST then save the data
    if(request.method == 'POST'):
        form = ArticleCreateForm(request.POST, instance=article)
        
        if form.is_valid():
            form.save()
        
        return redirect('index')
    # If request is not POST then return the form
    else:
        form = ArticleCreateForm(instance=article)
        context = {
            'form' : form
        }
        return render(request, 'form.html', context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('index')