from django.urls import path
from .views import home, contacto, galeria, registro, olvidada, terminos, user_view, pycore_view, perfil, auth_logout
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
    path('logout/', auth_logout, name='auth_logout'),  # Ruta para logout

]