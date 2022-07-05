from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user = request.user
            user2 = User.objects.get(username=user.username)
            return Response({
                'result': "success",
                'id': user2.id,
                'username': user2.username,
            })
        except:
            return Response({
                'result': "输入参数错误",
            })
