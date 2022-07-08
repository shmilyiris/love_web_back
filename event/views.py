from django.shortcuts import render
from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from django.core import serializers
from rest_framework.decorators import api_view

# Create your views here.

class EventView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            events = serializers.serialize("json", Event.objects.all())
            return Response({
                'result': "success",
                'events': events,
            })
        except:
            return Response({
                'result': "获取信息错误",
            })

    def post(self, request):
        try:
            new_event = Event.objects.create(
                label=request.POST.get('label'),
                category=request.POST.get('category'),
                content=request.POST.get('content'),
                info="",
            )
            return Response({
                'result': "success",
            })
        except:
            return Response({
                'result': "发送错误"
            })


class EventEditView(APIView):
    def post(self, pk):
        pass

