# Generated by Django 5.1 on 2024-08-20 23:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_beneficio', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_admissao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('ultimo_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_departamento', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('gerente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gerente_departamento', to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Contato_Emergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('relacao', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=20)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_certificado', models.CharField(max_length=100)),
                ('instituicao', models.CharField(max_length=100)),
                ('data_obtencao', models.DateField()),
                ('validade', models.DateField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario_Beneficio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('beneficio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.beneficio')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario_Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario_Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departamento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario_Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.projeto')),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_vigencia', models.DateField()),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.funcionario')),
                ('salario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.salario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]
