from django.shortcuts import render
from .models import school, certification, workExp, projectExp


def index(request):
    schools = school.objects.all().order_by('-finish')
    certifications = certification.objects.all().order_by('-finish')
    workexp = workExp.objects.all().order_by('-finish')
    projectexp = projectExp.objects.all().order_by('-finish')

    context = {
        'title': 'Education and Certification',
        'school': schools,
        'certificate': certifications,
        'workexp': workexp,
        'projectexp': projectexp
    }
    return render(request, 'education/index.html', context)
