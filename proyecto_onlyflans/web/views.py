from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan , ContactForm
from .contactDataForm import ContactDataForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.

#fuincion auxiliar para verificar si es admin(is_staf o is_superuser) 
def es_admin(user):
   return user.is_authenticated and user.is_superuser

def es_staff_o_admin(user):
   return user.is_authenticated and (user.is_staff or user.is_superuser)


def inicio(request): 
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes':flanes_publicos})

@login_required(login_url='login')
def bienvenido(request):  
    flanes_privados = Flan.objects.filter(is_private=True)  
    return render(request, 'welcome.html', {'flanes':flanes_privados})

def acerca(request):    
    return render(request, 'about.html', {})


def contacto(request):
    
    if request.method == 'POST':
        
        form = ContactDataForm(request.POST)
        
        if form.is_valid():
            
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            
            return HttpResponseRedirect('/exito')
        
    else:
        form = ContactDataForm()
        
    return  render(request, 'contacto.html' ,{'form':form})
    


def exito(request):    
    return render(request, 'exito.html', {})

def lista_contactos(request): 
    contactos = ContactForm.objects.all()
    return render(request, 'lista_contactos.html', {'contactos':contactos})
