from libraries.models import Reader
from users.models import User
from .models import HolderGroup, Holder
from rest_framework import serializers


class HolderGroupSerializer(serializers.ModelSerializer):
    holder = serializers.PrimaryKeyRelatedField(queryset=Holder.objects.all())
    admin = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    readers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reader.objects.all()
    )

    class Meta:
        model = HolderGroup
        fields = ["id", "label", "readers", "holder", "admin"]


class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = ["id", "type", "name"]
