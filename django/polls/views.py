from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question


def detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))
