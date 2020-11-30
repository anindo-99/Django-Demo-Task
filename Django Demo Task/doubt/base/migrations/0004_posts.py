# Generated by Django 3.1.2 on 2020-11-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20201129_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('subject', models.CharField(blank=True, max_length=15, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('lecture', models.FileField(blank=True, default=None, upload_to='video')),
                ('pdf', models.FileField(blank=True, default=None, upload_to='pdfs')),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]