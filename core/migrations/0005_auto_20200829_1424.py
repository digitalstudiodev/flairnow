# Generated by Django 3.0.7 on 2020-08-29 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200829_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='gpa',
            field=models.CharField(choices=[('N', "I don't have a GPA"), ('G0', 'Below 1.0'), ('G1', 'Between 1.0 and 1.5'), ('G2', 'Between 1.5 and 2.0'), ('G3', 'Between 2.0 and 2.5'), ('G4', 'Between 2.5 and 3.0'), ('G5', 'Between 3.0 and 3.5'), ('G6', 'Between 3.5 and 4.0'), ('P', 'Prefer Not To Say')], default=None, max_length=1000, null=True, verbose_name='GPA'),
        ),
    ]
