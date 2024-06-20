from typing import Any, Dict
from django.shortcuts import render
from .models import offer
from django.views.generic.base import TemplateView
# Create your views here.


class indexView(TemplateView):
    template_name = 'services/index.html'

    def get_context_data(self):
        offers = offer.objects.all()
        context = {
            'title': 'Services',
            'offers': offers}

        return context

# def index(request):
#     offers = offer.objects.all()
#     context = {
#         'title': 'Services',
#         'offers': offers
#     }
#     return render(request, 'services/index.html', context)
