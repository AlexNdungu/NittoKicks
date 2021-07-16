# Generated by Django 3.1.1 on 2021-05-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deliveryStatus',
            fields=[
                ('delivery_status', models.CharField(default='pending', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='paymentStatus',
            fields=[
                ('pay_status', models.CharField(default='unpaid', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='productCategory',
            fields=[
                ('category', models.CharField(default='Both', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='productStatus',
            fields=[
                ('status', models.CharField(default='Available', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='receivedOrder',
            fields=[
                ('seen', models.CharField(default='viewing', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='sentStatus',
            fields=[
                ('sent_status', models.CharField(default='sending', max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]