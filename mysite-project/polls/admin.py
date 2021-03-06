from django.contrib import admin
from polls.models import Question, Choice


# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
	model=Choice
	extra=3

class QuestionAdmin(admin.ModelAdmin): #name of class can be changed not matter
	fieldsets=[
	(None,{'fields':['question_text']}),
	('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
	]
	inlines=[ChoiceInline]
	list_display=('question_text','pub_date')
	list_filter=['pub_date']
	search_fields=['question_text','pub_date']
	
admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)
