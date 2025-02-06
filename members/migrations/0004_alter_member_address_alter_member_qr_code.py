# Generated by Django 5.1 on 2025-02-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_level_of_study'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='qr_code',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
