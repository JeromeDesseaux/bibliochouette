from rest_framework import serializers

from libraries.models import Reader
from users.models import User
from holders.models import HolderGroup, Holder


class HolderGroupSerializer(serializers.ModelSerializer):
    holder = serializers.PrimaryKeyRelatedField(
        queryset=Holder.objects.all(), required=False
    )
    admin = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    readers = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Reader.objects.all(), required=False
    )

    class Meta:
        model = HolderGroup
        fields = ["id", "label", "readers", "holder", "admin"]


class HolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holder
        fields = ["id", "type", "name"]
