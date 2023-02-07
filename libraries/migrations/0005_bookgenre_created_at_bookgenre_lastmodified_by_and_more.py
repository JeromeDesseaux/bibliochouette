# Generated by Django 4.1.5 on 2023-02-07 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraries', '0004_rename_pagecount_book_page_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookgenre',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookgenre',
            name='lastmodified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_lastmodified_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookgenre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bookgenre',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
