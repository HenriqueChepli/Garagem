from rest_framework.viewsets import ModelViewSet

from core.models import Cor
from core.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all().order_by('id')
    serializer_class = CorSerializer