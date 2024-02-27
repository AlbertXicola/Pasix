from django.urls import path
from .views import home, contacto, galeria, registro, olvidada, terminos, user_view, pycore_view, perfil, cierre, archivos
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"), 
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('olvidada/', olvidada, name='olvidada'),
    path('terminos/', terminos, name='terminos'),
    path('user/', user_view, name='user'),
    path('flask/', TemplateView.as_view(template_name='index_flask.html'), name='flask_upload'),
    path('pycore/', pycore_view, name='pycore'),
    path('perfil/', perfil, name='perfil'),
    path('cerrar-sesion/', cierre, name='cierre'),
    path('archivos/', archivos, name='archivos'),

]