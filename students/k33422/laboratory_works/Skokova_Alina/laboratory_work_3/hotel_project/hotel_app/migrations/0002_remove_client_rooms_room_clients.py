# Generated by Django 4.1.2 on 2023-03-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotel_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="rooms",
        ),
        migrations.AddField(
            model_name="room",
            name="clients",
            field=models.ManyToManyField(
                related_name="client_room",
                through="hotel_app.Booking",
                to="hotel_app.client",
                verbose_name="Клиенты",
            ),
        ),
    ]