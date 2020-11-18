# Generated by Django 3.1.3 on 2020-11-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorites', to='accounts.user_details'),
        ),
    ]
