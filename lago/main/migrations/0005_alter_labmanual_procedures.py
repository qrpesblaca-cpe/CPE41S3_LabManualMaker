# Generated by Django 4.1.1 on 2022-10-26 17:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_labmanual_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmanual',
            name='procedures',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]