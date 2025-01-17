# Generated by Django 4.1.7 on 2023-03-15 09:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id_booking", models.AutoField(primary_key=True, serialize=False)),
                ("date_start", models.DateField(verbose_name="Дата поселения")),
                (
                    "date_end",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата выселения"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cleaner",
            fields=[
                ("id_cleaner", models.AutoField(primary_key=True, serialize=False)),
                (
                    "last_name_cleaner",
                    models.CharField(max_length=120, verbose_name="Фамилия служащего"),
                ),
                (
                    "first_name_cleaner",
                    models.CharField(max_length=120, verbose_name="Имя служащего"),
                ),
                (
                    "patronymic_cleaner",
                    models.CharField(max_length=120, verbose_name="Отчество служащего"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "passport",
                    models.CharField(
                        max_length=10,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Номер паспорта",
                    ),
                ),
                (
                    "last_name_client",
                    models.CharField(
                        max_length=120, verbose_name="Фамилия проживающего"
                    ),
                ),
                (
                    "first_name_client",
                    models.CharField(max_length=120, verbose_name="Имя проживающего"),
                ),
                (
                    "patronymic_client",
                    models.CharField(
                        max_length=120, verbose_name="Отчество проживающего"
                    ),
                ),
                ("city", models.CharField(max_length=120, verbose_name="Родной город")),
            ],
        ),
        migrations.CreateModel(
            name="Floor",
            fields=[
                ("id_floor", models.AutoField(primary_key=True, serialize=False)),
                ("floor_num", models.IntegerField(verbose_name="Этаж")),
            ],
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                ("id_price", models.AutoField(primary_key=True, serialize=False)),
                (
                    "room_type",
                    models.CharField(
                        choices=[("s", "single"), ("d", "double"), ("t", "triple")],
                        max_length=1,
                        verbose_name="Тип номера",
                    ),
                ),
                ("price_daily", models.FloatField(verbose_name="Стоимость за сутки")),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                ("id_schedule", models.AutoField(primary_key=True, serialize=False)),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("mon", "monday"),
                            ("tue", "tuesday"),
                            ("wed", "wednesday"),
                            ("thu", "thursday"),
                            ("fri", "friday"),
                            ("sat", "saturday"),
                            ("sun", "sunday"),
                        ],
                        max_length=3,
                        verbose_name="День недели",
                    ),
                ),
                (
                    "id_cleaner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms_app.cleaner",
                        verbose_name="Служащий",
                    ),
                ),
                (
                    "id_floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms_app.floor",
                        verbose_name="Этаж для уборки",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                ("id_room", models.AutoField(primary_key=True, serialize=False)),
                (
                    "phone",
                    models.CharField(max_length=7, verbose_name="Номер телефона"),
                ),
                (
                    "clients",
                    models.ManyToManyField(
                        related_name="client_room",
                        through="rooms_app.Booking",
                        to="rooms_app.client",
                        verbose_name="Клиенты",
                    ),
                ),
                (
                    "id_floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms_app.floor",
                        verbose_name="Этаж",
                    ),
                ),
                (
                    "room_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms_app.price",
                        verbose_name="Тип номера",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cleaner",
            name="floors",
            field=models.ManyToManyField(
                related_name="floor_cleaner",
                through="rooms_app.Schedule",
                to="rooms_app.floor",
                verbose_name="Обслуживаемые этажи",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="id_client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="rooms_app.client",
                verbose_name="Проживающий",
            ),
        ),
        migrations.AddField(
            model_name="booking",
            name="id_room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="rooms_app.room",
                verbose_name="Выделенный номер",
            ),
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "tel",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="Телефон"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
