from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Proyek


class detailProjectView(DetailView):
    model = Proyek
    extra_context = {
        'title': 'Detail Projects',
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class indexView(ListView):
    model = Proyek
    ordering = ['-tanggal']
    paginate_by = 5
    extra_context = {

        'title': 'Projects',
        'item': ['SQL', 'Power BI', 'Tableau', 'Python Dash', 'Python Django']}

    def get_queryset(self):
        category = self.kwargs.get('category')
        if category and category != "ALL":
            return Proyek.objects.filter(category=category)
        return Proyek.objects.all()

    def get_context_data(self, *args, **kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


# def index(request):
#     ss = Proyek.objects.all()
#     projec = ss.order_by("-tanggal")
#     context = {
#         'title': 'Projects',
#         'project': projec,
#         'item': ['SQL', 'Power BI', 'Tableau', 'Pyhton Dash', 'Python Django']}

#     return render(request, 'projects/index.html', context)


# def detail_gambar(request, proyek_slug):
#     proyek = get_object_or_404(Proyek, slug=proyek_slug)
#     context = {
#         'title': 'Detail Projects',
#         'proyek': proyek,
#     }

#     return render(request, 'projects/detailProjects.html', context)


def report_project(request, proyek_slug):
    proyek = get_object_or_404(Proyek, slug=proyek_slug)
    context = {
        'title': 'Report Projects',
        'proyek': proyek,
        'orderhead': ['background', 'purpose', 'dataset', 'data preparation', 'result', 'insight and recomendation'],
    }

    return render(request, 'projects/reportProject.html', context)
