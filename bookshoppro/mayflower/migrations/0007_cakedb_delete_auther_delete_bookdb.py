# Generated by Django 4.0.4 on 2023-01-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayflower', '0006_auther'),
    ]

    operations = [
        migrations.CreateModel(
            name='cakedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cakename', models.CharField(blank=True, max_length=100, null=True)),
                ('Price', models.CharField(blank=True, max_length=100, null=True)),
                ('About', models.CharField(blank=True, max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='auther',
        ),
        migrations.DeleteModel(
            name='bookdb',
        ),
    ]