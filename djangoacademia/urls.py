from django.contrib import admin
from django.urls import path, include
from pagina import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('course/',views.course,name='course'),
    path('faq/',views.faq,name='faq'),
    path('liderazgo/',views.liderazgo,name='liderazgo'),
    path('mentor/<int:mentor_id>/', views.detalle_mentor, name='detalle_mentor'),
    path('marketing/',views.marketing,name='marketing'),
    path('loging/', auth_views.LoginView.as_view(template_name='loging.html'), name='loging'),
    path('logout/', auth_views.LogoutView.as_view(template_name='loging.html'), name='logout'),
    path('terminos/',views.terminos,name='terminos'),
    path('privacidad/',views.privacidad,name='privacidad'),
    path('registro/',views.registro,name='registro'),
    path('compra/',views.compra,name='compra'),
    path('curso/<int:course_id>/', views.course_details_view, name='course_details'),
    path('accounts/profile/', views.index, name='index'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
