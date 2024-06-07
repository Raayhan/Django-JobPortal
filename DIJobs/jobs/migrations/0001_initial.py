# Generated by Django 5.0.6 on 2024-06-07 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(default='N/A', max_length=40)),
                ('company', models.CharField(default='N/A', max_length=255)),
                ('experience', models.IntegerField(blank=True, default=0, null=True)),
                ('deadline', models.DateField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.category')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
