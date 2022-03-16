# Generated by Django 4.0.3 on 2022-03-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_request_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='cost_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.costmodel'),
        ),
    ]
