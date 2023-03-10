# Generated by Django 4.1.5 on 2023-01-06 22:09

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patient_care', '0005_alter_measure_options_alter_unit_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('carb_qty', models.FloatField(verbose_name='Carboidrati')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='patientmeasure',
            name='quantity',
            field=models.FloatField(verbose_name='Quantità'),
        ),
    ]
