# Generated by Django 3.1.1 on 2021-05-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nitto1', '0010_auto_20210503_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='shoe_availability',
            field=models.ForeignKey(default='AVAILABLE', on_delete=django.db.models.deletion.CASCADE, to='Nitto1.productstatus'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.ForeignKey(default='NONE', on_delete=django.db.models.deletion.CASCADE, to='Nitto1.productcategory'),
        ),
    ]