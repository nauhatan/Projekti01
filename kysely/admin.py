from django.contrib import admin

# Register your models here.
from .models import Kysymys, Vaihtoehto

admin.site.register(Kysymys)
admin.site.register(Vaihtoehto)
