# Generated by Django 4.0.3 on 2022-04-06 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_alter_imovelfoto_options_alter_imovelfoto_imovel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imovelfoto',
            options={'default_related_name': 'imoveisfotos'},
        ),
        migrations.AlterField(
            model_name='imovelfoto',
            name='imovel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovel'),
        ),
    ]