from rest_framework import serializers, viewsets
from .models import BPM, PRESSION, Temp


class BPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = BPM
        fields = ['id', 'bpm', 'dt']


class PRESSIONSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRESSION
        fields = ['id', 'systolique', 'diastolique', 'dt']


class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ['id', 'temp', 'dt']

