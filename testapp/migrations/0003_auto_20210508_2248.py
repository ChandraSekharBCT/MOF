# Generated by Django 3.2.1 on 2021-05-08 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_normal_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normal_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Whole_Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('zip_code', models.IntegerField()),
                ('gst_no', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whole_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]