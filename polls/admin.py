from django.contrib import admin
from .models import Question, Choice

# Register your models here.

#admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 4

class ChoiceTabular(admin.TabularInline):
	model = Choice
	extra = 4
	
class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date', 'question_text']
	fieldsets = [
	  (None, {'fields': ['question_text']}),
	  ('Date Information ', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	list_display = ('question_text','pub_date','was_published_recently')
	inlines = [ChoiceInline]
	inlines = [ChoiceTabular]
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
