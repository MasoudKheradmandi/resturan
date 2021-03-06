# Generated by Django 4.0.4 on 2022-04-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=300)),
                ('locations', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('date', models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('1', '1'), ('2', '2')], default='9', max_length=3)),
            ],
        ),
    ]
