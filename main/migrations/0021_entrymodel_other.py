# Generated by Django 5.0.3 on 2024-07-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_clustermodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrymodel',
            name='Other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
