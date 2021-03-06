# Generated by Django 2.2.3 on 2019-08-09 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_plantshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsershowLink',
            fields=[
                ('uslinkid', models.CharField(db_column='uslinkID', max_length=45, primary_key=True, serialize=False)),
                ('plantshow_spid', models.ForeignKey(blank=True, db_column='plantshow_spID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.PlantShow')),
                ('user_userid', models.ForeignKey(blank=True, db_column='User_userId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.User')),
            ],
            options={
                'db_table': 'usershowlink',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Incubatorhardinf',
            fields=[
                ('inchardinfID', models.CharField(db_column='InchardinfID', max_length=45, primary_key=True, serialize=False)),
                ('icpu', models.CharField(db_column='iCPU', max_length=45, null=True)),
                ('itemph', models.CharField(db_column='iTemph', max_length=45, null=True)),
                ('ihumh', models.CharField(db_column='iHumh', max_length=45, null=True)),
                ('ipressh', models.CharField(db_column='iPressh', max_length=45, null=True)),
                ('ilighth', models.CharField(db_column='iLighth', max_length=45, null=True)),
                ('inchardinfdate', models.DateField(auto_now=True, db_column=' inchardinfDate')),
                ('incubator_incuno', models.ForeignKey(blank=True, db_column='Incubator_IncuNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Incubator')),
            ],
            options={
                'db_table': 'incubatorhardinf',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Incplantdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayavertemp', models.CharField(db_column='dayAvertemp', max_length=45, null=True)),
                ('dayaverhum', models.CharField(db_column='dayAverhum', max_length=45, null=True)),
                ('dayaverpress', models.CharField(db_column='dayAverpress', max_length=45, null=True)),
                ('dayaverlight', models.CharField(db_column='dayAverlight', max_length=45, null=True)),
                ('Plant_plantname', models.ForeignKey(blank=True, db_column='plant_plantname', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Plant')),
                ('incubator_incuno', models.ForeignKey(blank=True, db_column='Incubator_IncuNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.Incubator')),
            ],
            options={
                'db_table': 'Incplantdetail',
                'managed': True,
            },
        ),
    ]
