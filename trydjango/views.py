from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string




def home_view(request):
    article_obj = Article.objects.get(id=1)
    article_queryset = Article.objects.all()
    print(article_queryset)

    context = {
        "article_queryset": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "content": article_obj.content
    }
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)