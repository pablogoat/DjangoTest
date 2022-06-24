from django.urls import path

from . import views

urlpatterns = [
    path("page1/", views.index, name="index"),
    path("", views.home,name="home"),
    path("page1/<str:name>", views.show,name="show"),
    path("create/", views.create, name="create"),
    path("lists/", views.lists, name="lists")
]