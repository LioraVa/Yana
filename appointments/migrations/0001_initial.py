# Generated by Django 3.0.5 on 2020-05-04 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centers', '0002_auto_20200504_1748'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('specielity', models.CharField(max_length=200)),
                ('center_id', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cen_i_work_at', to='centers.Center')),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('time_field', models.TimeField(blank=True, null=True)),
                ('date_field', models.DateField(blank=True, null=True)),
                ('center', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='cen_id', to='centers.Center')),
                ('doctor_name', models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.CASCADE, related_name='doc_name', to='appointments.Doctors')),
                ('pat_id', models.ForeignKey(default='username', on_delete=django.db.models.deletion.CASCADE, related_name='u_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]