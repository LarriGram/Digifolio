# Generated by Django 5.0.1 on 2024-02-23 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_portfolio_email_portfolio_minor_portfolio_resume_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='GitHub',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='LinkedIn',
            field=models.URLField(default='', max_length=100),
        ),
    ]
