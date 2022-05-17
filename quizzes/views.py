from django.shortcuts import render
from django.views import generic
from quizzes.models import Question,Quiz

# Create your views here.
class TakeQuiz(generic.ListView):
    model = Question
    template_name = "take-quiz.html"

    def get_context_data(self, **kwargs):
        # Queries
        context = super().get_context_data(**kwargs)
        self.quiz = Quiz.objects.values('id','name').get(pk=self.kwargs.get("question_quiz"))
        print(self.quiz)
        self.questions = Question.objects.filter(quiz__id=self.quiz.get("id")).all()
        print(self.questions)

        # Context - pass to template
        context['quiz'] = self.quiz
        context['questions'] = self.questions

        return context
