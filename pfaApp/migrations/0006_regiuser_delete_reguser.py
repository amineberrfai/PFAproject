# Generated by Django 4.2 on 2023-05-05 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfaApp', '0005_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('receId', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='RegUser',
        ),
    ]
