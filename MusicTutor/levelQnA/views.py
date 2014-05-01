# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from levelQnA.models import questions

def getQuestions(request, lesson_id):
	returnQList = list(questions.objects.filter(level_id = lesson_id))

	return render_to_response('questions.html', {'questions' : returnQList}, context_instance = RequestContext(request))