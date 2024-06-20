from django.shortcuts import render
from .models import ListSkill
# Create your views here.


def index(request):
    skillss = ListSkill.objects.all()
    context = {
        'title': 'Skills',
        'skills': skillss}

    return render(request, 'skill/index.html', context)
