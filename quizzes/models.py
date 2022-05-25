from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    name = models.CharField(max_length=512,null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

class Question(models.Model):
    quiz = models.ForeignKey(Quiz,related_name='question_quiz',null=False,on_delete=models.PROTECT) #Quizzes have questions
    question_number = models.IntegerField(default=1,null=False)
    question_text = models.CharField(max_length=1027,null=False)
    answer = models.CharField(max_length=1027,null=False)
    false_answer_1 = models.CharField(max_length=1027,null=True)
    false_answer_2 = models.CharField(max_length=1027,null=True)
    false_answer_3 = models.CharField(max_length=1027,null=True)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse(
            "quizzes:take-quiz",
            kwargs = {
                "pk": self.pk,
                "question_quiz": self.quiz.pk
            }
        )

    class Meta:
        verbose_name = 'Quiz Question'
        verbose_name_plural = 'Quiz Questions'