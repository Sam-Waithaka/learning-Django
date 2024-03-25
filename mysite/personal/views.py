from django.shortcuts import render

# Create your views here.
def  home_screen_view(request):
    context = {}

    list_of_values = ['First Entry', 'Second Entry', 'Third entry', 'Fourth Entry']
    context['list_of_values'] = list_of_values
    
    return render(request, 'personal/home.html', context)