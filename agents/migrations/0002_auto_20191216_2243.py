# Generated by Django 2.1.7 on 2019-12-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agents',
            old_name='agent_id',
            new_name='state_license_id',
        ),
        migrations.AddField(
            model_name='agents',
            name='agent_image',
            field=models.ImageField(default=334, upload_to='agent_image'),
            preserve_default=False,
        ),
    ]