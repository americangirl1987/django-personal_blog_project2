# Generated by Django 3.2.9 on 2021-12-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='pro/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
