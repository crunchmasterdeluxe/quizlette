from django.urls import path,re_path
from . import views 

app_name = "quizzes"

urlpatterns = [
    re_path(r"take-quiz/(?P<question_quiz>\d+)/$",views.TakeQuiz.as_view(),name="take-quiz"), #(?P<pk>\d+)
    re_path(r"all-quizzes/$",views.AllQuizzes.as_view(),name="all-quizzes")
]