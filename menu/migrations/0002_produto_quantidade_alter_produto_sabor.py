# Generated by Django 4.2.5 on 2023-11-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='sabor',
            field=models.CharField(choices=[('Morango', 'Chocolate'), ('Limão', 'Ninho'), ('Doce de leite', 'Goiaba')], max_length=20),
        ),
    ]
