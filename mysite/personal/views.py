from django.shortcuts import render
from .models import Question

# Create your views here.
def  home_screen_view(request):
    context = {}

    # list_of_values = ['First Entry', 'Second Entry', 'Third entry', 'Fourth Entry']
    # context['list_of_values'] = list_of_values

    questions = Question.objects.all()
    context['questions'] = questions

    
    return render(request, 'personal/home.html', context)