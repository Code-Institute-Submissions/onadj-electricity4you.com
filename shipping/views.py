from django.shortcuts import render
from .models import Deliverytime

# Create your views here.

def all_deliverytime(request):
    """ A view to show all delivery time """

    deliverytime = Deliverytime.objects.all()

    context = {
        'deliverytimes': deliverytime, 
    }

    return render(request, 'shipping/shipping.html', context)