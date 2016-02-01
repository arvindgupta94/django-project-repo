import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
import django
django.setup()
from pollsnew.models import *



def add_category(category_name):
	cat=Category.objects.get_or_create(category_name=category_name)[0]
	cat.save()
	return cat

def add_question(category,question_text):
	q=Question.objects.get_or_create(category=category,question_text=question_text)[0]
	q.save()
	return q

def add_choice(question,choice_text):
	c=Choice.objects.get_or_create(question=question,choice_text=choice_text)[0]
	c.save()
	return c
	
def populate():
	#sample 
	#cat=add_category()
	#q_cat=add_question(category=cat,question_text="")
	#c_q_cat=add_choice(question=catq,choice_text="")
	
	cat1=add_category('Picninc Spot')
	
	q1_cat1=add_question(category=cat1,question_text='Which is the best waterfall of Ranchi ? ')
	
	c1_q1_cat1=add_choice(question=q1_cat1,choice_text='Hundru Fall')
	c2_q1_cat1=add_choice(question=q1_cat1,choice_text='Dasam Falls')
	c3_q1_cat1=add_choice(question=q1_cat1,choice_text='Jhonha Fall')
	c4_q1_cat1=add_choice(question=q1_cat1,choice_text='Hirni Fall')
	
	q2_cat1=add_question(category=cat1,question_text="Which one is the best Dam for picnic in Ranchi ?" )
	
	c1_q2_cat1=add_choice(question=q2_cat1,choice_text="Rukka Dam")
	c2_q2_cat1=add_choice(question=q2_cat1,choice_text="Getalsud dam")
	c3_q2_cat1=add_choice(question=q2_cat1,choice_text="Kanke Dam")
	c4_q2_cat1=add_choice(question=q2_cat1,choice_text="Dhurwa Dam")
	
	cat2=add_category('Movies')
	q1_cat2=add_question(category=cat2,question_text="Best Multiplex in Ranchi ?")
	
	c1_q1_cat2=add_choice(question=q1_cat2,choice_text="Glitz Cinema")
	c2_q1_cat2=add_choice(question=q1_cat2,choice_text="Fun Cinemas")
	c3_q1_cat2=add_choice(question=q1_cat2,choice_text="Popcorn Cinema")
	
	
	
if __name__=='__main__':
	print "Starting populating the Pollsnew Database ......."
	populate()
	
	
	
	
	
	
	
	
		
	