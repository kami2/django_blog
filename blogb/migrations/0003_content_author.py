# Generated by Django 3.1.5 on 2021-02-16 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogb', '0002_auto_20210216_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogb.author'),
        ),
    ]