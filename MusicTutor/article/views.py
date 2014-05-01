# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext 

from article.models import articles
 
def home(request):
    return render_to_response('index.html', context_instance = RequestContext(request))


def article(request, lesson_id):
	db_article = articles.objects.get(level = lesson_id)
	return render_to_response('articles.html', {'article' : db_article}, context_instance = RequestContext(request))