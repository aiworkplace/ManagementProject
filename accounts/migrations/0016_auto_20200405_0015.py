# Generated by Django 3.0.4 on 2020-04-04 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200328_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='cuttingmaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CuttingMaster'),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(default='hello', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='sewingmaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SewingMaster'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('CuttingMaster', 'CuttingMaster'), ('SewingMaster', 'SewingMaster'), ('OtherEmploy', 'OtherEmploy'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered'), ('Complete Order', 'Complete Order')], default='Pending', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='subemploy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubEmploy'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
