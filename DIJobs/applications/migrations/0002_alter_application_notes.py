# Generated by Django 5.0.6 on 2024-06-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='notes',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]