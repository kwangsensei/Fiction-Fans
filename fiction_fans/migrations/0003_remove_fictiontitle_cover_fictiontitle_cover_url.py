# Generated by Django 4.1.1 on 2022-11-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiction_fans', '0002_alter_fictiontitle_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fictiontitle',
            name='cover',
        ),
        migrations.AddField(
            model_name='fictiontitle',
            name='cover_url',
            field=models.URLField(default='gs://fiction-fans.appspot.com/no-cover.png', max_length=255),
        ),
    ]
