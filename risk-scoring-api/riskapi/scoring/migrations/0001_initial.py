# Generated by Django 5.2 on 2025-05-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=100)),
                ('data_sensitivity', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('processor_name', models.CharField(max_length=100)),
                ('risk_score', models.IntegerField(blank=True, null=True)),
                ('risk_breakdown', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
