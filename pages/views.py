from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {
        'course': 'IT 373',
        'name': 'Euan Josh Amor',
        'student_id': '2023-00187',
    }
    return render(request, 'pages/home.html', ctx)

def hello(request):
    return render(request, 'pages/hello.html')

def about(request):
    ctx = {
        'course': 'IT 373',
        'name': 'Euan Josh Amor',
        'student_id': '2023-00187',
    }
    return render(request, 'pages/about.html', ctx)

