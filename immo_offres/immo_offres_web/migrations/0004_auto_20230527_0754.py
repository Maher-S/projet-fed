# Generated by Django 3.2.19 on 2023-05-27 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo_offres_web', '0003_alter_article_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='images',
            field=models.TextField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0ucLwpzy0WPiV_Mr4oMiVwx8bPjf3s4NjVw&usqp=CAU', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.IntegerField(),
        ),
    ]
