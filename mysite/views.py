from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

# Create your views here.

class wellcome:
	def Home(request):
		greeting = "Assalam-O-Alaikum, I am working on Python Django Web Framework"
		Polls_App = ("<a href='http://127.0.0.1:8000/polls/' target='_blank'>Polls App</a>")
		return HttpResponse(greeting + "<br/>" + Polls_App)
