from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import ForAny, IsAdmin, IsOwner
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action == "list":    # Просмотр - все пользователи
            return [ForAny()]
        elif self.action in ["create", "partial_update"]:  # Cоздание, частичное изменение - аут.пользователи, владельцы
            return [IsAuthenticated(), IsOwner()]
        elif self.action in ["update", "destroy"]:   # Изменение и удаление только администраторы
            return [IsAdmin()]
        return []


