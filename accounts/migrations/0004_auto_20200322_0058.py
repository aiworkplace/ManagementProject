# Generated by Django 3.0.4 on 2020-03-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cuttingmaster_sewingmaster_subemploy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('CuttingMaster', 'CuttingMaster'), ('SewingMaster', 'SewingMaster'), ('OtherEmploy', 'OtherEmploy'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Complete Order', 'Complete Order')], max_length=200, null=True),
        ),
    ]