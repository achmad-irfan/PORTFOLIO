from django.shortcuts import render
from .models import skills
# Create your views here.


def index(request):
    skillss = skillsss.objects.all()
    context = {
        'title': 'Skills',
        'skills': skillss}

    return render(request, 'skill/index.html', context)
