# Generated by Django 3.2.8 on 2021-10-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_alter_person_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]