# Generated by Django 5.0.6 on 2024-11-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_firstname_users_name_remove_articles_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='news_paper_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='authors',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]