from django.contrib import admin
from . import models

admin.site.register(models.Quiz)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['quiz','question_text']
admin.site.register(models.Question, QuestionAdmin)
