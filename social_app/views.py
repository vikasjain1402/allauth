from django.shortcuts import render
from allauth.account.decorators import login_required
from allauth.account.models import EmailAddress
from .forms import Questionform,Answerform
from .models import Question,Answer
from django.http import HttpResponse, HttpResponseNotFound
import datetime as dt
from django.contrib.auth.models import User

@login_required
def answer(request):

    user=User.objects.get(email=request.user.email)  
    context={}
    context['user']=user
    # print("get_expire_at_browser_close",request.session.get_expire_at_browser_close())
    # print("get_expiry_age",request.session.get_expiry_age())
    # print("get_expiry_date",request.session.get_expiry_date())
    # print("get_session_cookie_age",request.session.get_session_cookie_age())
    
    
    if request.method=="GET":        
        qid=request.GET['questionid']
        try:
            question=Question.objects.get(id=qid)                
        except:
            return HttpResponse('<h1>Page was found</h1>')    
        context['answerform']=Answerform(initial={'question':question.question})
        request.session['id']=qid
        answers=Answer.objects.filter(question=question)
        context['answers']=answers
    else:
        answerformdata=Answerform(request.POST)
        if answerformdata.is_valid():       
            ans=Answer() 
            question=Question.objects.get(id=request.session['id'])
            already_answered=len(Answer.objects.filter(answerby=user,question=question))
            
            if already_answered>=1:     
                Answer.objects.get(answerby=user,question=question).delete()

            ans.answer=answerformdata.cleaned_data['answer']
            ans.question=question
            ans.answerby=user                                
            ans.save()                                                                                
        else:       
            context['answerform']=Answerform() 
    
    return render(request,'answer.html',context=context)



@login_required
def question(request):
    user=User.objects.get(email=request.user.email)  
    context={}
    context['user']=user
    if request.method=="GET":
        context['form']=Questionform()
      
    else:
        questionformdata=Questionform(request.POST)
        if questionformdata.is_valid():
            ques=Question()
            ques.question= questionformdata.cleaned_data['question']
            ques.askedby=User.objects.get(email=user.email)
            ques.save()
            context['thanks']="thanks! Question submitted successfully "
            
            results=Question.objects.filter().order_by("-questiondate")
            context['results']=results
            return render(request,"result.html",context=context)
          
        else:       
            context['form']=Questionform(request.POST) 
    
    return render(request,'question.html',context=context)