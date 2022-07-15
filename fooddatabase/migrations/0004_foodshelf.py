# Generated by Django 4.0.6 on 2022-07-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fooddatabase', '0003_profile_email_profile_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foodshelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('expiry_date', models.IntegerField(default=0)),
                ('food_status', models.CharField(max_length=200)),
                ('liter_kilogram', models.IntegerField(default=0)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]