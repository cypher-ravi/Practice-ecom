# Generated by Django 3.1 on 2020-09-08 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
                ('category_publish_data', models.DateTimeField(auto_now_add=True)),
                ('category_status', models.CharField(max_length=20)),
                ('Image', models.ImageField(upload_to='')),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='EachModelSpecification',
            fields=[
                ('spec_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_name', models.CharField(max_length=20)),
                ('spec_publish_date', models.DateTimeField(auto_now_add=True)),
                ('spec_status', models.CharField(max_length=20)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Specification',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='')),
                ('product_company', models.CharField(max_length=50)),
                ('product_publish_date', models.DateTimeField(auto_now_add=True)),
                ('product_regular_price', models.FloatField()),
                ('product_discount_price', models.FloatField()),
                ('product_stock_quantity', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=20)),
                ('model_status', models.CharField(max_length=20)),
                ('model_publish_date', models.DateTimeField(auto_now_add=True)),
                ('model_description', models.CharField(max_length=20)),
                ('model_image', models.ImageField(upload_to='')),
                ('model_price', models.FloatField()),
                ('model_stock_quantity', models.IntegerField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Product Model',
            },
        ),
        migrations.CreateModel(
            name='EachSpecificationValue',
            fields=[
                ('spec_value_id', models.AutoField(primary_key=True, serialize=False)),
                ('spec_value', models.CharField(max_length=100)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('spec_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.eachmodelspecification')),
            ],
            options={
                'verbose_name_plural': 'Specification values',
            },
        ),
        migrations.AddField(
            model_name='eachmodelspecification',
            name='model_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productinfo'),
        ),
    ]
