# Generated by Django 3.1.7 on 2021-04-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210402_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
