from .models import Proyek
from django.views.generic import ListView
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView


class detailProjectView(DetailView):
    model = Proyek
    template_name = 'projects/reports.html'
    extra_context = {
        'title': 'Detail Projects',
        'classes': ['purpose', 'datasets', 'praprocess', 'arsitektur', 'training', 'evaluation', 'conclution', 'improvment']
    }

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


# class indexView(ListView):
#     model = Proyek
#     ordering = ['-tanggal']
#     paginate_by = 5
#     extra_context = {

#         'title': 'Projects',
#         'item': ['SQL', 'Power BI', 'Tableau', 'Dash', 'Django', 'Data Science', 'Classification']}

#     def get_queryset(self):
#         category = self.kwargs.get('category')
#         if category and category != "ALL":
#             return Proyek.objects.filter(category=category)
#         return Proyek.objects.all()

#     def get_context_data(self, *args, **kwargs):
#         self.kwargs.update(self.extra_context)
#         kwargs = self.kwargs
#         return super().get_context_data(*args, **kwargs)


class indexView(ListView):
    model = Proyek
    ordering = ['-tanggal']
    paginate_by = 5
    template_name = 'projects/index.html'

    # Menambahkan extra_context langsung di dalam get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projects'
        context['item'] = ['SQL', 'Power BI', 'Tableau',
                           'Dash', 'Django', 'Data Science', 'Classification']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()  # Mendapatkan queryset dasar dari ListView
        category = self.kwargs.get('category')

        if category and category != "ALL":
            queryset = queryset.filter(category=category)

        return queryset


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
