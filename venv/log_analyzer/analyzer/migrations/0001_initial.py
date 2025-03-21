# Generated by Django 5.1.6 on 2025-03-15 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=100)),
                ('request', models.TextField()),
                ('status_code', models.IntegerField()),
                ('response_size', models.IntegerField()),
                ('user_agent', models.TextField()),
            ],
        ),
    ]
