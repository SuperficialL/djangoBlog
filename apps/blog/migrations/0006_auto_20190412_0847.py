# Generated by Django 2.1.7 on 2019-04-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190412_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否有效'),
        ),
        migrations.AddField(
            model_name='link',
            name='is_show',
            field=models.BooleanField(default=False, verbose_name='是否首页展示'),
        ),
    ]
