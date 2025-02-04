from django.contrib import admin
from . import models


class RegisterAdminApp(admin.ModelAdmin):
    ...
    
admin.site.register(models.Author, RegisterAdminApp)
admin.site.register(models.Job, RegisterAdminApp)
admin.site.register(models.ModelFood, RegisterAdminApp)
admin.site.register(models.Category, RegisterAdminApp)
admin.site.register(models.SubCategory, RegisterAdminApp)