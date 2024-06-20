from django.shortcuts import render
from .models import skills
# Create your views here.


def index(request):
    skill = skills.objects.all()
    context = {
        'title': 'Skills',
        'skills': skill}

    return render(request, 'skill/index.html', context)
