

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('specialization', models.CharField(choices=[('GP', 'General Practitioner'), ('CARD', 'Cardiologist'), ('NEURO', 'Neurologist'), ('PED', 'Pediatrician'), ('DERM', 'Dermatologist'), ('ORTHO', 'Orthopedist'), ('PSYCH', 'Psychiatrist'), ('OTHER', 'Other')], max_length=5)),
                ('license_number', models.CharField(max_length=50, unique=True)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
