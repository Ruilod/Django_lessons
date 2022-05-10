# Generated by Django 4.0.3 on 2022-05-10 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpgsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, upload_to='products_img')),
                ('short_desc', models.TextField(blank=True, max_length=300, verbose_name='short_desc')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpgsapp.productcategory')),
            ],
        ),
    ]