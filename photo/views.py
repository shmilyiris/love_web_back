from django.shortcuts import render
from .models import Photo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
# Create your views here.

class PhotoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        photos = Photo.objects.all()
        photos_json = []
        for photo in photos:
            item = {}
            item['id'] = photo.pk
            item['src'] = 'http://101.35.183.71:5288' + photo.img.url
            item['cap'] = photo.cap
            item['info'] = photo.info
            photos_json.append(item)
        photos_json = json.dumps(photos_json)
        return Response({
            'result': "success",
            'photos': photos_json,
        })

    def post(self, request):
        print(request.user)
        try:
            new_photo = Photo.objects.create(
                img=request.FILES['img'],
                cap=request.POST.get('cap'),
                info=request.POST.get('info'),
            )
            return Response({
                'result': "success",
            })
        except:
            return Response({
                'result': "发送错误",
            })

