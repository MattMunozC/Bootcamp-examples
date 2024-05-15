from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from account.decorators.requestsDecorator import page_in_construction
from .forms import TaskForm
from .models import Task,Status,Tag
from account.models import User
# Create your views here.
@login_required
def new_task(request):
    if request.method=="POST":
        form=TaskForm(user=request.user.username,data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=User.objects.get(username=request.user.username)
            task=Task.objects.create(
                owner=user,
                title=data["title"],
                content=data["description"] if data["description"]!="" else "No Description has been provided",
                expire_date=data["expire_date"],
                status=Status.objects.get(id=data["status"]),
                tag=Tag.objects.get(id=data["tag"])
            )
            task.save()
            return redirect("/home")
    return render(request,"task_new_task.html",context={
        "DocumentName":"Nueva Tarea",
        "form":TaskForm(user=request.user.username),
        "styles":["task_new_task"],
        "action_taken":"Nueva Tarea"
    })

@login_required
def full_task(request,task_name):
    user=User.objects.get(username=request.user.username)
    task=Task.objects.get(title=task_name,owner=user)
    return render(request,"task_full_task.html",context={
        "DocumentName":task_name,
        "task":task,
        "styles":[
            "pages_mainpage"
        ]
    })
@login_required
def delete_task(request,task_name):
    try:
        user=User.objects.get(username=request.user.username)
        task=Task.objects.get(title=task_name,owner=user)
        task.delete()
        return redirect("/home")
    except Task.DoesNotExist:
        return redirect("/home")

@login_required
def edit_task(request,task_name):
    try:
        if request.method=="POST":
            form=TaskForm(user=request.user.username,data=request.POST)
            if form.is_valid():
                data=form.cleaned_data
                user=User.objects.get(username=request.user.username)
                task=Task.objects.get(owner=user,title=task_name)
                
                task.owner=user,
                task.title=data["title"],
                task.content=data["description"] if data["description"]!="" else "No Description has been provided",
                task.expire_date=data["expire_date"],
                task.status=Status.objects.get(id=data["status"]),
                task.tag=Tag.objects.get(id=data["tag"])
                
                task.save()
                return redirect("/home")
    except Task.DoesNotExist:
        return redirect("/home")
    return render(request,"task_new_task.html",context={
        "DocumentName":"Editar Tarea",
        "form":TaskForm(user=request.user.username),
        "styles":["task_new_task"],
        "action_taken":f"editando {task_name}"
    })