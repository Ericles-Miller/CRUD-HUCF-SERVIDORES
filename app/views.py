from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Servidor
from .forms import ServidorForm, ValidForm
from django.core.paginator import Paginator
#from django.contrib import messages
# Create your views here.
def inicio(request):
    return render(request, 'index.html')   

def cadastrar(request):
       
    if request.method == 'GET':
        user = Servidor.objects.all()

        form = ValidForm()
        #form2= CandidatosForm()
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'cadastro.html', context=context)
    
    else:
        form2 = ServidorForm(request.POST or None, request.FILES)
        form = ValidForm(request.POST or None, request.FILES)

        if form.is_valid():    
            form = ValidForm() # funcao para validar cpf
            form2.save()
            #messages.success(request, 'Dados Cadastrados com Sucesso!!')
            return redirect('show_message')
        else: 
            user = Servidor.objects.all()
            context = {
                'form': form,
                'user': user,   
            }
            return render(request, 'cadastro.html', context = context)


def show_message(request):
    return render(request,'show_message.html' )


def listar(request):
    server = Servidor.objects.all()
    search = request.GET.get('search')
    print('---------')
    print(search)
    if search:
        server = objects.filter(cpf_icontains=search)
        rename_image(search)
        context = {'server': server}
        return render(request, 'lista.html', context)
    context ={
        'server': server
    }
    return render(request, 'lista.html', context)

