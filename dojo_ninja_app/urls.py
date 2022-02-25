from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('new/dojo', views.new_dojo),
    path('new/ninja', views.new_ninja),	 
    path('delete/dojo/<int:id>', views.delete_dojo)
]