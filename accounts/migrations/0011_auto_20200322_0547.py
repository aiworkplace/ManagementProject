# Generated by Django 3.0.4 on 2020-03-21 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200322_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
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
