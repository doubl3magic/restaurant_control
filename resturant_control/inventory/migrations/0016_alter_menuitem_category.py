# Generated by Django 4.2.4 on 2024-01-04 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('W', 'W'), ('SR', 'Starter'), ('DT', 'Desert'), ('BE', 'Beverage'), ('AL', 'Alcohol'), ('SP', 'Soup'), ('MC', 'Main Course')], max_length=2),
        ),
    ]