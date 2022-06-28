from django.urls import path

from . import views

urlpatterns = [
    path("page1/", views.index, name="index"), #test
    path("", views.home,name="home"), #test
    path("page1/<str:name>", views.show,name="show"), # show specific list
    path("create/", views.create, name="create"), # create list form
    path("lists/", views.lists, name="lists") # show all lists
]