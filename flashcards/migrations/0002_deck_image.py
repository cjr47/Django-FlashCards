# Generated by Django 4.0.1 on 2022-02-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]