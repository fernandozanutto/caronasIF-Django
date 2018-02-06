from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *

# Create your views here.


class Login(View):

    def get(self, request, *args, **kwargs):
        template = "login.html"
        form = FormLogin()
        context = {
            'form': form
        }

        return render(request, template, context)

    def post(self, request, *args, **kwargs):

        template = "login.html"
        form = FormLogin(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            login = form.cleaned_data("login")
            senha = form.cleaned_data("senha")

            user = Usuario.objects.get(login=login, senha=senha)

            if user:
                template = "index.html"
                return redirect('Index')

        return render(request, template, context)


class NovaConta(View):

    def get(self, request):

        form = FormCadastroUsuario()
        template = "usuario/cadastro.html"

        context = {
           'form': form
        }

        return render(request, template, context)


    def post(self, request):
        pass


class Index(View):

    def get(self, request):
        return HttpResponse("Olá, aqui vai ficar a página principal")
