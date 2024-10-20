from rest_framework import generics

from api.models.worshiper import Worshiper
from api.serializers.worshiper_serializer import WorshiperSerializer


class WorshiperListView(generics.ListAPIView):
    serializer_class = WorshiperSerializer

    def get_queryset(self):
        return Worshiper.objects.all()
