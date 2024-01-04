# Generated by Django 4.2.4 on 2023-08-31 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('SP', 'Soup'), ('SR', 'Starter'), ('MC', 'Main Course'), ('W', 'W'), ('DT', 'Desert'), ('BE', 'Beverage'), ('AL', 'Alcohol')], max_length=2),
        ),
    ]