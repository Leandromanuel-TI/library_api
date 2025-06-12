from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"status": "API Online 🚀"})

urlpatterns = [
    path('', home),  # Rota raiz
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # ou o nome correto da sua app
]
