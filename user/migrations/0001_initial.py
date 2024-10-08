# Generated by Django 3.2.8 on 2024-10-07 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, choices=[('Created', 'Created'), ('Modified', 'Modified'), ('Deleted', 'Deleted')], max_length=10, null=True)),
                ('user_who_registers', models.JSONField(blank=True, null=True)),
                ('recorded_user', models.JSONField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high_risk_pension', models.BooleanField(default=False)),
                ('identification_number', models.IntegerField()),
                ('surname', models.CharField(max_length=255)),
                ('second_surname', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=255)),
                ('integral_salary', models.BooleanField(default=True)),
                ('salary', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('psswd', models.CharField(default='CiEJVp3v9DHVOcuggO3T', max_length=20, unique=True)),
                ('block', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('internal_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('company', models.IntegerField()),
                ('municipality_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.municipalities')),
                ('payroll_type_document_identification_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.payroll_type_document_identification')),
                ('permission', models.ManyToManyField(blank=True, null=True, to='setting.Permission')),
                ('sub_type_worker_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.sub_type_worker')),
                ('type_contract_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.type_contract')),
                ('type_worker_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='setting.type_worker')),
            ],
        ),
    ]
