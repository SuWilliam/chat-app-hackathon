# Generated by Django 3.2.10 on 2022-05-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default=None)),
            ],
        ),
    ]