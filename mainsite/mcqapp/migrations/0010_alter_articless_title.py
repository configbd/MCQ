# Generated by Django 4.1.5 on 2023-02-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqapp', '0009_alter_articless_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articless',
            name='title',
            field=models.CharField(blank=True, default='Empty Title', max_length=300, null=True),
        ),
    ]