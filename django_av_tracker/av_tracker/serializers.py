from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AV, Device_Types


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class AVSerializer(serializers.ModelSerializer):

    id = serializers.HyperlinkedIdentityField(view_name='av_detail', format='html')
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = AV
        fields = ('id','hostname', 'device_type', 'date_gen', 'date_rec', 'ip_address', 'username', 'location', 'organization', 'action', 'detection', 'logs', 'dat_version', 'filepath', 'comments', 'updating', 'created_by')

    def create(self, validated_data):
        return AV.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.hostname = validated_data.get('hostname', instance.hostname)
        instance.device_type = validated_data.get('device_type', instance.device_type)
        instance.date_gen = validated_data.get('date_gen', instance.date_gen)
        instance.date_rec = validated_data.get('date_rec', instance.date_rec)
        instance.ip_address = validated_data.get('ip_address', instance.ip_address)
        instance.username = validated_data.get('username', instance.username)
        instance.location = validated_data.get('location', instance.location)
        instance.organization = validated_data.get('organization', instance.organization)
        instance.action = validated_data.get('action', instance.action)
        instance.detection = validated_data.get('detection', instance.detection)
        instance.logs = validated_data.get('logs', instance.logs)
        instance.dat_version = validated_data.get('dat_version', instance.dat_version)
        instance.filepath = validated_data.get('filepath', instance.filepath)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.updating = validated_data.get('updating', instance.updating)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.save()
        return instance