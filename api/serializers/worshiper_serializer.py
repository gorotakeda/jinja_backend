from rest_framework import serializers

from api.models.worshiper import Worshiper


class WorshiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worshiper
        fields = "__all__"
