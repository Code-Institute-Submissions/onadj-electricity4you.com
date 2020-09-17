from django.shortcuts import render
from .models import Deliverycost

# Create your views here.

def all_deliverycost(request):
    """ A view to show all delivery cost """

    deliverycost = Deliverycost.objects.all()

    context = {
        'deliverycost' : deliverycost, 
    }

    return render(request, 'shipping/shipping.html', context)
