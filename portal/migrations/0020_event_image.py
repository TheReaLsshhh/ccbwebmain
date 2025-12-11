# Generated migration for adding image field to Event model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_institutionalinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, help_text='Event image', null=True, upload_to='events/'),
        ),
    ]

