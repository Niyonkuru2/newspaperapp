# Generated by Django 5.0.6 on 2024-11-07 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_articles_bio_articles_birth_date_articles_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='email',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='website',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='pen_name',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='authors',
            name='website',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='users',
            name='location',
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='api.authors'),
        ),
        migrations.AddField(
            model_name='articles',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.TextField(max_length=222, null=True),
        ),
        migrations.AddField(
            model_name='authors',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.articles'),
        ),
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='created_At',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.users'),
        ),
        migrations.AddField(
            model_name='users',
            name='adress',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
