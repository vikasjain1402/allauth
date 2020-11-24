from django.db import models
#from allauth.account.models import EmailAddress
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    askedby=models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    question=models.TextField(blank=False)
    questiondate=models.DateTimeField(auto_now_add=True)
    
class Answer(models.Model):
    question=models.ForeignKey(Question,blank=False,on_delete=models.CASCADE)
    answerby=models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    answer=models.TextField(blank=False)
    answerdate=models.DateTimeField(auto_now_add=True)
    