from django.shortcuts import render

# Create your views here.
def landy(request):
    return render(request, 'index.html')