# Generated by Django 3.2 on 2021-04-28 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
