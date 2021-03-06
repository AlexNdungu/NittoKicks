# Generated by Django 3.1.1 on 2021-05-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nitto1', '0004_auto_20210502_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverystatus',
            name='delivery_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('DELIVERED', 'Delivered')], default='PENDING', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paymentstatus',
            name='pay_status',
            field=models.CharField(choices=[('UNPAID', 'Unpaid'), ('PAID', 'Paid')], default='UNPAID', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receivedorder',
            name='seen',
            field=models.CharField(choices=[('VIEWING', 'Viewing'), ('VIEWED', 'Viewed')], default='VIEWING', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sentstatus',
            name='sent_status',
            field=models.CharField(choices=[('SENDING', 'Sending'), ('SENT', 'Sent')], default='SENDING', max_length=100, primary_key=True, serialize=False),
        ),
    ]
