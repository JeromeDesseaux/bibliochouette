from libraries.models import Reader
from .models import HolderGroup, Holder
from rest_framework import serializers


class HolderGroupSerializer(serializers.ModelSerializer):
    holder = serializers.PrimaryKeyRelatedField(queryset=Holder.objects.all())
    readers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reader.objects.all()
    )

    class Meta:
        model = HolderGroup
        fields = ["id", "label", "readers", "holder"]


class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = ["id", "type", "name"]
