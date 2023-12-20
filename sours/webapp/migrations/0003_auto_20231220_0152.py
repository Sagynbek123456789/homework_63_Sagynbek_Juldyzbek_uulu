# Generated by Django 5.0 on 2023-12-19 19:52

from django.db import migrations


def transfer_type(apps, schema_editor):
    Issue = apps.get_model('webapp.Issue')

    for issue in Issue.objects.all():
        issue.types.add(issue.type)


def rollback_transfer(apps, schema_editor):
    Issue = apps.get_model('webapp.Issue')

    for issue in Issue.objects.all():
        issue.type = issue.types.first()
        issue.save()


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_issue_types_alter_issue_status'),
    ]

    operations = [
        migrations.RunPython(transfer_type, rollback_transfer)
    ]