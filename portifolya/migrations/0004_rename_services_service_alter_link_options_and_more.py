# Generated by Django 5.0.4 on 2024-04-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portifolya', '0003_services_alter_link_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='service',
        ),
        migrations.AlterModelOptions(
            name='link',
            options={},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Manzil keritildi', 'verbose_name_plural': 'Manzillari keritildi'},
        ),
    ]