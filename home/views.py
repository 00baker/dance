from django.shortcuts import render,render_to_response,get_object_or_404
from .models import Registration

# Create your views here.
def home(request):
    return render_to_response('home/index.html',{
        'registrations': Registration.objects.all(),
    })

def contact_us(request):
    return render(request,'home/contactus.html')