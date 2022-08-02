# Generated by Django 4.0.4 on 2022-08-02 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=30)),
                ('residence', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=30)),
                ('lga', models.CharField(max_length=30)),
                ('categories', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
