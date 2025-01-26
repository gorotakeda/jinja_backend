from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from api.models.worshiper import Worshiper
from api.serializers.worshiper_serializer import WorshiperSerializer


class WorshiperDeleteView(generics.DestroyAPIView):
    """
    参拝者の削除を行うAPI
    """

    serializer_class = WorshiperSerializer
    queryset = Worshiper.objects.all()

    def get_worshiper(self):
        # 参拝者情報を取得できない場合は NotFound を返す
        try:
            return Worshiper.objects.get(pk=self.kwargs["pk"])
        except Worshiper.DoesNotExist:
            raise NotFound("対象の参拝者が存在しません")

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_worshiper()
            instance.delete()
            return Response(
                {"detail": "参拝者を削除しました。"},
                status=status.HTTP_200_OK,
            )
        except NotFound as e:
            # 参拝者が見つからない場合
            return Response(
                {"detail": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
