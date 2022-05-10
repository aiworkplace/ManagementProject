# Generated by Django 3.0.4 on 2020-03-27 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200324_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cuttingmaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CuttingMaster'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sewingmaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SewingMaster'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subemploy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubEmploy'),
        ),
    ]
