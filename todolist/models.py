from django.db import models
from datetime import datetime
# Create your models here.


class Category(models.Model):
    title= models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title
    

class ToDoTask(models.Model):
    task = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, null= True, blank =True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, editable=False, on_delete=models.CASCADE)                                    
    
    def __str__(self):
        formatted_date = self.created_date.strftime(f"Date:%Y-%m-%d    Time:%H:%M:%S")
        return f"{self.task} created on {formatted_date}" 
    
   
    class Meta:
        ordering = ["created_date"]
    
    
    
    
    
    
    
    
    
    