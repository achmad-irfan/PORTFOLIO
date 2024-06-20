from django.contrib import admin

# Register your models here.
from .models import school, certification, workExp, projectExp

admin.site.register(school)
admin.site.register(certification)
admin.site.register(workExp)
admin.site.register(projectExp)
