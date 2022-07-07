from django.shortcuts import render
from django.views import generic
from quizzes.models import Question,Quiz
from django.http import HttpResponse,HttpResponseRedirect
# from django.utils.decorators import method_decorator
# from django.utils.decorators import csrf_exempt

# @method_decorator(csrf_exempt,name='dispatch')
class TakeQuiz(generic.ListView):
    model = Question
    template_name = "take-quiz.html"

    def get_context_data(self, **kwargs):
        # Queries
        context = super().get_context_data(**kwargs)
        self.quiz = Quiz.objects.values('id','name').get(pk=self.kwargs.get("question_quiz"))
        print(self.quiz)
        self.questions = Question.objects.filter(quiz__id=self.quiz.get("id")).all() #.values_list['answer']
        # This is the equivalent of sql's "Select * from questions where quiz_id = [url_param id];"
        print(self.questions)

        # Context - pass to template
        context['quiz'] = self.quiz
        context['questions'] = self.questions

        return context

    def post(self,*args,**kwargs):
        # context = super().get_context_data(**kwargs)
        # print(context)
        self.quiz = Quiz.objects.values('id','name').get(pk=self.kwargs.get("question_quiz"))
        questions = Question.objects.filter(quiz__id=self.quiz.get("id")).all()
 
        username = self.request.user
        print(username)
        if self.request.method == "POST":
            for i in questions:
                answer = self.request.POST.get(f"{i.question_number}_answer")
                if answer == i.answer:
                    print(i.question_number,"Correct!")
                else:
                    print(i.question_number,"Wrong")
            
        return HttpResponseRedirect("#")

class AllQuizzes(generic.ListView):
    model = Quiz
    template_name = "all-quizzes.html"

    def get_context_data(self, **kwargs):
        # Queries
        context = super().get_context_data(**kwargs)
        self.quizzes = Quiz.objects.values('id','name').all()
        
        # Context - pass to template
        context['quizzes'] = self.quizzes

        return context