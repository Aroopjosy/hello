from django.contrib import admin

# Register your models here.
from myapp import models
admin.site.register(models.Blog)
