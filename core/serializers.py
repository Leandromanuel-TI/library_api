from rest_framework import serializers
from .models import Cliente, Equipamento, Tecnico, Reparacao
from rest_framework import serializers
from .models import Cliente, Tecnico, Equipamento, Reparacao

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'

class ReparacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparacao
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'

class ReparacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparacao
        fields = '__all__'
