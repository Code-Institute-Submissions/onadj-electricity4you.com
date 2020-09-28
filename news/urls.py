from django.urls import path
from .views import AddNews

urlpatterns = [
      path('', AddNews.as_view(), name ='newshome'),
]