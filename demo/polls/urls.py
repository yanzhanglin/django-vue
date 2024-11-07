from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),                                 #  /polls/
    path("<int:question_id>/",views.detail,name="detail"),             #  /polls/1
    path("<int:question_id>/results",views.results,name="results"),    #  /polls/1/results
    path("<int:question_id>/vote",views.vote,name="vote")              #  /polls/1/vote
]