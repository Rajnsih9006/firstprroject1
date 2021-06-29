from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

    # for deserialization
    def create(self,validated_data):
        return Employee.objects.create(**validated_data)
    #
    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance