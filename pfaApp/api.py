from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import BPM, PRESSION, Temp
from .serializer import BPMSerializer, PRESSIONSerializer, TempSerializer

@api_view(['GET', 'POST'])

def Dlist(request):
    all_data = BPM.objects.all()
    data = BPMSerializer(all_data, many=True).data
    return Response({'data': data})


class BPMviews(generics.CreateAPIView):
    queryset = BPM.objects.all()
    serializer_class = BPMSerializer


def Plist(request):
    all_data = PRESSION.objects.all()
    data = PRESSIONSerializer(all_data, many=True).data
    return Response({'data': data})


class PRESSIONviews(generics.CreateAPIView):
    queryset = PRESSION.objects.all()
    serializer_class = PRESSIONSerializer


def Tlist(request):
    all_data = Temp.objects.all()
    data = TempSerializer(all_data, many=True).data
    return Response({'data': data}, content_type='application/json')


class Tempviews(generics.CreateAPIView):
    queryset = Temp.objects.all()
    serializer_class = TempSerializer