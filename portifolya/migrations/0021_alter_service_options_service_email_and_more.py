# Generated by Django 5.0.4 on 2024-04-25 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolya', '0020_alter_service_options_remove_service_email_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('location', 'email', 'phone_number'), 'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='service',
            name='email',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='phone_number',
            field=models.CharField(default=None, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='location',
            field=models.CharField(max_length=120),
        ),
    ]
