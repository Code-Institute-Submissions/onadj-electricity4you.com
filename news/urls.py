from django.urls import path
from .views import AddNewsView, CreateNewsView, DeleteNewsView

urlpatterns = [
      path('', AddNewsView.as_view(), name ='newshome'),
      path('addnew/', CreateNewsView.as_view(), name ='addnew'),
      path('remove/<int:pk>/', DeleteNewsView.as_view(), name='deletenews'),
]
