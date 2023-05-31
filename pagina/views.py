from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Tema
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

# @login_required
def course(request):
    cursos = Curso.objects.all()
    data = {
        'cursos' : cursos
    }

    return render(request, "course.html",data)

def course_details_view(request, course_id):
    course = get_object_or_404(Curso, id=course_id)
    # Obtén información adicional o modelos relacionados para el curso
    # Por ejemplo: course_extra_info = course.extrainfo_set.all()
    context = {
        'course': course,
        # Pasa información adicional al contexto del template si es necesario
        # 'extra_info': course_extra_info,
    }
    return render(request, 'course_details.html', context)

# def viewCurso(request, nombre, aprenderas,descripcionDentro,aprenderas2,aprenderas3):    
    return render(request, "viewCurso.html",{
        
        # "nombre": nombre,
        # # "video": video,
        # "aprenderas" : aprenderas,
        # "aprenderas2" : aprenderas2,
        # "aprenderas3" : aprenderas3,
        # "descripcionDentro" : descripcionDentro,
        
        
 
    })

def liderazgo(request):
    return render(request, "liderazgo.html")

def marketing(request):
    return render(request, "marketing.html")

def loging(request):
    if request.method == 'GET':
        return render(request, 'loging.html', {
            'form': AuthenticationForm
        })
    else:

        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])

        if user is None:
            return render(request, 'loging.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
             })
        else :
            login(request,user)
            return redirect('index')

def terminos(request):
    return render(request, "terminos.html")

def privacidad(request):
    return render(request, "privacidad.html")

def registro(request):
    
    if request.method == 'GET':
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except :
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'registro.html', {
            'form': UserCreationForm,
        
            'error': 'La contraseña no coincide'
        })

def compra(request):
    return render(request, "compra.html")

def index(request):
    return render(request, "index.html")