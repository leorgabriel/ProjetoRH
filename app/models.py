from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)
    ultimo_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Usuário: {self.nome} - Email: {self.email}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    data_admissao = models.DateField()
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Funcionário: {self.nome} - CPF: {self.cpf} - Email: {self.email}'

class Cargo(models.Model):
    nome_cargo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f'Cargo: {self.nome_cargo} - Descrição: {self.descricao}'

class Funcionario_Cargo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Cargo: {self.cargo.nome_cargo} - Início: {self.data_inicio} - Fim: {self.data_fim}'

class Salario(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vigencia = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Salário: R$ {self.valor} - Cargo: {self.cargo.nome_cargo} - Vigência: {self.data_vigencia}'


class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=100)
    descricao = models.TextField()
    gerente = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True, related_name='gerente_departamento')

    def __str__(self):
        return f'Departamento: {self.nome_departamento} - Gerente: {self.gerente.nome if self.gerente else "N/A"}'


class Funcionario_Departamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Departamento: {self.departamento.nome_departamento} - Início: {self.data_inicio} - Fim: {self.data_fim}'


class Historico_Salario(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Salário: R$ {self.salario.valor} - Início: {self.data_inicio} - Fim: {self.data_fim}'


class Projeto(models.Model):
    nome_projeto = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f'Projeto: {self.nome_projeto} - Departamento: {self.departamento.nome_departamento} - Início: {self.data_inicio} - Fim: {self.data_fim}'


class Funcionario_Projeto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Projeto: {self.projeto.nome_projeto} - Início: {self.data_inicio} - Fim: {self.data_fim}'


class Beneficio(models.Model):
    nome_beneficio = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f'Benefício: {self.nome_beneficio} - Descrição: {self.descricao}'


class Funcionario_Beneficio(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    beneficio = models.ForeignKey(Beneficio, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Benefício: {self.beneficio.nome_beneficio} - Início: {self.data_inicio} - Fim: {self.data_fim}'


class Certificado(models.Model):
    nome_certificado = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    data_obtencao = models.DateField()
    validade = models.DateField(null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Certificado: {self.nome_certificado} - Funcionário: {self.funcionario.nome} - Instituição: {self.instituicao}'


class Contato_Emergencia(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    relacao = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f'Contato de Emergência: {self.nome} - Funcionário: {self.funcionario.nome} - Relação: {self.relacao} - Telefone: {self.telefone}'


class Historico_Cargo(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Funcionário: {self.funcionario.nome} - Cargo: {self.cargo.nome_cargo} - Início: {self.data_inicio} - Fim: {self.data_fim}'

