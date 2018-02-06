from django.forms import Form, ModelForm, TextInput, CharField
from .models import Usuario

class FormLogin(Form):

    login = CharField(label="Login", max_length = 20, widget=TextInput(attrs={"class":"form-control"}))
    senha   = CharField(label="Senha", max_length = 20, widget=TextInput(attrs={"class":"form-control"}))


class FormCadastroUsuario(ModelForm):


    class Meta:
        model = Usuario
        #fields = ['nome', 'sobrenome', 'cidade', 'login', 'senha', 'logradouro', 'email']
        exclude = ['ativo']
