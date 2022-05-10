# Generated by Django 3.0.4 on 2020-03-21 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200322_0430'),
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
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.SubEmploy'),
        ),
    ]