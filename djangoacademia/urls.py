from django.contrib import admin
from django.urls import path
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course,name='course'),
    path('faq/',views.faq,name='faq'),
    path('liderazgo/',views.liderazgo,name='liderazgo'),
    path('marketing/',views.marketing,name='marketing'),
    path('loging/',views.loging,name='loging'),
    path('terminos/',views.terminos,name='terminos'),
    path('privacidad/',views.privacidad,name='privacidad'),
    path('registro/',views.registro,name='registro'),
    path('compra/',views.compra,name='compra'),


]