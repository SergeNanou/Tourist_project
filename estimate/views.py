from django.shortcuts import render
from .forms import EstimateForm
# Create your views here.
# Create your views here.

def post_new(request):
    form = EstimateForm()
    return render(request, 'estimate/post_edit.html', {'form': form})
