from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    no1 = int(request.GET.get('num1'))
    no2 = int(request.GET.get('num2'))
    
    answer = no1+no2
    return render (request, 'result.html', {'answer':answer})
