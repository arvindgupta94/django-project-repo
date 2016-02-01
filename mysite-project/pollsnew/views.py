from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from pollsnew.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
import os
import re
#Create your views here.
#shows top 5 categories and top 5 questions based on hits
#link to categoryAll,categoryDetail,choiceAdd,vote
def index(request):
	#latest_question_list=Question.objects.order_by('-pub_date')[:5]
	most_hits_question_list=Question.objects.order_by('-hits')[:5]
	most_hits_category_list=Category.objects.order_by('-hits')[:5]
	context={'questions':most_hits_question_list,'categories':most_hits_category_list}
	#return HttpResponse(q_set)
	return render(request,'pollsnew/index.html',context)


	

#handles votes
@login_required
def vote(request, question_id):
	q=get_object_or_404(Question,pk=question_id)
	voteCount=1
	go=True
	burnflag=False
	burnPoints=0
	try:
		userdata=UserData.objects.filter(user=request.user,question=q)
		if userdata:
			if request.POST.get('burn'):
					#request.POST[burnPoints]:
					burnPoints=int(request.POST.get('burn'))
					#return HttpResponse(burnPoints)
					voteCount=int(burnPoints/10)
					burnflag=True
			else:
				print 'burn points not exist'
				return HttpResponse('You have already voted this question')
				go=False
	except  (UserData.DoesNotExist):
		print 'vote this question'
	
	
	if go :

		try:
			selected_choice=q.choice_set.get(pk=request.POST['choice'])
			question_category=q.category
		except (KeyError,Choice.DoesNotExist,Category.DoesNotExist):
			#redisplay the form with error message
			
			message="You didn't select a choice"
			return HttpResponse(message)
		else:
			message="Your vote has been submitted thank you !!!!"
			selected_choice.votes+=voteCount
			selected_choice.save()
			q.hits+=1
			q.save()
			question_category.hits+=1
			question_category.save()
			
			user=UserProfile.objects.get(user=request.user)
			if burnflag:
				user.points=user.points-burnPoints+burnPoints%10
				user.save()
			else:
			
				user.points+=10
				user.save()
				userdata=UserData(user=request.user,question=q,choice=selected_choice)
				userdata.save()
			return HttpResponseRedirect(reverse('pollsnew:questionDetail',args=(q.id,)))
		#return HttpResponse(request.META.get('method'))
		
	

#shows list of questions of selected category
#link to categoryAdd,questionAdd,choiceAdd,vote

def categoryDetail(request,category_id):
	c=get_object_or_404(Category,pk=category_id)
	
	questions_list=c.questionsofcategory().order_by('-hits')
	context={'questions':questions_list,'category':c}
	print request.META['HTTP_REFERER']
	print request.META['REMOTE_ADDR']
	
	return render (request,'pollsnew/categoryDetail.html',context)


#shows whole list of category
#link to categoryDetail,categoryAdd
def categoryAll(request):
	categories=Category.objects.order_by('-hits')
	
	return render(request,'pollsnew/categoryAll.html',{'categories':categories})
	
	
#adds a new category and handle forms submission
#redirect to categoryDetail page of the new category
@login_required
def categoryAdd(request):
	if request.method=='POST':
		try:
			categoryName=request.POST['category_name']
			if (Category.objects.get(category_name__iexact=categoryName)):
				error_message="!! ERROR !! Category wIth same name already exist "
				return render(request,'pollsnew/categoryAdd.html',{'error_message':error_message})
		except(KeyError):
			error_message="!!ERROR !! You didn't enter the name "
			return render(request,'pollsnew/categoryAdd.html',{'error_message':error_message})
		
		except(Category.DoesNotExist):
			c=Category(category_name=request.POST['category_name'],addedBy=request.user)
			c.save()
			user=UserProfile.objects.get(user=request.user)
			user.points+=10
			user.save()
			#return HttpResponseRedirect('/pollsnew/category/all/')
			return HttpResponseRedirect(reverse('pollsnew:categoryDetail',args=(c.id,)))
	else:
		return render(request,'pollsnew/categoryAdd.html',{})
		
		
		
	
#adds a new choice to the question
#redirect to questionDetail page
def choiceAdd(request,question_id):
	if request.method=='POST':
		try:
			q=Question.objects.get(pk=question_id)
			c=Choice(choice_text=request.POST['choice_text'],question=q,addedBy=request.user)
			c.save()
			user=UserProfile.objects.get(user=request.user)
			user.points+=20
			user.save()
			return HttpResponseRedirect(reverse('pollsnew:questionDetail',args=(q.id,)))
		except(Question.DoesNotExist):
			error_message='Question does not exist'
			return HttpResponse(request,error_message)
		except(KeyError):
			error_message="!!ERROR !! You didn't enter any value"
			q=Question.objects.get(pk=question_id)
			context={'error_message':error_message,'question':q}
			return render(request,'pollsnew/choiceAdd.html',context)
	else:
		
		q=Question.objects.get(pk=question_id)
		context={'question':q}
		return render(request,'pollsnew/choiceAdd.html',context)
		
		
#adds a new question
#redirects to questionDetail page of new question
def questionAdd(request,category_id):
		c=get_object_or_404(Category,pk=category_id)
		if request.method=='POST':
			try:
				questionText=request.POST['question_text']
				q=Question(question_text=questionText,category=c,addedBy=request.user)
				q.save()
				user=UserProfile.objects.get(user=request.user)
				user.points+=50
				user.save()
				return HttpResponseRedirect(reverse('pollsnew:questionDetail',args=(q.id,)))
			except(KeyError):
				error_message="!! ERROR !! You didn't entered any value !"
				return render(request,'pollsnew/questionAdd.html',{'category':c,'error_message':error_message})
		else:
			return render(request,'pollsnew/questionAdd.html',{'category':c})
		
	
	
def questionDetail(request,question_id):
	q=get_object_or_404(Question,pk=question_id)
	msg=q.choicesofquestion()
	flag=False
	try:
		if UserData.objects.filter(user=request.user,question=q):
			flag=True
		
	except  (UserData.DoesNotExist):
		print 'vote this question'
	if request.user.is_authenticated() :
		userProfile=UserProfile.objects.get(user=request.user)
		points=userProfile.points
	return render(request,'pollsnew/questionDetail.html',{'question':q,'msg':msg,'flag':flag,'userPoints':points})
	
def arvind(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
	
	
def login_view(request):
	message=''
	next=False
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		next=request.POST.get('next',False)
		user=authenticate(username=username,password=password)
		
		if user:
			if user.is_active:
				login(request,user)
				message='you are logged in'
				if next:
					return HttpResponseRedirect (next)
				else: 
					return HttpResponseRedirect('/pollsnew/')
			else:
				message='user is not active'
		else:
			message='Username or password is incorrect'
	else:
		message='Login Please to continue'
	
	if not next:
		next=request.META.get('HTTP_REFERER','/pollsnew/')
	return render(request,'pollsnew/login.html',{'message':message,'next':next})
		
	
		
		
@login_required		
def logout_view(request):
	logout(request)
	#return HttpResponseRedirect(reverse('pollsnew:index'))
	return HttpResponseRedirect(request.GET['next'])
	
	


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save() 
		    
		    # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
		    
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
			
            

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'pollsnew/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
			
@login_required		
def profile(request):
	userdata=UserData.objects.filter(user=request.user)
	userpoints=UserProfile.objects.get(user=request.user).points
	return render(request,'pollsnew/profile.html',{'userdata':userdata,'userpoints':userpoints})
	