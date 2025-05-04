from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all().order_by('id')
    serializer_class = VeiculoSerializer