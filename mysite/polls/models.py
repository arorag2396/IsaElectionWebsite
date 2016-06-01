import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
		
		
class Person(models.Model):
	name = models.CharField(max_length=200)
	email = models. EmailField()
	uniqueCode = models.CharField(max_length=100)
	voted = models.NullBooleanField()
	def __str__(self):
		return self.name
	def votingCompleted(self):
		voted = True

class totalNumberOfVotes(models.Model):
	number = models.IntegerField(default=0)
	
