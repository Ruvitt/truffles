# Generated by Django 4.2.5 on 2023-11-27 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_produto_alter_cliente_nome_alter_cliente_telefone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
