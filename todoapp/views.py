from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Todo

def add_todo(request):
    if request.method=="POST":
        Title=request.POST['title']
        Date=request.POST['date']
        Priority=request.POST['priority']
        add=Todo(Title=Title,Date=Date,Priority=Priority)
        add.save()
        return redirect('view_todo')

def index(request):
    return render(request,"index.html")

def view_todo(request):
    data=Todo.objects.all()
    return render(request,"result.html",{'data':data})    

def delete_todo(request,id):
    add=Todo.objects.get(id=id)
    add.delete()
    return redirect('view_todo')

def edit(request,id):
    Data=Todo.objects.get(id=id)
    return render(request,'edit.html',{'Data':Data})

def edit_todo(request,id):
    if request.method=="POST":
        add=Todo.objects.get(id=id)
        add.Title=request.POST["title"]
        add.Date=request.POST["date"]
        add.Priority=request.POST["priority"]
        add.save()
        return redirect("view_todo")

def search(request):
    query=request.GET["query1"]
    Data=Todo.objects.filter(Priority__icontains=query)
    return render(request,'search.html',{'Data':Data})