# Generated by Django 4.1.7 on 2023-02-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('01', 'Танки'), ('02', 'Хилы'), ('03', 'ДД'), ('04', 'Торговцы'), ('05', 'Гилдмастеры'), ('06', 'Квестгиверы'), ('07', 'Кузнецы'), ('08', 'Кожевники'), ('09', 'Зельевары'), ('10', 'Мастера заклинаний')], default='01', max_length=2),
        ),
    ]
