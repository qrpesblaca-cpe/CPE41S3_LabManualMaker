# Generated by Django 4.1.1 on 2022-12-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_course_labmanual_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='labmanual',
            name='image_1',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labmanual',
            name='image_2',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]