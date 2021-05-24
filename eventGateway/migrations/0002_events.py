# Generated by Django 3.1.2 on 2021-05-24 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventGateway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=50)),
                ('max_participants', models.IntegerField()),
                ('up', models.BooleanField(default=False)),
                ('banner', models.ImageField(upload_to='Event_pics')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('rejected', 'rejected'), ('approved', 'approved')], default='pending', max_length=10)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
