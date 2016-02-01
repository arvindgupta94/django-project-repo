from polls.models import Question, Choice
from django.utils import timezone

#q=Question(question_text='What is your favorite colour ?',pub_date=timezone.now())
#q2=Question(question_text='Who is your favorite actor',pub_date=timezone.now())
q3=Question(question_text='Who is your favorite actoress ?',pub_date=timezone.now())
q4=Question(question_text='Who is your favorite cricketer ?',pub_date=timezone.now())
q5=Question(question_text='Who is your favorite super hero ?',pub_date=timezone.now())
q6=Question(question_text='Who is favorite cricket captain of all time ?',pub_date=timezone.now())
q7=Question(question_text='Which type of movie you like much ?',pub_date=timezone.now())
q8=Question(question_text='What is most important to you ?',pub_date=timezone.now())
q9=Question(question_text='Which is your favorite subject ?',pub_date=timezone.now())
q10=Question(question_text="What is the thing you can't live without ?",pub_date=timezone.now())

#q.choice_set.create(choice_text='Red')
#q.choice_set.create(choice_text='Green')
#q.choice_set.create(choice_text='Blue')
#q.choice_set.create(choice_text='Pink')
#q.choice_set.create(choice_text='Yellow')

#q2.choice_set.create(choice_text='SRK')
#q2.choice_set.create(choice_text='Salman')
#q2.choice_set.create(choice_text='AMir')
#q2.choice_set.create(choice_text='AMitab')
#q2.choice_set.create(choice_text='Akshay')

q3.choice_set.create(choice_text='Aishwarya')
q3.choice_set.create(choice_text='Priankya chopra')
q3.choice_set.create(choice_text='Deepika Padukone')
q3.choice_set.create(choice_text='Alia Bhatt')
q3.choice_set.create(choice_text='Parnitee chopra')

#q4.choice_set.create(choice_text='Sachin tendulkar')
#q4.choice_set.create(choice_text='Saurav Ganguly')
#q4.choice_set.create(choice_text='irendra Sehwag')
#q4.choice_set.create(choice_text='Yuvraj Singh')
#q4.choice_set.create(choice_text='MS Dhoni')

q5.choice_set.create(choice_text='Shaktiman')
q5.choice_set.create(choice_text='Iron man')
q5.choice_set.create(choice_text='Batman')
q5.choice_set.create(choice_text='Harry Potter')
q5.choice_set.create(choice_text='Spider Man')

q6.choice_set.create(choice_text='Saurav Ganguly')
q6.choice_set.create(choice_text='MS Dhoni')
q6.choice_set.create(choice_text='Kapil dev')
q6.choice_set.create(choice_text='Virat Kohli')






