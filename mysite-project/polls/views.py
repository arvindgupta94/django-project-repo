from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from .forms import ContactForm1


# Create your views here.
def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list':latest_question_list}
	#return HttpResponse(q_set)
	return render(request,'polls/index.html',context)

def detail(request,question_id):
	#try: 
		#question=Question.objects.get(id=question_id)
	#except Question.DoesNotExist:
		#raise Http404("Question does not exist")
	question=get_object_or_404(Question,pk=question_id)
		
	choices=question.choice_set.all()
	context={'question':question}
	
	return render (request,'polls/detail.html',context)
	


def vote(request, question_id):
	q=get_object_or_404(Question,pk=question_id)
	
	try:
		selected_choice=q.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		#redisplay the form with error message
		
		context={'error_message':"You didn't select a choice",'question':q}
		return render(request,'polls/detail.html',context)
	else:
		selected_choice.votes+=1
		selected_choice.save()
		
		return HttpResponseRedirect (reverse ('polls:result',args=(question_id,)))
		
	
   
def result(request,question_id):
	q=get_object_or_404(Question,pk=question_id)
	
	choices=q.choice_set.all()
	context={'question':q,'choices':choices}
	
	return render(request,'polls/result.html',context)
	
	
	
def ContactView(request):
	form=ContactForm1()
	msg='enter your contact'
	if request.method=='POST':
		f=ContactForm1(request.POST)
		if f.is_valid():
			f.save(commit=True)
			msg="Thanks for contacting"
			return render(request,'polls/ContactForm.html',{'errors':msg,'form':form})
		else:
			
			return render(request,'polls/ContactForm.html',{'errors':f.errors,'form':form})
	else:
		return render(request,'polls/ContactForm.html',{'form':form,'errors':msg})
			