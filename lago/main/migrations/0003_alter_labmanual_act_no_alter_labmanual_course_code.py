# Generated by Django 4.1.1 on 2022-10-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_labmanual_act_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labmanual',
            name='act_no',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='labmanual',
            name='course_code',
            field=models.CharField(max_length=50),
        ),
    ]
