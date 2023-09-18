from django.shortcuts import render
#sirve para crear un formulario
from django.contrib.auth.forms import UserCreationForm
#sirve para almacenar datos
from django.contrib.auth.models import User
#enviar un texto
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html',{
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registrar usuario
            try:
                user=User.objects.create_user(username=request.POST['username'],
                                          password=request.POST['password1'])
                user.save()
                return HttpResponse('user creted successfuly')
            except:
                return HttpResponse('el usuario ya existe')
        return HttpResponse('password do not much')

