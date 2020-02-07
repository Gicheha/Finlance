# Generated by Django 3.0.2 on 2020-01-25 22:16

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=30)),
                ('contact_person_name', models.CharField(max_length=64)),
                ('company_size', models.CharField(choices=[('', 'Company Size'), ('1-10 employees', '1-10 employees'), ('11-50 employees', '11-50 employees'), ('51-200 employees', '51-200 employees'), ('201-500 employees', '201-500 employees'), ('501-1,000 employees', '501-1,000 employees'), ('5,001-10,000 employees', '5,001-10,000 employees'), ('10,001 or more employees', '10,001 or more employees')], max_length=50)),
                ('country', models.CharField(default='Kenya', max_length=64)),
                ('business_description', ckeditor.fields.RichTextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=164)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, max_length=200, null=True, populate_from='title', unique=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('employment_type', models.CharField(choices=[('', 'Choose Employment Type'), ('FULL_TIME', 'Full Time'), ('PART_TIME', 'Part Time'), ('CONTRACTOR', 'Contractor'), ('TEMPORARY', 'Temporary'), ('INTERN', 'Intern'), ('VOLUNTEER', 'Volunteer'), ('PER_DIEM', 'Per Diem')], max_length=64)),
                ('experience', models.IntegerField(blank=True, null=True)),
                ('job_location', models.CharField(default='Nairobi', max_length=64)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('valid_through', models.DateField()),
                ('education_level', models.CharField(choices=[('PRIMARY_EDUCATION', 'Primary Education'), ('LOWER_SECONDARY_EDUCATION', 'Lower Secondary Education'), ('UPPER_SECONDARY_EDUCATION', 'Upper Secondary Education'), ('ASSOCIATES_OR_EQUIVALENT', 'Associates or Equivalent'), ('BACHELORS_OR_EQUIVALENT', 'Bachelors or Equivalent'), ('MASTERS_OR_EQUIVALENT', 'Masters or Equivalent'), ('DOCTORAL_OR_EQUIVALENT', 'Doctoral or Equivalent'), ('DEGREE_TYPE_UNSPECIFIED', 'Unspecified')], default='DEGREE_TYPE_UNSPECIFIED', max_length=200)),
                ('job_level', models.CharField(choices=[('ENTRY_LEVEL', 'Entry Level'), ('EXPERIENCED', 'Experienced'), ('MANAGER', 'Manager'), ('DIRECTOR', 'Director'), ('EXECUTIVE', 'Executive'), ('JOB_LEVEL_UNSPECIFIED', 'Unspecified')], default='JOB_LEVEL_UNSPECIFIED', max_length=200)),
                ('category', models.CharField(choices=[('Auditing', 'Auditing and Forensics'), ('Tax', 'Tax management and policy'), ('Book keeping', 'Financial records and reporting'), ('Financial Modelling', 'Financial Modelling'), ('Data Analysis', 'Data analysis and modeling')], max_length=200)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('hiring_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]
