# Generated by Django 5.2.3 on 2025-06-14 08:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('FIC', 'Fiction'), ('NF', 'Non-Fiction'), ('MYST', 'Mystery'), ('THRL', 'Thriller'), ('ROM', 'Romance'), ('SCI', 'Science Fiction'), ('FANT', 'Fantasy'), ('BIO', 'Biography'), ('HIST', 'Historical'), ('PHIL', 'Philosophy'), ('POET', 'Poetry'), ('HORR', 'Horror'), ('SELF', 'Self-help'), ('TECH', 'Technology'), ('BUS', 'Business'), ('SPIR', 'Spirituality'), ('EDU', 'Educational'), ('TRAV', 'Travel'), ('ART', 'Art & Photography'), ('COOK', 'Cooking')], max_length=20)),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('publication_date', models.DateField()),
                ('avgRating', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
