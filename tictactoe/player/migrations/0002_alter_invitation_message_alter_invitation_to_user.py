# Generated by Django 4.2.8 on 2023-12-12 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitation",
            name="message",
            field=models.CharField(
                help_text="It's always nice to add some friendly message!",
                max_length=300,
                verbose_name="Optional Message",
            ),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="to_user",
            field=models.ForeignKey(
                help_text="Please select the suer you want to play a game with.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invitations_received",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User to invite",
            ),
        ),
    ]
