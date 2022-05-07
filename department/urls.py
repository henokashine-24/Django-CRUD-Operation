
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employe_home , name="employee-home"),
    path('create/', views.create , name="create"),
    path('update/<str:id>/', views.update , name="update"),
    path('delete/<str:id>/', views.delete, name="delete")
]