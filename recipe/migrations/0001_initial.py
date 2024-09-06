# Generated by Django 5.0.3 on 2024-09-03 17:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe_module',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipeName', models.CharField(max_length=100)),
                ('recipeDescription', models.TextField()),
                ('recipeImage', models.FileField(default='', upload_to='documents/')),
                ('recipeImageUrl', models.TextField(default='')),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]