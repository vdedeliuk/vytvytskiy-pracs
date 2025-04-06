from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from .models import Article, Category
from .forms import ArticleImageForm, ArticleForm

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = ArticleImageForm()
        posts = Article.objects.prefetch_related('images').all()
        categories = Category.objects.all()
        return render(request, 'index.html', {'form': form, 'posts': posts, 'categories': categories})

    def post(self, request, **kwargs):
        form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        posts = Article.objects.prefetch_related('images').all()
        categories = Category.objects.all()
        return render(request, 'index.html', {'form': form, 'posts': posts, 'categories': categories})

@require_POST
def delete_post(request, post_id):
    post = get_object_or_404(Article, id=post_id)
    post.delete()
    return redirect('home')

def manage_posts(request):
    if request.method == 'POST':
        form = ArticleImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleImageForm()
    posts = Article.objects.prefetch_related('images').all()
    return render(request, 'index.html', {'form': form, 'posts': posts})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})