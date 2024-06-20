from django.shortcuts import render
from .models import skills
# Create your views here.


def index(request):
    skill = skill.objects.all()
    context = {
        'title': 'Skills',
        'skills': skill}

    return render(request, 'skill/index.html', context)
