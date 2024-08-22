from django.contrib import admin
from app.models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Funcionario)
admin.site.register(Cargo)
admin.site.register(Funcionario_Cargo)
admin.site.register(Salario)
admin.site.register(Departamento)
admin.site.register(Funcionario_Departamento)
admin.site.register(Historico_Salario)
admin.site.register(Projeto)
admin.site.register(Funcionario_Projeto)
admin.site.register(Beneficio)
admin.site.register(Funcionario_Beneficio)
admin.site.register(Certificado)
admin.site.register(Contato_Emergencia)
admin.site.register(Historico_Cargo)