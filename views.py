from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import store
from django.utils import timezone


# Create your views here.
def hr(request):

    if request.method == "POST":
        task = request.POST.get('task_name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        todo = store(task_name=task, priority=priority, date=date)
        todo.save()
        return redirect("/")
    all_todo = store.objects.filter(status = False)
    completed_todo = store.objects.filter(status = True).order_by('date')
    context = {
        "all_todo": all_todo,
        "completed_todo" :  completed_todo,
    }


    return render(request, "home.html",context=context)


def de(request,id):
    if request.method == "POST":
        del_todo =get_object_or_404(store, id =id)
        del_todo.delete()
        return redirect("/")


    return render(request,"delete.html")


def up(request,id):


    return render(request,"update.html")

def ch(request,id):
    todo = get_object_or_404(store, id=id)
    if request.method == "POST":
        task = request.POST.get('task_name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        todo.task_name = task
        todo.priority = priority
        todo.date = date
        todo.save()
        return redirect("/")
    return render(request,"change.html",context={"todo":todo})






def mark_as_done(req , id):
    task =get_object_or_404(store, id=id)
    task.status = True
    task.date = timezone.now().date()
    task.save()
    return redirect("/")
