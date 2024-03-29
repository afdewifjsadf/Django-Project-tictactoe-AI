# Generated by Django 3.2.9 on 2021-11-06 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_alter_player_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='bot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.bot'),
        ),
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
