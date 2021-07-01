# Generated by Django 3.2 on 2021-07-01 00:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_delete_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('review', models.TextField(max_length=800)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='products.product')),
            ],
        ),
    ]
