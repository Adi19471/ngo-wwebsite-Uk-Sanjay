from django.shortcuts import render

from .models import ContactForm

# Create your views here.
def home(request):
    return render(request, 'Home/home.html')


def About(request):
    return render(request, 'Home/About.html')


def Donate(request):
    return render(request, 'Home/Donate.html')

def Gallery(request):
    return render(request, 'Home/Gallery.html')



def Sponserroom(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        ContactForm(
           first_name = first_name,
           email = email,          
           mobile = mobile,
           message = message,
       ).save()
        return render(request, 'Home/Sponserroom.html')
    else:
        return render(request, 'Home/Sponserroom.html')
   


