from django import forms

from .models import Category, ToDoTask

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        
class ToDoTaskForm(forms.ModelForm):
    class Meta:
        model = ToDoTask
        fields = "__all__"