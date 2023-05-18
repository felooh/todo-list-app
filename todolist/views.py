from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Category, ToDoTask
from django.shortcuts import redirect
from .forms import CategoryForm, ToDoTaskForm
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
# Create your views here.

#index
def startPage(request):
    
    categories = Category.objects.all()
    
    category_list=[]
    for i in categories:
        category_list.append(i)
        
    context = {"categories":category_list}
    
    return render(request, 'todos/index.html', context)



# createCategory
def createCategory(request):
    category_form = CategoryForm(request.POST)
    
    if category_form.is_valid():
        category_form.save()
        return redirect("http://127.0.0.1:8000")
                   
    context= {'form':category_form}
    return render(request, 'todos/category_form.html', context)


#createTask
def createTask(request, category_id):
    category = Category.objects.filter(id=category_id).first()
    task_form = ToDoTaskForm(request.POST)
    
    if task_form.is_valid():
         task = task_form.save(commit=False)
         task.category = category
         task.save()
        #  return redirect('http://127.0.0.1:8000/viewTask') 
         return redirect("todolist:viewTask", category_id=category_id)
    else:
        task_form = ToDoTaskForm()
        
    context = {
        'form': task_form, 
        "category": category
        }
    return render(request, 'todos/task_form.html', context)


#viewCategory
def viewCategory(request):
    categories = Category.objects.all()
    
    category_list=[]
    for i in categories:
        category_list.append(i)
        
    context = {"categories":category_list}
    
    return render(request, 'todos/index.html', context)
    
    
#viewTasks

def viewTask(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tasks = ToDoTask.objects.filter(category=category)
    
    context = {
        "tasks":tasks, 
        "category":category
    }
    return render(request, 'todos/task_list.html', context)


#view task details

def viewTaskDetails(request, task_id):
    task = get_object_or_404(ToDoTask, pk=task_id)
    details = task.description
    
    context ={
        "task":task,
        "details":details,
    }
    print(context) 

    return render(request, 'todos/task_details.html', context)

#deleteCategory
def deleteCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    
    return redirect("todolist:index")
    
#deleteTask
def deleteTask(request, task_id):
    task = get_object_or_404(ToDoTask, id=task_id)
    category_id = task.category_id
    task.delete()
     
    return redirect("todolist:viewTask", category_id)
    

