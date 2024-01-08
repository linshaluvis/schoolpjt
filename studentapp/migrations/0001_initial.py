# Generated by Django 5.0 on 2023-12-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255, null=True)),
                ('address', models.TextField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('joining_date', models.DateField()),
                ('qualification', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
