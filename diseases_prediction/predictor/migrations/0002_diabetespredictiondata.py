# Generated by Django 4.2.7 on 2023-12-03 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesPredictionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField(default=0)),
                ('glucose', models.IntegerField(default=0)),
                ('blood_pressure', models.IntegerField(default=0)),
                ('skin_thickness', models.IntegerField(default=0)),
                ('insulin', models.IntegerField(default=0)),
                ('bmi', models.FloatField(default=0)),
                ('diabetes_pedigree_function', models.FloatField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('prediction', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]