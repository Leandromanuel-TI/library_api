from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Equipamento, Tecnico, Reparacao
from .serializers import ClienteSerializer, EquipamentoSerializer, TecnicoSerializer, ReparacaoSerializer
from rest_framework import viewsets, permissions
from .models import Cliente, Equipamento, Tecnico, Reparacao
from .serializers import ClienteSerializer, EquipamentoSerializer, TecnicoSerializer, ReparacaoSerializer
from rest_framework import viewsets
from .models import Cliente, Tecnico, Equipamento, Reparacao
from .serializers import ClienteSerializer, TecnicoSerializer, EquipamentoSerializer, ReparacaoSerializer
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    permission_classes = [IsAuthenticated]

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    permission_classes = [IsAuthenticated]

class ReparacaoViewSet(viewsets.ModelViewSet):
    queryset = Reparacao.objects.all()
    serializer_class = ReparacaoSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReparacaoViewSet(viewsets.ModelViewSet):
    queryset = Reparacao.objects.all()
    serializer_class = ReparacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EquipamentoViewSet(viewsets.ModelViewSet):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class ReparacaoViewSet(viewsets.ModelViewSet):
    queryset = Reparacao.objects.all()
    serializer_class = ReparacaoSerializer


# Create your views here.
