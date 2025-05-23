# Generated by Django 4.2.17 on 2025-02-13 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_remove_medicationrequest_checkbox_data_policy_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
        migrations.AddField(
            model_name='medicationrequest',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='medicationrequest',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='medicationrequestotp',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='medicationrequestotp',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
