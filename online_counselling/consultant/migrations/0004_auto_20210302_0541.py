# Generated by Django 2.2.12 on 2021-03-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('consultant', '0003_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='portfolio_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
