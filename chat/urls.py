from django.urls import path

from . import views

urlpatterns = [
    path('<int:chat_id>/', views.index, name='index'),
]