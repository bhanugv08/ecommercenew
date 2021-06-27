# Generated by Django 3.1.7 on 2021-04-01 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0009_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255, null=True)),
                ('Password', models.CharField(max_length=200, null=True)),
                ('User_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
