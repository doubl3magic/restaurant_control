# Generated by Django 4.2.4 on 2024-01-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_reciperequirements_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('DT', 'Desert'), ('W', 'W'), ('MC', 'Main Course'), ('AL', 'Alcohol'), ('BE', 'Beverage'), ('SR', 'Starter'), ('SP', 'Soup')], max_length=2),
        ),
    ]
