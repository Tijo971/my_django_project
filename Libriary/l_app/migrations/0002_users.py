# Generated by Django 4.1.7 on 2023-04-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('l_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nme', models.CharField(blank=True, max_length=50, null=True)),
                ('eml', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('mob', models.IntegerField(blank=True, null=True)),
                ('pri', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
