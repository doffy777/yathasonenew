# Generated by Django 3.2 on 2022-05-21 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zatlansone', '0002_auto_20220521_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='episode',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='zatlansone.episode'),
        ),
    ]
