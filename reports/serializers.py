"""Serializers"""
from rest_framework import serializers

from reports.models import Vehicle, BaseTable, Trips, Device, Exceptions


class BaseTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseTable
        fields = ('uuid', 'jsonrpc',)


class DeviceSerializer(serializers.ModelSerializer):

    class Metal:
        model = Device
        fields = ('geo_tab_id',)


class VehicleSerializer(serializers.ModelSerializer):
    base_table = BaseTableSerializer(many=False, required=False)

    class Meta:
        model = Vehicle
        fields = ('geo_tab_id', 'license_plate', 'base_table',)


class TripsSerializer(serializers.ModelSerializer):
    base_table = BaseTableSerializer(many=False, required=False)
    device_id = DeviceSerializer(many=False, required=False)

    class Meta:
        model = Trips
        fields = (
            'uuid', 'distance', 'start', 'stop', 'base_table', 'device_id')


class ExceptionSerializer(serializers.ModelSerializer):
    base_table = BaseTableSerializer(many=False, required=False)
    device_id = DeviceSerializer(many=False, required=False)

    class Meta:
        model = Exceptions
        fields = (
            'uuid', 'driver', 'active_to', 'active_from', 'base_table',
            'device_id')
