from django.contrib import admin
from .model.models import StudentsData, TeachersData

@admin.register(StudentsData)
class StudentsDataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "yearstudent", "dni", "family", "phone")
    search_fields = ("name", "dni", "family")
    list_filter = ("yearstudent",)


@admin.register(TeachersData)
class TeachersDataAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "dni", "yearstudentasign", "phone")
    search_fields = ("name", "dni")
    list_filter = ("yearstudentasign",)
