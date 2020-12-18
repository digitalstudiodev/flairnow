# Generated by Django 3.0.7 on 2020-12-17 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='IN', max_length=1000, verbose_name='Opportunity Type')),
                ('title', models.CharField(default=None, max_length=1000, verbose_name='Position Title')),
                ('field', models.CharField(choices=[('F0', 'Athletic Training'), ('F1', 'Biology'), ('F2', 'Chemistry'), ('F3', 'Phyics'), ('F4', 'Environmental Science'), ('F5', 'Exercise Sci/Kinesiology'), ('F6', 'Fisheries and Wildlife'), ('F7', 'Food Science'), ('F8', 'Forest Management'), ('F9', 'Marine Science'), ('F10', 'Nursing (RN/BSN)'), ('F11', 'Organic/Urban Farming'), ('F12', 'Pharmacy'), ('F13', 'Physicians Assistant'), ('F14', 'Pre - Dental'), ('F15', 'Pre - Medical'), ('F15', 'Pre - Veterinary Medicine'), ('L0', 'Apparel/Textile Design'), ('L1', 'Dance'), ('L2', 'Film/Broadcast'), ('L3', 'Fine/Studio Art'), ('L4', 'Graphic Design'), ('L5', 'Industrial Design'), ('L6', 'Interior Design'), ('L7', 'Landscape Architecture'), ('L8', 'Music'), ('L9', 'Theatre'), ('L10', 'Urban Planning'), ('L11', 'Video Game Design'), ('L12', 'Web Design/Digital Media'), ('A0', 'Arts Management'), ('A1', 'Education'), ('A2', 'Emergency Management'), ('A3', 'English/Writing'), ('A4', 'Equine Science/Mgmt'), ('A5', 'Family & Child Science'), ('A6', 'History'), ('A7', 'Journalism'), ('A8', 'Language Studies'), ('A9', 'Non-Profit Management'), ('A10', 'Parks and Recreation Management'), ('A11', 'Peace/Conflict Studies'), ('A12', 'Philosophy'), ('A13', 'Political Science'), ('A14', 'Psychology / Sociology'), ('A15', 'Sports Turf/Golf Mgmt'), ('A16', 'Women/Gender Studies'), ('I0', 'Aerospace Engineering'), ('I1', 'Astronomy / Physics'), ('I2', 'Aviation/Aeronautics'), ('I3', 'Biomedical Engineering'), ('I4', 'Chemical Engineering'), ('I5', 'Civil Engineering'), ('I6', 'Computer Science'), ('I7', 'Cyber Security'), ('I8', 'Electrical Engineering'), ('I9', 'Energy Science'), ('I10', 'Industrial Engineering'), ('I11', 'Industrial Technology'), ('I12', 'Materials Science'), ('I13', 'Mathematics'), ('I14', 'Mechanical Engineering'), ('R0', 'Accounting - General'), ('R1', 'Business - General'), ('R2', 'Construction Management'), ('R3', 'Data Science - Analytics'), ('R4', 'Economics (National + Global)'), ('R5', 'Finance'), ('R6', 'Hospitality Management'), ('R7', 'Human Resources Mgmt'), ('R8', 'Information Systems (MIS)'), ('R9', 'Insurance & Risk Mgmt'), ('R10', 'Marketing / Advertising'), ('R11', 'Public Health Administration'), ('R12', 'Sport Management'), ('R13', 'Supply Chain Mgmt (Logistics)')], default=None, max_length=1000)),
                ('desc', models.TextField(default=None, verbose_name='Description')),
                ('pos', models.IntegerField(default=1, verbose_name='# of Applicants')),
                ('edu_level', models.CharField(choices=[('N', 'None'), ('L0', 'Middle School (7, 8 Grades)'), ('L1', 'Grade 9 High School'), ('L2', 'Grade 10 High School'), ('L3', 'Grade 11 High School'), ('L4', 'Grade 12 High School'), ('L5', 'First Year Undergraduate'), ('L6', 'Second Year Undergraduate'), ('L7', 'Third Year Undergraduate'), ('L8', 'Fourth Year Undergraduate'), ('L9', 'Five Year or More Undergraduate'), ('L10', 'Graduate Student'), ('L11', 'Vocational Education')], default='None', max_length=1000, verbose_name='Edu level')),
                ('degree', models.CharField(choices=[('N', 'None'), ('L0', 'High School Diploma (or Equivalent)'), ('L1', 'Associate Degree'), ('L2', "Bachelor's Degree"), ('L3', "Master's Degree"), ('L4', 'Doctoral Degree')], default='None', max_length=1000, verbose_name='Degree Type')),
                ('amount', models.IntegerField(default=0, help_text='Enter as the complete amount for duration of working period.', verbose_name='Amount')),
                ('valid_date', models.DateField(default=datetime.date(2021, 3, 17), verbose_name='Deadline')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(default=None, max_length=50, verbose_name='City')),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('DC', 'District of Columbia')], default=None, max_length=1000, verbose_name='State')),
                ('org', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='SC', max_length=1000, verbose_name='Opportunity Type')),
                ('title', models.CharField(default=None, max_length=1000, verbose_name='Title')),
                ('field', models.CharField(choices=[('F0', 'Athletic Training'), ('F1', 'Biology'), ('F2', 'Chemistry'), ('F3', 'Phyics'), ('F4', 'Environmental Science'), ('F5', 'Exercise Sci/Kinesiology'), ('F6', 'Fisheries and Wildlife'), ('F7', 'Food Science'), ('F8', 'Forest Management'), ('F9', 'Marine Science'), ('F10', 'Nursing (RN/BSN)'), ('F11', 'Organic/Urban Farming'), ('F12', 'Pharmacy'), ('F13', 'Physicians Assistant'), ('F14', 'Pre - Dental'), ('F15', 'Pre - Medical'), ('F15', 'Pre - Veterinary Medicine'), ('L0', 'Apparel/Textile Design'), ('L1', 'Dance'), ('L2', 'Film/Broadcast'), ('L3', 'Fine/Studio Art'), ('L4', 'Graphic Design'), ('L5', 'Industrial Design'), ('L6', 'Interior Design'), ('L7', 'Landscape Architecture'), ('L8', 'Music'), ('L9', 'Theatre'), ('L10', 'Urban Planning'), ('L11', 'Video Game Design'), ('L12', 'Web Design/Digital Media'), ('A0', 'Arts Management'), ('A1', 'Education'), ('A2', 'Emergency Management'), ('A3', 'English/Writing'), ('A4', 'Equine Science/Mgmt'), ('A5', 'Family & Child Science'), ('A6', 'History'), ('A7', 'Journalism'), ('A8', 'Language Studies'), ('A9', 'Non-Profit Management'), ('A10', 'Parks and Recreation Management'), ('A11', 'Peace/Conflict Studies'), ('A12', 'Philosophy'), ('A13', 'Political Science'), ('A14', 'Psychology / Sociology'), ('A15', 'Sports Turf/Golf Mgmt'), ('A16', 'Women/Gender Studies'), ('I0', 'Aerospace Engineering'), ('I1', 'Astronomy / Physics'), ('I2', 'Aviation/Aeronautics'), ('I3', 'Biomedical Engineering'), ('I4', 'Chemical Engineering'), ('I5', 'Civil Engineering'), ('I6', 'Computer Science'), ('I7', 'Cyber Security'), ('I8', 'Electrical Engineering'), ('I9', 'Energy Science'), ('I10', 'Industrial Engineering'), ('I11', 'Industrial Technology'), ('I12', 'Materials Science'), ('I13', 'Mathematics'), ('I14', 'Mechanical Engineering'), ('R0', 'Accounting - General'), ('R1', 'Business - General'), ('R2', 'Construction Management'), ('R3', 'Data Science - Analytics'), ('R4', 'Economics (National + Global)'), ('R5', 'Finance'), ('R6', 'Hospitality Management'), ('R7', 'Human Resources Mgmt'), ('R8', 'Information Systems (MIS)'), ('R9', 'Insurance & Risk Mgmt'), ('R10', 'Marketing / Advertising'), ('R11', 'Public Health Administration'), ('R12', 'Sport Management'), ('R13', 'Supply Chain Mgmt (Logistics)')], default=None, max_length=1000)),
                ('desc', models.TextField(default=None, verbose_name='Description')),
                ('pos', models.IntegerField(default=1, verbose_name='# of Applicants')),
                ('edu_level', models.CharField(choices=[('N', 'None'), ('L0', 'Middle School (7, 8 Grades)'), ('L1', 'Grade 9 High School'), ('L2', 'Grade 10 High School'), ('L3', 'Grade 11 High School'), ('L4', 'Grade 12 High School'), ('L5', 'First Year Undergraduate'), ('L6', 'Second Year Undergraduate'), ('L7', 'Third Year Undergraduate'), ('L8', 'Fourth Year Undergraduate'), ('L9', 'Five Year or More Undergraduate'), ('L10', 'Graduate Student'), ('L11', 'Vocational Education')], default='None', max_length=1000, verbose_name='Edu level')),
                ('degree', models.CharField(choices=[('N', 'None'), ('L0', 'High School Diploma (or Equivalent)'), ('L1', 'Associate Degree'), ('L2', "Bachelor's Degree"), ('L3', "Master's Degree"), ('L4', 'Doctoral Degree')], default='None', max_length=1000, verbose_name='Degree Type')),
                ('amount', models.IntegerField(default=0, help_text='Enter as the complete amount.', verbose_name='Amount')),
                ('valid_date', models.DateField(default=datetime.date(2021, 3, 17), verbose_name='Deadline')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(default=None, max_length=50, verbose_name='City')),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('DC', 'District of Columbia')], default=None, max_length=1000, verbose_name='State')),
                ('org', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScholarshipApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='SC', max_length=1000, null=True, verbose_name='Application Type')),
                ('cover', models.FileField(blank=True, default=None, null=True, upload_to='resumes', verbose_name='Cover Letter')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Denied'), ('W', 'Wait List')], default='P', max_length=1000, null=True)),
                ('confirm', multiselectfield.db.fields.MultiSelectField(choices=[('Y', 'Yes, I Confirm')], default=None, max_length=1000, verbose_name='Are you sure? Plase Confirm.')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('scholar', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Scholarship')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InternshipApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('IN', 'Internship'), ('SC', 'Scholarship')], default='IN', max_length=1000, verbose_name='Application Type')),
                ('cover', models.FileField(blank=True, default=None, null=True, upload_to='resumes', verbose_name='Cover Letter')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('D', 'Denied'), ('W', 'Wait List')], default='P', max_length=1000, null=True)),
                ('confirm', multiselectfield.db.fields.MultiSelectField(choices=[('Y', 'Yes, I Confirm')], default=None, max_length=1000, verbose_name='Are you sure? Plase Confirm.')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('intern', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Internship')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='External',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default=None, max_length=1000, verbose_name='Host')),
                ('type', models.CharField(choices=[('EIN', 'Internship'), ('ESC', 'Scholarship')], default='SC', max_length=1000, null=True, verbose_name='Opportunity Type')),
                ('title', models.CharField(default=None, max_length=1000, null=True, verbose_name='Title')),
                ('field', models.CharField(choices=[('F0', 'Athletic Training'), ('F1', 'Biology'), ('F2', 'Chemistry'), ('F3', 'Phyics'), ('F4', 'Environmental Science'), ('F5', 'Exercise Sci/Kinesiology'), ('F6', 'Fisheries and Wildlife'), ('F7', 'Food Science'), ('F8', 'Forest Management'), ('F9', 'Marine Science'), ('F10', 'Nursing (RN/BSN)'), ('F11', 'Organic/Urban Farming'), ('F12', 'Pharmacy'), ('F13', 'Physicians Assistant'), ('F14', 'Pre - Dental'), ('F15', 'Pre - Medical'), ('F15', 'Pre - Veterinary Medicine'), ('L0', 'Apparel/Textile Design'), ('L1', 'Dance'), ('L2', 'Film/Broadcast'), ('L3', 'Fine/Studio Art'), ('L4', 'Graphic Design'), ('L5', 'Industrial Design'), ('L6', 'Interior Design'), ('L7', 'Landscape Architecture'), ('L8', 'Music'), ('L9', 'Theatre'), ('L10', 'Urban Planning'), ('L11', 'Video Game Design'), ('L12', 'Web Design/Digital Media'), ('A0', 'Arts Management'), ('A1', 'Education'), ('A2', 'Emergency Management'), ('A3', 'English/Writing'), ('A4', 'Equine Science/Mgmt'), ('A5', 'Family & Child Science'), ('A6', 'History'), ('A7', 'Journalism'), ('A8', 'Language Studies'), ('A9', 'Non-Profit Management'), ('A10', 'Parks and Recreation Management'), ('A11', 'Peace/Conflict Studies'), ('A12', 'Philosophy'), ('A13', 'Political Science'), ('A14', 'Psychology / Sociology'), ('A15', 'Sports Turf/Golf Mgmt'), ('A16', 'Women/Gender Studies'), ('I0', 'Aerospace Engineering'), ('I1', 'Astronomy / Physics'), ('I2', 'Aviation/Aeronautics'), ('I3', 'Biomedical Engineering'), ('I4', 'Chemical Engineering'), ('I5', 'Civil Engineering'), ('I6', 'Computer Science'), ('I7', 'Cyber Security'), ('I8', 'Electrical Engineering'), ('I9', 'Energy Science'), ('I10', 'Industrial Engineering'), ('I11', 'Industrial Technology'), ('I12', 'Materials Science'), ('I13', 'Mathematics'), ('I14', 'Mechanical Engineering'), ('R0', 'Accounting - General'), ('R1', 'Business - General'), ('R2', 'Construction Management'), ('R3', 'Data Science - Analytics'), ('R4', 'Economics (National + Global)'), ('R5', 'Finance'), ('R6', 'Hospitality Management'), ('R7', 'Human Resources Mgmt'), ('R8', 'Information Systems (MIS)'), ('R9', 'Insurance & Risk Mgmt'), ('R10', 'Marketing / Advertising'), ('R11', 'Public Health Administration'), ('R12', 'Sport Management'), ('R13', 'Supply Chain Mgmt (Logistics)')], default=None, max_length=1000)),
                ('link', models.CharField(default='', max_length=5000, null=True, verbose_name='Website Link')),
                ('date_posted', models.DateField(default=datetime.date.today)),
                ('org', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
