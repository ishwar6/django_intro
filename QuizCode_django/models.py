from django.db import models
from django.contrib.auth.models import User

class Test_topic(models.Model):
 creator=models.ForeignKey(User, on_delete=models.CASCADE)
 topic = models.CharField(max_length=200)
 description = models.CharField(max_length=200)
 total_test_time_in_minutes=models.IntegerField(default=0)
 def __str__(self):
   return self.topic
# Create your models here.

class TestsTaken(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	topic=models.ForeignKey(Test_topic, on_delete=models.CASCADE)
	score=models.IntegerField(default=0)
	def __str__(self):
		return str(self.user)+str(self.topic)

class Question(models.Model):
	topic=models.ForeignKey(Test_topic, on_delete=models.CASCADE)
	question_text=models.CharField(max_length=200)
	qno=models.IntegerField(default=0)
	level = models.IntegerField(default=0)
	question_image=models.ImageField(blank=True, null=True, upload_to="questions")
	text_option1=models.CharField(blank=True, max_length=200)
	text_option2=models.CharField(blank=True, max_length=200)
	text_option3=models.CharField(blank=True, max_length=200)
	text_option4=models.CharField(blank=True, max_length=200)
	op1=models.BooleanField(default=False)
	op2=models.BooleanField(default=False)
	op3=models.BooleanField(default=False)
	op4=models.BooleanField(default=False)
	time_in_minutes=models.IntegerField(default=0)
	score=models.IntegerField(default=0)
	integer_type=models.BooleanField(default=False)
	single_option=models.BooleanField(default=False)
	integer_type_answer=models.CharField(blank=True, max_length=200)
	answer_image=models.ImageField(blank=True, null=True, upload_to="answers")
	answer_text = models.CharField(blank=True, max_length=200)
	def __str__(self):
		return self.question_text
    #option1 = models.BooleanField(default=False)
    #pub_date = models.DateTimeField('date published')


    

class User_submission(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	op1=models.BooleanField(default=False)
	op2=models.BooleanField(default=False)
	op3=models.BooleanField(default=False)
	op4=models.BooleanField(default=False)
	integer_type_submission=models.CharField(blank=True, max_length=200)
	time_of_sumbission=models.CharField(blank=True, max_length=200)
	submitted_by_user=models.BooleanField(default=False)
	correctans=models.BooleanField(default=False)
	def __str__(self):
		return str(self.question.id)+str(self.user)
