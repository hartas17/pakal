# Generated by Django 5.0.4 on 2024-04-11 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huertos', '0002_huerto_foto_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='huerto',
            name='header_img',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]