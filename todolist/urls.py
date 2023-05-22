from django.urls import path

from . import views

app_name = "todolist"
urlpatterns = [
    
    path("", views.startPage, name="index"),
    path("createCategory/", views.createCategory, name="createCategory"),
    path("createTask/<int:category_id>", views.createTask, name="createTask"),
    path("viewCategory/<int:category_id>", views.viewCategory, name="viewCategory" ),
    path("viewTask/<int:category_id>", views.viewTask, name="viewTask"),
    path("viewTaskDetails/<str:task_id>", views.viewTaskDetails, name="viewTaskDetails"),
    path("deleteTask/<int:task_id>", views.deleteTask, name="deleteTask"),
    path("deleteCategory/<int:category_id>", views.deleteCategory, name="deleteCategory"),
    path('numberOfTasks/<int:category_id>/', views.numberOfTasks, name='numberOfTasks'),
    path('markAsDone/<int:task_id>', views.markAsDone, name="markAsDone"),
    path('taskIsOverdue/<int:task_id>', views.taskIsOverdue, name="taskIsOverdue"),
    path("editTask/<int:task_id>", views.editTask, name="editTask"),
]