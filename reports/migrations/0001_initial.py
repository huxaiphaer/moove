# Generated by Django 3.1 on 2022-08-28 19:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('jsonrpc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('custom_properties', models.CharField(max_length=100)),
                ('accelerometer_threshold_warning_factor', models.CharField(max_length=100)),
                ('minor', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('parameter_version_on_device', models.IntegerField()),
                ('wifi_hotspot_limits', models.CharField(max_length=100)),
                ('enable_control_external_relay', models.BooleanField()),
                ('device_type', models.CharField(max_length=100)),
                ('is_reverse_detect_on', models.BooleanField()),
                ('pin_device', models.BooleanField()),
                ('is_aux_inverted', models.CharField(max_length=100)),
                ('major', models.IntegerField()),
                ('is_driver_seatbelt_warning_on', models.BooleanField()),
                ('disable_sleeper_berth', models.BooleanField()),
                ('is_passenger_seatbelt_warning_on', models.BooleanField()),
                ('enable_speed_warning', models.BooleanField()),
                ('_id', models.CharField(max_length=100)),
                ('gps_off_delay', models.IntegerField()),
                ('engine_type', models.CharField(max_length=100)),
                ('device_plans', models.CharField(max_length=100)),
                ('is_iox_connection_enabled', models.BooleanField()),
                ('serial_number', models.CharField(max_length=100)),
                ('acceleration_warning_threshold', models.IntegerField()),
                ('idle_minutes', models.CharField(max_length=100)),
                ('fuel_tank_capacity', models.CharField(max_length=100)),
                ('enable_beep_on_idle', models.BooleanField()),
                ('disable_buzzer', models.BooleanField()),
                ('parameter_version', models.IntegerField()),
                ('odometer_factor', models.CharField(max_length=100)),
                ('odometer_offset', models.CharField(max_length=100)),
                ('aux_warning_speed', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('time_to_download', models.CharField(max_length=100)),
                ('is_speed_indicator', models.BooleanField()),
                ('engine_hour_offset', models.CharField(max_length=100)),
                ('immobilize_arming', models.IntegerField()),
                ('enable_aux_warning', models.CharField(max_length=100)),
                ('ignore_downloads_until', models.CharField(max_length=100)),
                ('license_state', models.CharField(max_length=100)),
                ('auto_hos', models.CharField(max_length=100)),
                ('active_to', models.CharField(max_length=100)),
                ('min_accident_speed', models.CharField(max_length=100)),
                ('rpm_value', models.IntegerField()),
                ('seat_belt_warning_speed', models.CharField(max_length=100)),
                ('enable_beep_on_rpm', models.BooleanField()),
                ('timezone_id', models.CharField(max_length=100)),
                ('speeding_off', models.IntegerField()),
                ('enable_beep_on_dangerous_driving', models.BooleanField()),
                ('engine_vehicle_identification_number', models.CharField(max_length=100)),
                ('is_active_tracking_enabled', models.BooleanField()),
                ('speeding_on', models.IntegerField()),
                ('is_auxign_trigger', models.CharField(max_length=100)),
                ('immobilize_unit', models.BooleanField()),
                ('braking_warning_threshold', models.IntegerField()),
                ('max_seconds_between_logs', models.IntegerField()),
                ('active_from', models.CharField(max_length=100)),
                ('ensure_hot_start', models.BooleanField()),
                ('enable_must_reprogram', models.BooleanField()),
                ('cornering_warning_threshold', models.IntegerField()),
                ('go_talk_language', models.CharField(max_length=100)),
                ('auto_groups', models.CharField(max_length=100)),
                ('vehicle_identification_number', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100)),
                ('external_device_shutdown_delay', models.IntegerField()),
                ('license_plate', models.CharField(max_length=100)),
                ('base_table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.basetable')),
            ],
        ),
        migrations.CreateModel(
            name='WorkTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('_id', models.CharField(max_length=100)),
                ('result_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('_id', models.CharField(max_length=100)),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DevicePlanBillingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('device_plan_name', models.CharField(max_length=100)),
                ('billing_level', models.CharField(max_length=100)),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceFlags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('is_garmin_allowed', models.BooleanField()),
                ('is_ui_allowed', models.BooleanField()),
                ('is_vin_allowed', models.BooleanField()),
                ('active_features', models.CharField(max_length=100)),
                ('is_active_tracking_allowed', models.BooleanField()),
                ('is_hos_allowed', models.BooleanField()),
                ('is_iridium_allowed', models.BooleanField()),
                ('is_engine_allowed', models.BooleanField()),
                ('is_odometer_allowed', models.BooleanField()),
                ('is_trip_detail_allowed', models.BooleanField()),
                ('rate_plans', models.CharField(max_length=100)),
                ('result_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CustomParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('offset', models.IntegerField()),
                ('bytes', models.CharField(max_length=100)),
                ('is_enabled', models.BooleanField()),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='CustomFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('auto_hos', models.BooleanField()),
                ('result_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reports.vehicle')),
            ],
        ),
    ]
