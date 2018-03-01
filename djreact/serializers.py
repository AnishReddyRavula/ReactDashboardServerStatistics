from rest_framework import serializers
from watch.models import ServerDetails
from watch.models import ServerUsage


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerDetails
        fields = ('department_name', 'metric')

class UsageSerializer(serializers.ModelSerializer):
    detail = serializers.ReadOnlyField(source='ServerDetails.department_name')


    class Meta:
        model = ServerUsage
        fields = ('detail', 'date_time', 'units')