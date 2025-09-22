from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        'course': 'IT 373',
        'name': 'Euan Pogi',
    }
    return render(request, 'pages/home.html', ctx)

def hello(request):
    return render(request, 'pages/hello.html')

def about(request):
    return render(request, 'pages/about.html')

