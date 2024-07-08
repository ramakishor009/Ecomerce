from django.urls import path
from . import views
app_name="food"
urlpatterns=[
    #food/
    path("",views.index,name="index"),
    #food/item 
    path("item/",views.item,name="item"),
    #food/1
    path("<int:itemid>/",views.details,name="details"),
    #add Item
    path("add/",views.create_item,name="create_item"),
    #update
    path("update/<int:id>",views.update_item,name="update_item"),
    #delete 
    path("delete/<int:id>",views.Delete_item,name="Delete_item"),
]