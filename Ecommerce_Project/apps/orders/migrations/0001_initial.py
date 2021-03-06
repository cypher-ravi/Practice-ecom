# Generated by Django 3.1 on 2020-09-08 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_no', models.IntegerField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('total_order', models.IntegerField()),
                ('shipping_date', models.DateField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_quantity', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderdetail'),
        ),
    ]
