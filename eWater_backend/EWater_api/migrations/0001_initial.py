# Generated by Django 3.2.8 on 2022-01-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=70)),
                ('fullname', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('reservation', models.DateField()),
            ],
        ),
    ]