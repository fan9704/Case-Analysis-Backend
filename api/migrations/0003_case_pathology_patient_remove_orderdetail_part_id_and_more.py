# Generated by Django 4.2.11 on 2024-05-17 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_orderdetail_order_i_orderdetail_order_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField()),
                ('clinical_findings', models.TextField()),
                ('diagnostic_process', models.TextField()),
                ('intervention_and_treatment', models.TextField()),
                ('outcome', models.TextField()),
                ('discuss', models.TextField()),
                ('pathology', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pathology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specimen_source', models.TextField()),
                ('specimen_type', models.TextField()),
                ('specimen_size', models.TextField()),
                ('check_description', models.TextField()),
                ('summary', models.TextField()),
                ('addition_test', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sexual', models.CharField(max_length=10)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='part_id',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.AddField(
            model_name='pathology',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient'),
        ),
        migrations.AddField(
            model_name='case',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.patient'),
        ),
    ]
