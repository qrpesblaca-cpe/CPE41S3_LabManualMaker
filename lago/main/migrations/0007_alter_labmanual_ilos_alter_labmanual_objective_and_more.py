# Generated by Django 4.1.1 on 2022-10-29 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_labmanual_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmanual',
            name='ilos',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='labmanual',
            name='objective',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='labmanual',
            name='questions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='labmanual',
            name='res',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='labmanual',
            name='supplementary',
            field=models.TextField(),
        ),
    ]
