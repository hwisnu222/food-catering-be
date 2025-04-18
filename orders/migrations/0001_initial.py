# Generated by Django 5.1.7 on 2025-03-26 03:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField()),
                ('delivery_address', models.TextField()),
                ('special_notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Confirmed'), ('IP', 'In Progress'), ('OD', 'Out for Delivery'), ('CP', 'Completed'), ('CN', 'Cancelled')], default='P', max_length=2)),
                ('is_paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('special_request', models.TextField(blank=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
        ),
    ]
