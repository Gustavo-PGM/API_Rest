from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.pegar_usuario, name='pegar_usuario'),
    path('apelido/<str:apelido>', views.pegar_apelido,name='apelido'),
    path('apelido_cripto/', views.gerenciar_usuario ,name='apelido_cripto')
]