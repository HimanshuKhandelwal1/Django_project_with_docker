# Generated by Django 4.1.8 on 2023-04-21 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knapsack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knaps',
            name='Attachment',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
