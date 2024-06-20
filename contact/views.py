from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def index(request):
    contactForm= ContactForm(request.POST or None )
    if request.method=='POST':
        if contactForm.is_valid():
           contactForm.save()
        
    context={
        'title' : 'Contact',
        'contacts' : contactForm,
        'location':'Malang',
        'email': 'achmad.irfan1@yahoo.com',
        'call': '+62-821-1425-2524',   
    }
    return render(request,'contact/index.html',context)