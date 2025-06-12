from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    TIPO_CHOICES = [
        ('PC', 'Computador'),
        ('TV', 'Televisão'),
        ('OUTRO', 'Outro')
    ]
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='equipamentos')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    defeito = models.TextField()
    status = models.CharField(max_length=50, default='Pendente')

    def __str__(self):
        return f'{self.tipo} - {self.marca}/{self.modelo}'

class Reparacao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, related_name='reparacoes')
    tecnicos = models.ManyToManyField(Tecnico, related_name='reparacoes')
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Reparação de {self.equipamento} iniciada em {self.data_inicio}'
