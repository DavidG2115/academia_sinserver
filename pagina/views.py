from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Mentore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


# Create your views here.

def index(request):
    latest_course = Curso.objects.latest('id')
    username = request.session.get('username')
    context = {
        'latest_course': latest_course,
        'cursos': Curso.objects.all(),
        'username': username
    }
    return render(request, "index.html", context)
@login_required
def about(request):
    mentores = Mentore.objects.all()
    return render(request, 'about.html', {'mentores': mentores})
@login_required
def contact(request):
    return render(request, "contact.html")
@login_required
def faq(request):
    return render(request, "faq.html")

@login_required
def course(request):
    cursos = Curso.objects.all()
    data = {
        'cursos' : cursos
    }

    return render(request, "course.html",data)
@login_required
def detalle_mentor(request, mentor_id):
    mentor = Mentore.objects.get(id=mentor_id)
    descripcion_amplia = mentor.descripcion_amplia.split('\n')
    context = {
        'mentor': mentor,
        'descripcion_amplia': descripcion_amplia
    }
    return render(request, 'detalle_mentor.html', context)

def course_details_view(request, course_id):
    course = get_object_or_404(Curso, id=course_id)
    dirigido_a_list = course.dirigido_a_1.split('\n')
    modulo_lines = course.modulo.split('\n')  # Dividir el contenido de modulo en líneas

    context = {
        'course': course,
        'dirigido_a_list': dirigido_a_list,
        'modulo_lines': modulo_lines,  # Agregar la lista de líneas de modulo al contexto
        'duracion': course.duracion,  # Agregar el campo duracion al contexto
        'modalidad': course.modalidad,  # Agregar el campo modalidad al contexto
        'fecha_arranque': course.fechaArranque,
    }
    return render(request, 'course_details.html', context)


def liderazgo(request):
    return render(request, "liderazgo.html")

def marketing(request):
    return render(request, "marketing.html")


def profile(request):
    return render(request, 'profile.html')

def loging(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Autenticación exitosa, iniciar sesión
                login(request, user)
                return redirect('index')  
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
    else:
        form = LoginForm()
        
    return render(request, 'loging.html', {'form': form})

def terminos(request):
    return render(request, "terminos.html")

def privacidad(request):
    return render(request, "privacidad.html")

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Autenticar al usuario recién registrado
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                # Autenticación exitosa, iniciar sesión
                login(request, user)
                
                # Realizar las acciones necesarias después de un registro exitoso
                return redirect('index')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registro.html', {'form': form})


def compra(request):
    return render(request, "compra.html")
