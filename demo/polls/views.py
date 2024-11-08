# from django.shortcuts import render

from django.http import HttpResponse
from .models import Question

def index(request):
    last_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ",".join([q.quetion_text for q in last_question_list])
    return HttpResponse(output)

def detail(request,question_id):
    return HttpResponse(f"you are looking at question {question_id}.")

def results(request,question_id):
    response = f"you are looking at the result of question{question_id}."
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"you are voting on question{question_id}")
# Create your views here.
