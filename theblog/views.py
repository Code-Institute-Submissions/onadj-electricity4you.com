from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'blog.html'
    ordering = ['-post_date']
    #ordering = ['-id']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddCategoryView(CreateView):
    model = Category
     #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'body', ... )

class AddPostView(CreateView):
    model=Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'body', ... )

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']
  
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog')