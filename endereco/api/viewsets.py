from rest_framework.viewsets import ModelViewSet
from endereco.models import Endereco
from .serializes import EnderecoSerializer


class EnderecosViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
