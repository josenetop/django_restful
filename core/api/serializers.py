from rest_framework.serializers import ModelSerializer
from core.models import *

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ('id','name','description')

