from django.contrib import admin
from lottery.apps.website.models import Num3D


class Num3DAdmin(admin.ModelAdmin):
    list_display = ('turn', 'num1', 'num2', 'num3')

admin.site.register(Num3D, Num3DAdmin)
