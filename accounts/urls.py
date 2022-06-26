from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, ServidorCreate

urlpatterns = [
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('cadastrar/', ServidorCreate.as_view(), name='cadastrar'),
    path('cadastro/', PerfilUpdate.as_view(), name='cadastro'),
  
]



