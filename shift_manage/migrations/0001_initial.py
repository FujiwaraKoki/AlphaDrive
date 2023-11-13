# Generated by Django 4.1.5 on 2023-11-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(help_text='従業員')),
                ('shift_type', models.IntegerField(help_text='シフトタイプ')),
                ('work_day', models.DateField(help_text='勤務日')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日時')),
            ],
            options={
                'db_table': 'employee_shift',
            },
        ),
        migrations.CreateModel(
            name='GroupCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='会社の名称', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日時')),
            ],
            options={
                'db_table': 'group_company',
            },
        ),
        migrations.CreateModel(
            name='MaxOfficeHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(help_text='従業員')),
                ('max_hours', models.DecimalField(decimal_places=2, help_text='最大勤務時間', max_digits=5)),
                ('year', models.IntegerField(help_text='年')),
                ('month', models.IntegerField(help_text='月')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日時')),
            ],
            options={
                'db_table': 'max_office_hour',
            },
        ),
        migrations.CreateModel(
            name='ShiftType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="シフトの名称（例： 'Aシフト'）", max_length=255)),
                ('start_time', models.TimeField(help_text='シフトの開始時間')),
                ('end_time', models.TimeField(help_text='シフトの終了時間')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日時')),
            ],
            options={
                'db_table': 'shift_type',
            },
        ),
    ]