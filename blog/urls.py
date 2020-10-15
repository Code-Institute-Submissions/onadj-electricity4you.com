from django.urls import path
from .views import HomeView, ArticleDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    #path('', views.home, name="blog"), 
    path('', HomeView.as_view(), name="blog"),
    path('article/<int:pk>/', ArticleDetailView.as_view(),
    name='article-detail'),
]