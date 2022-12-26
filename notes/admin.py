from django.contrib import admin
from . import models
# Register your models here.
from .models import Equipment


class EquipmentInstanceInline(admin.TabularInline):
    model = Equipment




class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


# inlines = [NotesInstanceInline]


class ClientAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('marca',)


# class NotesInstanceInline(admin.TabularInline):
#     model = Notes


# @admin.register(Notes)
# class NotessAdmin(admin.ModelAdmin):
#     list_display = ('title')

#     inlines = [NotesInstanceInline]


admin.site.register(models.Equipment, EquipmentAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Notes, NotesAdmin)
