from django.shortcuts import render
from django.http import HttpResponse
from .models import Speech,Speaker
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# Create your views here.


def index(request):
    return render(request,'speech/welcome.html')

    

def home(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request,'speech/home.html',context)

class PostListView(ListView):
    model = Speech
    template_name = 'speech/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']
    paginate_by = 3

def about(request):
    context = {
        'posts': Speech.objects.all()
    }
    return render(request, 'speech/about.html',context)


def Speakview(request):
    context = {
        'queryset': Speaker.objects.all()
    }
    return render(request, 'speech/speaker.html',context)







