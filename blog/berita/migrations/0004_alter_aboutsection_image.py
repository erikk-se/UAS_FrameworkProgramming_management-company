# Generated by Django 5.1.3 on 2024-12-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0003_aboutsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='image',
            field=models.ImageField(default='assets/img/about.jpg', upload_to='assets/img/'),
        ),
    ]
