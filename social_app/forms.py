from django import forms

class Questionform(forms.Form):
    question=forms.CharField(label='Question',widget=forms.Textarea)

class Answerform(forms.Form):
    question=forms.CharField(label='question',widget=forms.Textarea,disabled=True,required=False)
    answer=forms.CharField(label='answer',widget=forms.Textarea)

    