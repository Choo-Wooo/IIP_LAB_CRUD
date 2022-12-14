# Generated by Django 3.2.7 on 2021-09-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('writer', models.CharField(default='', max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='첨부파일')),
            ],
        ),
    ]
