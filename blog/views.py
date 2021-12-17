from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article

# Create your views here.
def list(request):

    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': articles
    })


def category(request, category_id):

    # TODO: asi se hace una consulta a la BD
    # category = get_object_or_404(Category, id=category_id)
    category = Category.objects.get(id=category_id)
    # articles = Article.objects.filter(categories=category)

    # TODO: llama al template
    return render(request, 'categories/category.html', {
        'category': category,
        # 'articles':articles
    })

def article(request, article_id):

    # TODO: asi se hace una consulta a la BD
    # category = get_object_or_404(Category, id=category_id)
    article = Article.objects.get(id=article_id)
    # articles = Article.objects.filter(categories=category)

    # TODO: llama al template
    return render(request, 'articles/detail.html', {
        'article': article,
        # 'articles':articles
    })
