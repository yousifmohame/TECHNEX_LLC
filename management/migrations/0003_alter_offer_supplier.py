# Generated by Django 4.2.23 on 2025-06-30 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_offer_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.supplier', verbose_name='المورد'),
            preserve_default=False,
        ),
    ]
