
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='isread',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
