from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .models import Category, ToDoTask
from django.shortcuts import redirect
from .forms import CategoryForm, ToDoTaskForm
from django.utils import timezone
# from datetime import datetime
from django.utils import timezone
from pytz import timezone
import datetime
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
    deadline = task.deadline
    
    context ={
        "task":task,
        "details":details,
        "deadline":deadline
    } 

    return render(request, 'todos/task_details.html', context)

#deleteCategory
def deleteCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # equally you would have accessed the categosries this way
    # category = Category.objects.get(id = category_id)
    category.delete()
    
    return redirect("todolist:index")
    
#deleteTask
def deleteTask(request, task_id):
    task = get_object_or_404(ToDoTask, id=task_id)
    #task = ToDoTask.objects.get(id=task_id)
    category_id = task.category_id
    task.delete()

     
    return redirect("todolist:viewTask", category_id)
 
# category details(number of tasks)
def numberOfTasks(request, category_id):
    category = Category.objects.get(id= category_id)
    task_count = ToDoTask.objects.filter(category=category)
    
    context = {
        "category":category,
        "task_count":task_count
    }
    print()
    return render(request, "todos/index.html", context)


def markAsDone(request, task_id):
    task = ToDoTask.objects.get(id = task_id)
    category_id = task.category_id
    task.is_complete = True
    task.save()
    
    return redirect("todolist:viewTask", category_id=category_id)


def taskIsOverdue(request, task_id):
    task = ToDoTask.objects.get(id = task_id)
    category_id = task.category_id
    remaining_time = task.deadline
    
   
    context= {
    
        "task":task,
        "category_id":category_id,
        "remaining_time":remaining_time
       
    }
   
    return render(request, "todos/task_list.html", context)

