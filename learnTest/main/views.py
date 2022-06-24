from itertools import count
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import ListCreator

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def show(response, name):
    ls = ToDoList.objects.get(name=name)

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()


        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete = False)
  
    return render(response, "main/list.html", {"list":ls, "name":ls.name})

def create(response):
    if response.method == "POST":
        form = ListCreator(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

            return HttpResponseRedirect("/page1/%s" %t.name)

    else:
        form = ListCreator()
        return render(response, "main/create.html", {"form":form})

def lists(response):
    if response.method == "POST":
        if response.POST.get("delete"):
            print(response.POST)
            for item in ToDoList.objects.all():
                if response.POST.get("delete") == item.name:
                    t = ToDoList.objects.get(name=item.name)
                    t.delete()
                    return HttpResponseRedirect("/lists", {})
        else:
            print(response.POST)
            return HttpResponseRedirect("/page1/%s" %response.POST.get("goto"))
    else:
        form = ListCreator()
        ls = [item.name for item in ToDoList.objects.all()]
        return render(response, "main/allList.html", {"lists": ls})