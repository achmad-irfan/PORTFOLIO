from django.shortcuts import render
# from .forms import ProjectForm
from django.views import View


def index(request):
    # projectForm = ProjectForm()
    context = {
        'title': 'Achmad Irfan Afandi',
        'tile': 'Home',
        'subtitle': 'Data Analyst - Data Scientist - Python Developer',
        # 'projectForm': projectForm
    }

    return render(request, 'index.html', context)
