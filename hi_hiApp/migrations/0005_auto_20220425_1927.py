# Generated by Django 2.1.8 on 2022-04-26 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi_hiApp', '0004_auto_20220425_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='status',
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('sent', 'sent'), ('receive', 'receive'), ('topup', 'topup')], default='sent', max_length=12),
            preserve_default=False,
        ),
    ]
