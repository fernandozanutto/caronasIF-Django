from django.db.models import *


class Usuario(Model):

    choices = (
        ('', 'Selecione'),
        ('A', 'Aluno'),
        ('S', 'Servidor')
    )

    nome            = CharField(max_length=150)
    sobrenome       = CharField(max_length=150)
    login           = CharField(max_length=20)
    senha           = CharField(max_length=20)
    vinculo         = CharField(max_length=1 ,choices=choices, verbose_name="Vínculo")
    email           = EmailField()
    cidade          = CharField(max_length=250)
    logradouro      = CharField(max_length=250)
    numEndereco     = PositiveIntegerField(verbose_name="Número de Endereço")
    telefone        = CharField(max_length=14)
    dataCadastro    = DateField(auto_now_add=True, verbose_name="Data de Cadastro")
    ativo           = BooleanField(default=True)

    class Meta:
        verbose_name        = "usuário"
        verbose_name_plural = "usuários"


class Mensagem(Model):

    assunto         = CharField(max_length=100)
    mensagem        = CharField(max_length=500)
    remetente       = ForeignKey('Usuario', null=True, on_delete=SET_NULL, related_name='remetente')
    destinatario    = ForeignKey('Usuario', null=True, on_delete=SET_NULL, related_name='destinatario')
    data            = DateField(auto_now_add=True)
    lida            = BooleanField(default=False)


    class Meta:
        verbose_name_plural = "mensagens"
