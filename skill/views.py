from django.shortcuts import render
from .models import Skillsss
# Create your views here.


def index(request):
    skillss = Skillsss.objects.all()
    context = {
        'title': 'Skills',
        'skills': skillss}

    return render(request, 'skill/index.html', context)
