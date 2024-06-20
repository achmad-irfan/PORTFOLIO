from typing import Any, Dict
from django.shortcuts import render
from .models import summaries
from django.views.generic.base import TemplateView
# Create your views here.


class indexView(TemplateView):
    template_name = 'about/index.html'

    def get_context_data(self):
        isiAbout = summaries.objects.all()
        context = {
            'title': 'About',
            'summary': isiAbout}

        return context


# def index(request):
#     isiAbout = summaries.objects.all()

#     context = {
#         'title': 'About',
#         'summary': isiAbout,
#         'menu':
#             {'about': 'bi bi-file-earmark-person',
#              'education': 'bx bxs-graduation',
#              'skill': 'bx bx-wrench',
#              'projects': 'bx bx-building',
#              'services': 'bx bx-support',
#              'contact': 'bx bxs-contact'},

#     }
#     return render(request, 'about/index.html', context)
