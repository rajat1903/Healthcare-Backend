
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mappings', '0001_initial'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdoctormapping',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
        migrations.AlterUniqueTogether(
            name='patientdoctormapping',
            unique_together={('patient', 'doctor')},
        ),
    ]
