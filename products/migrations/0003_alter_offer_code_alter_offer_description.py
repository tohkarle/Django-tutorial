# Generated by Django 4.1.3 on 2022-12-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]