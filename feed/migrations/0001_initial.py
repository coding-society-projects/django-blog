# Generated by Django 3.1.2 on 2021-04-10 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('content', models.TextField(blank=True)),
                ('slug', models.CharField(max_length=140, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='feed.category')),
            ],
        ),
    ]
