# Generated by Django 4.1.3 on 2023-04-18 07:08

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=17, null=True),
        ),
    ]
