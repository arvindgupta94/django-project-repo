from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	category_name=models.CharField(max_length=200)
	date_created=models.DateTimeField('date created',default=timezone.now)
	hits=models.IntegerField(default=0)
	addedBy=models.ForeignKey(User,default=1)
	def __unicode__(self):
		return self.category_name
	
	def questionsofcategory(self):
		return self.question_set.all()
	
	
class Question (models.Model):
	category=models.ForeignKey(Category)
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published',default=timezone.now)
	hits=models.IntegerField(default=0)
	addedBy=models.ForeignKey(User,default=1)
	
	def __unicode__(self):
		return self.question_text
		
	def choicesofquestion(self):
		
		return self.choice_set.all()
	
class Choice (models.Model):
	question=models.ForeignKey(Question)
	choice_text=models.CharField(max_length=200)
	votes=models.IntegerField(default=0)
	addedBy=models.ForeignKey(User,default=1)
	
	def __unicode__(self):
		return self.choice_text

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
	
	
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    points=models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class UserData (models.Model):
	user=models.ForeignKey(User)
	question=models.ForeignKey(Question)
	choice=models.ForeignKey(Choice)
	
	def __unicode__(self):
		data=self.user.username+"voted to "+self.choice.choice_text+" for Question "+self.question.question_text
		
		return data
	