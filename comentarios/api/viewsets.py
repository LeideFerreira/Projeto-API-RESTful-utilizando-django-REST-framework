from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from .serializes import ComentarioSerializer


class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
