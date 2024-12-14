# Generated by Django 5.1.3 on 2024-12-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beejournal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalqueen',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'Hvid'), ('yellow', 'Gul'), ('red', 'Rød'), ('green', 'Grøn'), ('blue', 'Blå')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='queen',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'Hvid'), ('yellow', 'Gul'), ('red', 'Rød'), ('green', 'Grøn'), ('blue', 'Blå')], max_length=8, null=True),
        ),
    ]
