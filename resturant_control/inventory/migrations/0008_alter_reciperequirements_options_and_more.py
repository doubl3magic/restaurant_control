# Generated by Django 4.2.4 on 2024-01-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_menuitem_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reciperequirements',
            options={'ordering': ['menu_item']},
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('AL', 'Alcohol'), ('DT', 'Desert'), ('BE', 'Beverage'), ('SR', 'Starter'), ('W', 'W'), ('SP', 'Soup'), ('MC', 'Main Course')], max_length=2),
        ),
    ]