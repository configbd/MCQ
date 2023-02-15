# Generated by Django 4.1.5 on 2023-02-03 15:31

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqapp', '0007_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articless',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]