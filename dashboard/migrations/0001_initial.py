# Generated by Django 4.2.17 on 2025-02-23 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inquiry', '0007_delete_medicationrequestanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicationRequestAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('diagnosis', models.TextField(null=True)),
                ('private_notes', models.TextField(null=True)),
                ('medication', models.TextField(null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_request_answers', to=settings.AUTH_USER_MODEL)),
                ('medication_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='inquiry.medicationrequest')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
