# Generated by Django 5.1.1 on 2024-09-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_grupo_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
    ]
