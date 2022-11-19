from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    context ={
        'about': About.objects.all,
        'services': service.objects.all(),
        'prof_exp': professional_experience.objects.all(),
        'resume':Resume.objects.all(),
        'experties': expertie.objects.all(),
        'prijects': projects.objects.all(),
        'price': price.objects.all(),
        'contact': contact_me.objects.all(),
    }
    return render(request, 'index.html', context)

def admin(request):
    return redirect(request,'admin')