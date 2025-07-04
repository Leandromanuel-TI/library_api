# Generated by Django 5.2.3 on 2025-06-12 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('PC', 'Computador'), ('TV', 'Televisão'), ('OUTRO', 'Outro')], max_length=10)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('problema_descrito', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reparacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDENTE', 'Pendente'), ('EM_ANDAMENTO', 'Em andamento'), ('CONCLUIDA', 'Concluída')], default='PENDENTE', max_length=20)),
                ('descricao_servico', models.TextField()),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.equipamento')),
                ('tecnico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tecnico')),
            ],
        ),
    ]
