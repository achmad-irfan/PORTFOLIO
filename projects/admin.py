from django.contrib import admin

# Register your models here.
from .models import Proyek, background, purpose, dataset, result, insight, recommendation, dataPrep


class ProyekAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]


admin.site.register(Proyek, ProyekAdmin)
admin.site.register(background)
admin.site.register(purpose)
admin.site.register(dataset)
admin.site.register(result)
admin.site.register(insight)
admin.site.register(recommendation)
admin.site.register(dataPrep)
