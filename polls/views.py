from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice


def home_page(request):
    return render(request, 'polls/home.html')


def about_page(request):
    context = {
        'message': 'this is my first django project'
    }
    return render(request, 'polls/about.html', context)


def questionaire(request):
    questions = Question.objects.all()

    context = {
        'questions': questions,
    }

    return render(request, 'polls/questionaire.html', context)
