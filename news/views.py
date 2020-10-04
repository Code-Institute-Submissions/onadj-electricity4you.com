from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import AddNews

from django.urls import reverse_lazy

# Create your views here.

#def newshome(request):
   # return render(request, 'newshome.html', {})

class AddNewsView(ListView):
  model = AddNews
  ordering = ['-id']
  template_name='newshome.html'

class CreateNewsView(CreateView):
  model = AddNews
  template_name = 'add_new.html'
  fields = '__all__'
  success_url = reverse_lazy('newshome')


class DeleteNewsView(DeleteView):
    model = AddNews
    template_name = 'delete_news.html'
    success_url = reverse_lazy('newshome')
