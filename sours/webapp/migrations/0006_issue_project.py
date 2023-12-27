# Generated by Django 5.0 on 2023-12-27 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_project_alter_issue_descriptions_alter_issue_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]