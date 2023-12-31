# Generated by Django 4.2.3 on 2023-08-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_orders_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surename', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=50, verbose_name='Эл.почта')),
                ('phone', models.TextField(max_length=11, verbose_name='Телефон')),
                ('review', models.TextField(verbose_name='Напишите отзыв здесь')),
                ('recommendation', models.CharField(max_length=5)),
                ('suggestion', models.TextField(verbose_name='Что бы вы изменили в работе?')),
            ],
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
