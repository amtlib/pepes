# Generated by Django 3.0.3 on 2020-02-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20200229_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pepe',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
