from .models import Proyek, background,  datasets, result, insight, purpose, praprocess, recommendation, dataPrep, conclution, improvment, evaluation, training, arsitektur
from django.contrib import admin


class ProyekAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]


admin.site.register(Proyek, ProyekAdmin)
admin.site.register(result)
admin.site.register(insight)
admin.site.register(recommendation)
admin.site.register(dataPrep)
admin.site.register(datasets)
admin.site.register(purpose)
admin.site.register(conclution)
admin.site.register(improvment)
admin.site.register(evaluation)
admin.site.register(training)
admin.site.register(arsitektur)
admin.site.register(praprocess)
