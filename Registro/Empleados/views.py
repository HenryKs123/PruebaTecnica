from urllib import request
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Empleaos

from django.views.generic import ListView 

from django.core.paginator import Paginator


#from django.http import HttpResponse

# Create your views here.

def home(request):
    Lista=Empleaos.objects.all()
    Empleados = Empleaos.objects.all()
    page = request.GET.get('page',1)
    
    try:
        paginator = Paginator(Empleados,10)
        Empleados = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'titulo':"Gestion de Registro",
        'entity': Empleados,
        'paginator':paginator,
        'Lista':Lista
    }
    
    return render(request,"Gestion.html",data)

class EmpleadosListViem(ListView):
    
    paginate_by = 10
    model = Empleaos
    template_name='Gestion.html'
    
    def get_queryset(self):
        Empleados = Empleaos.objects.all().order_by('PrimerNombre')
        #paginator = request.GET.get('page',1)
        try:
            paginator = Paginator(Empleados,1)
            #Empleados = paginator.page(page)
        except:
            raise Http404
        
        return Empleados[:10]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Registros'
        return context   
    
def eliminarEmpleado(request, id):
    empleado = Empleaos.objects.get(id=id)
    empleado.delete()
    return redirect('/')

def crearEmpleado(request):
    nombre = request.POST["PrimerNombre"]
    apellido = request.POST["PrimerApellido"]
    segundoNombre = request.POST["OtroNombre"]
    nombre = Correcion(nombre)
    apellido = Correcion(apellido)
    segundoNombre = Correcion(segundoNombre)
    pais = request.POST["Opcion"]
    CorreoE = CrearCorreo(nombre,apellido,pais)
    Empleado = Empleaos.objects.create(PrimerNombre=nombre, PrimerApellido=apellido, OtrosNombres=segundoNombre, PaisEmpleo = pais, Correo = CorreoE)
    return redirect('/')

def editarEmpleado(request):
    
    id = int(request.POST["Id"])
    nombre = request.POST["APrimerNombre"]
    apellido = request.POST["APrimerApellido"]
    segundoNombre = request.POST["AOtroNombre"]
    nombre = Correcion(nombre)
    apellido = Correcion(apellido)
    segundoNombre = Correcion(segundoNombre)
    pais = request.POST["AOpcion"]
    
    Empleado = Empleaos.objects.get(id=id)
    Empleado.PrimerNombre = nombre
    Empleado.PrimerApellido = apellido
    Empleado.OtrosNombres = segundoNombre
    Empleado.PaisEmpleo = pais
    
    Empleado.Correo=CrearCorreo(nombre,apellido,pais)
    
    Empleado.save()
    
    return redirect('/')
    
def CrearCorreo(nombre, apellido, Pais):
    
    extencion = ".com"
    if Pais == "Colombia" :
        extencion = "@cidenet.com.co"
    else:
        extencion = "@cidenet.com.us"
    Correo  = nombre + "." + apellido + extencion
    
    Correo = Correo.replace("  ","")
    CorreoF = Correo.lower()
    
    CorreoEmpleados = Empleaos.objects.filter(PrimerNombre=nombre, PrimerApellido=apellido)
    if len(CorreoEmpleados) != 0:
        Correo  = nombre + "." + apellido+ str(len(CorreoEmpleados)) + extencion
        Correo  = Correo.lower()
    else:
        Correo = Correo.lower()
    return(Correo)

def Almacenador(request,id):
    Empleado = Empleaos.objects.get(id=id)
    data = {
        'titulo':"Edicion de cursos de Registro",
        'Lista': Empleado }    
    return render(request,"Actualizacion.html",data)


def Correcion(palabra):
    
    palabra = palabra.upper()
    
    palabra = palabra.replace('Á','A')
    palabra = palabra.replace('É','E')
    palabra = palabra.replace('Í','I')
    palabra = palabra.replace('Ó','O')
    palabra = palabra.replace('Ú','U')
    palabra = palabra.replace('Ñ','N')
    
    return palabra


def listing(request):
    empleados_list = Empleaos.objects.all()
    paginator = Paginator(empleados_list, 10)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "list.html", {"page_obj": page_obj})