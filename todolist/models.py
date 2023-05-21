from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    title= models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.title
    
    
class ToDoTask(models.Model):
    task = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, null= True, blank =True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_complete= models.BooleanField(default=False)
    is_overdue = models.BooleanField(default=False)
    deadline = models.DateTimeField(blank=True)
    deadline_date = models.DateField()
    deadline_time = models.TimeField()
    category = models.ForeignKey(Category, editable=False, on_delete=models.CASCADE)                                    
    
    
    def __str__(self):    
        # formatted_date = self.created_date.strftime(f"Date:%Y-%m-%d    Time:%H:%M:%S")
        return self.task
    
    def get_remaining_time(self):
        now = timezone.now()
        deadline_datetime = datetime.combine(self.deadline_date, self.deadline_time)
        remaining_time = deadline_datetime - now

        return remaining_time

    
    def save(self, *args, **kwargs):
        deadline_datetime = datetime.combine(self.deadline_date, self.deadline_time)
        self.deadline = deadline_datetime
        super(ToDoTask, self).save(*args, **kwargs)  
    class Meta:
        ordering = ["created_date"]
    
    
    
    
    
    
    
    
    
    