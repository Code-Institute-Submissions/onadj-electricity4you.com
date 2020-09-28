from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import AddNews
# Create your views here.

#def newshome(request):
   # return render(request, 'newshome.html', {})

class AddNews(ListView):
  model = AddNews
  template_name='newshome.html'
