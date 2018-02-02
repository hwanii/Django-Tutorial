from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from polls.models import Question, Choice


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)  # 에러가 빈번하게 발생하기 때문에 shortcut으로 존재함.
    context = {
        'question': question
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    pk = request.POST['choice']
    # 어차피 Choice 테이블에 question_id가 있기 때문에 question이 어떤것인지 확인할 필요없이 votes 값을 증가시키면 됨.
    choice = Choice.objects.get(pk=pk)
    choice.votes += 1
    choice.save()
    return redirect('polls:results', question_id=question_id)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # template = loader.get_template('poll/index.html')
    # return HttpResponse(template.render(context, request))
