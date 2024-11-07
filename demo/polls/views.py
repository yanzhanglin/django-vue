# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world.You're at the polls index")

def detail(request,question_id):
    return HttpResponse(f"you are looking at question {question_id}.")

def results(request,question_id):
    response = f"you are looking at the result of question{question_id}."
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse(f"you are voting on question{question_id}")
# Create your views here.
