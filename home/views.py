from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def contact_us(request):
    return render(request,'home/contactus.html')
def payment(requset):
    return render(requset,'home/payment.html')