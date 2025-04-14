# Generated by Django 5.1.3 on 2025-04-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beejournal', '0007_alter_historicalqueen_color_alter_queen_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalhive',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'Hvid (1-6)'), ('yellow', 'Gul (2-7)'), ('red', 'Rød (3-8)'), ('green', 'Grøn (4-9)'), ('blue', 'Blå (5-0)')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='hive',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'Hvid (1-6)'), ('yellow', 'Gul (2-7)'), ('red', 'Rød (3-8)'), ('green', 'Grøn (4-9)'), ('blue', 'Blå (5-0)')], max_length=8, null=True),
        ),
    ]
