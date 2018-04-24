from django.shortcuts import render_to_response, get_object_or_404
from .models import Article


# Create your views here.
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {}
    context['article'] = article
    # return render(request, 'article_detail.html', context)
    return render_to_response('article_detail.html', context)
    # return HttpResponse('<h2>{}</h2> <br> <p>{}</p>'.format(article.title, article.content))


def article_list(request):
    article = Article.objects.all()
    context={}
    context['articles'] = article
    return render_to_response('article_list.html', context)