from django.shortcuts import render
from .models import Contacto
from .models import Nuevo
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from perritos.serializers import UserSerializer, GroupSerializer

def index(request):
    return render(request,'perritos/index.html')

def contacto(request):
    if request.method == 'POST':
        email_m = request.POST.get('txtcorreo')
        rut_m = request.POST.get('txtrut')
        nombre_m = request.POST.get('txtnombre')
        fecha_nac_m = request.POST.get('txtfecha')
        telefono_m = request.POST.get('txttelefono')
        region_m = request.POST.get('cmbregion')
        ciudad_m = request.POST.get('cmbciudad')
        tipo_vivienda_m = request.POST.get('cmbvivienda')
        
        c = Contacto(email=email_m,rut=rut_m,nombre=nombre_m,fecha_nac=fecha_nac_m,telefono=telefono_m,region=region_m,ciudad=ciudad_m,tipo_vivienda=tipo_vivienda_m)
        c.save()
        return render(request,'perritos/answercontacto.html')
    else:
        return render(request,'perritos/Contactanos.html')

def nuevo(request):
    if request.method =='POST':
        nom_new_n = request.POST.get('nom_new')
        raza_n = request.POST.get('raza_new')
        descripcion_n = request.POST.get('desc_new')
        foto_n = request.FILES.get('foto_new')
        estado_n = request.POST.get('cmdestado')
        m = Nuevo(nom=nom_new_n,raza=raza_n,descripcion=descripcion_n,foto=foto_n,estado=estado_n)
        m.save()
        return render(request,'perritos/answernuevo.html')
    else:
        return render(request,'perritos/nuevo.html')

def quienes(request):
    return render(request,'perritos/quienes.html')

def mostrar(request):
	nuevito = Nuevo.objects.all()
	contexto = {'nuevo':nuevito}
	return render(request, 'perritos/mostrar.html',contexto)

def mostrarcontacto(request):
    conti = Contacto.objects.all()
    contexto2 = {'conta': conti}
    return render(request,'perritos/mostrarcontacto.html',contexto2)




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Create your views here.
