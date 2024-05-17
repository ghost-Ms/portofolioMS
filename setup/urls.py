from django.contrib import admin
from django.urls import path
from home import views
from home.views import abrir_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("reflexoes/", views.reflexoes, name="reflexoes"),
    path('abrir-pdf/<str:nome_arquivo>/', abrir_pdf, name='abrir_pdf'),
    path("contacto/", views.contacto, name="contacto"),
    path('enviar-mensagem/', views.enviar_mensagem, name='enviar_mensagem'),


]
