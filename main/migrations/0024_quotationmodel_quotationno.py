# Generated by Django 5.0.3 on 2024-07-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_quotationmodel_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationmodel',
            name='QuotationNo',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
