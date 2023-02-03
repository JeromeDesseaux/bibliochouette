from rest_framework import viewsets
from rest_framework import permissions

from holders.models import Holder, HolderGroup
from holders.serializers import HolderSerializer, HolderGroupSerializer


# Create your views here.
class HolderViewSet(viewsets.ModelViewSet):
    queryset = Holder.objects.all().order_by("-created_at")
    serializer_class = HolderSerializer
    permission_classes = [permissions.IsAuthenticated]


class HolderGroupViewSet(viewsets.ModelViewSet):
    queryset = HolderGroup.objects.all().order_by("-created_at")
    serializer_class = HolderGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
