# Generated by Django 3.1.1 on 2021-04-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vouch', '0003_remove_contact_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
