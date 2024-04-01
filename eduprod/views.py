from django.core import serializers
from django.shortcuts import render
from .models import Question
from django.contrib.auth.decorators import login_required

def index(request):
    quiz_type = request.GET.get('quiz_type', 'M-E')  
    
    if quiz_type == 'M-E':
       
        pass
    elif quiz_type == 'E-M':
       
        pass
    

@login_required
def index(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions)
    return render(request, 'eduprod/index.html', {'questions_json': questions_json})