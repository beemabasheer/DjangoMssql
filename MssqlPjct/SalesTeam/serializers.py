from rest_framework import serializers
from SalesTeam.models import SalesTeam

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesTeam
        fields = '__all__'
