# Generated by Django 4.2.13 on 2024-05-30 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
