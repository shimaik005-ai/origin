from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "name", "age", "class_name")
    search_fields = ("student_id", "name", "class_name")
