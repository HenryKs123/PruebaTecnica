from django.urls import path
from Registro.Empleados.views import EmpleadosListViem, eliminarEmpleado, crearEmpleado, editarEmpleado, Almacenador

urlpatterns = [
    path('', EmpleadosListViem.as_view(), name='gestion_curso'),
    path('EliminarEmpleado/<int:id>', eliminarEmpleado ),
    path('crearEmpleado/', crearEmpleado),
    path('EditarEmpleado/', editarEmpleado),
    path('Almacenador/<int:id>',Almacenador),
]
