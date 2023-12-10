"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from aplicacion import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registrousuarios/', views.registro, name='registroUsuarios'),
    path('informes/', views.informes, name='informes'),
    path('iniciarjornada/', views.iniciarJornada, name='iniciarJornada'),
    path('createcargacamioneta/',views.cargaCamioneta,name='cargacamioneta'),
    path('cargacamioneta/', views.listaCargaCamioneta, name='cargaCamioneta'),
    path('editarCargaCamioneta/<int:id>', views.editarCargaCamioneta, name='editarCargaCamioneta'),
    path('eliminarCargaCamioneta/<int:id>', views.eliminarCargaCamioneta, name='eliminarCargaCamioneta'),
    path('createcargabomba/', views.cargaBomba, name='cargabomba'),
    path('cargabomba/', views.listarCargaBomba, name='cargaBomba'),
    path('editarCargaBomba/<int:id>', views.editarCargaBomba, name='editarCargaBomba'),
    path('eliminarCargaBomba/<int:id>', views.eliminarCargaBomba, name='eliminarCargaBomba'),

]
