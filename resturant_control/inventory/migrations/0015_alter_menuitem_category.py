# Generated by Django 4.2.4 on 2024-01-04 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('SR', 'Starter'), ('SP', 'Soup'), ('BE', 'Beverage'), ('MC', 'Main Course'), ('W', 'W'), ('DT', 'Desert'), ('AL', 'Alcohol')], max_length=2),
        ),
    ]
