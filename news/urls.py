from django.urls import path
from .views import AddNewsView, CreateNewsView

urlpatterns = [
      path('', AddNewsView.as_view(), name ='newshome'),
      path('addnew/', CreateNewsView.as_view(), name ='addnew'),
]
