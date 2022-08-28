import uuid as uuid

from django.db import models


class BaseTable(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    jsonrpc = models.CharField(max_length=100)


class Trips(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    distance = models.CharField(max_length=100, null=True, blank=True)
    after_hours_start = models.BooleanField(default=False)
    average_speed = models.CharField(max_length=100, null=True, blank=True)
    maximum_speed = models.IntegerField(null=True, blank=True)
    after_hours_stop_duration = models.CharField(
        max_length=100, null=True, blank=True)
    speed_range1_duration = models.CharField(
        max_length=100, null=True, blank=True)
    work_stop_duration = models.CharField(max_length=100, null=True, blank=True)
    driving_duration = models.CharField(max_length=100, null=True, blank=True)
    _id = models.CharField(max_length=100, null=True, blank=True)
    idling_duration = models.CharField(max_length=100, null=True, blank=True)
    after_hours_distance = models.CharField(
        max_length=100, null=True, blank=True)
    start = models.CharField(max_length=100, null=True, blank=True)
    speed_range2 = models.CharField(max_length=100, null=True, blank=True)
    speed_range3 = models.CharField(max_length=100, null=True, blank=True)
    engine_hours = models.CharField(max_length=100, null=True, blank=True)
    speed_range1 = models.CharField(max_length=100, null=True, blank=True)
    stop_duration = models.CharField(max_length=100, null=True, blank=True)
    is_seat_belt_off = models.BooleanField(default=False)
    speed_range2_duration = models.CharField(
        max_length=100,null=True, blank=True)
    speed_range3_duration = models.CharField(
        max_length=100, null=True, blank=True)
    next_trip_start = models.CharField(max_length=100, null=True, blank=True)
    stop = models.CharField(max_length=100, null=True, blank=True)
    after_hours_driving_duration = models.CharField(
        max_length=100, null=True, blank=True)
    work_driving_duration = models.CharField(
        max_length=100, null=True, blank=True)
    after_hour_send = models.BooleanField(default=False)
    work_distance = models.CharField(max_length=100, null=True, blank=True)
    base_table_id = models.ForeignKey(BaseTable, on_delete=models.CASCADE)


class Driver(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    is_driver = models.BooleanField(default=False)
    _id = models.CharField(max_length=100, null=True, blank=True)
    trip_id = models.OneToOneField(Trips, on_delete=models.CASCADE)


class StopPoint(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    x = models.CharField(max_length=100, null=True, blank=True)
    y = models.CharField(max_length=100, null=True, blank=True)
    trip_id = models.OneToOneField(Trips, on_delete=models.CASCADE)


class Exceptions(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    distance = models.CharField(max_length=100, blank=False, null=False)
    active_to = models.CharField(max_length=100, blank=False, null=False)
    active_from = models.CharField(max_length=100, blank=False, null=False)
    version = models.CharField(max_length=100, blank=False, null=False)
    duration = models.CharField(max_length=100, blank=False, null=False)
    last_modified_datetime = models.CharField(
        max_length=100, blank=False, null=False)
    driver = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    _id = models.CharField(max_length=100, blank=False, null=False)
    base_table_id = models.ForeignKey(BaseTable, on_delete=models.CASCADE)


class Rule(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    _id = models.CharField(max_length=100)
    exceptions_id = models.OneToOneField(Exceptions, on_delete=models.CASCADE)


class Diagnostic(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    _id = models.CharField(max_length=100, blank=False, null=False)
    exceptions_id = models.OneToOneField(Exceptions, on_delete=models.CASCADE)


class Device(models.Model):
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    _id = models.CharField(max_length=100, null=True, blank=True)
    trip_id = models.OneToOneField(
        Trips, on_delete=models.CASCADE, null=True, blank=True)
    exceptions_id = models.OneToOneField(
        Exceptions, on_delete=models.CASCADE, null=True, blank=True)
