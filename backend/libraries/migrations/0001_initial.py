# Generated by Django 4.1.5 on 2023-02-05 07:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('holders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('description', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=14, verbose_name='isbn')),
                ('pageCount', models.SmallIntegerField(default=0)),
                ('publicationDate', models.DateField(blank=True, null=True)),
                ('title', models.CharField(max_length=42, verbose_name='title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(blank=True, max_length=32, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, max_length=52, null=True, verbose_name='lastname')),
                ('surname', models.CharField(blank=True, max_length=32, null=True, verbose_name='surname')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('returned_date', models.DateField(blank=True, null=True)),
                ('expected_return_date', models.DateField(default=datetime.date(2023, 2, 26))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.reader')),
            ],
            options={
                'ordering': ['-expected_return_date'],
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=32, verbose_name='label')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holders.holdergroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=42, verbose_name='label')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='libraries.bookgenre'),
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraries.library'),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
