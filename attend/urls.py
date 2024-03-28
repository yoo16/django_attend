from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='attend-index'),
    path("list", views.list, name='attend-list'),
    path("detail/<int:user_id>/", views.detail, name='attend-detail'),
]