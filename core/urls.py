from django.urls import path
from . import views

urlpatterns = [
    path('exemplo/', views.exemplo_view),
]
