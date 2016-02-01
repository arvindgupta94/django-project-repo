from django.contrib import admin
from pollsnew.models import Question, Choice, Category, UserProfile


# Register your models here.
#class ChoiceInline(admin.StackedInline):

admin.site.register(Choice)
admin.site.register(Question)
#admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(UserProfile)
