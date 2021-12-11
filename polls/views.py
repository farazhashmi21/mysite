from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question

# Create your views here.

def index(request):
	greeting = "Assalam-O-Alaikum, I am working on Python Django Web Framework"
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	context = { 'latest_question_list': latest_question_list, }
	return render(request, 'polls/index.html', context)
	
def detail(request, question_id):
		question = get_object_or_404(Question, pk=question_id)
		return render(request, 'polls/details.html',{'question': question})

def results(request, question_id):
	response = "You are looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on questions %s" % question_id)

class DetailView():#generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
