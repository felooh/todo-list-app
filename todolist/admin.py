from django.contrib import admin
from .models import Category,ToDoTask

# Register your models here.
admin.site.register((Category,ToDoTask))