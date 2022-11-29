# Generated by Django 4.1.3 on 2022-11-28 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="is_staff", new_name="is_admin",
        ),
        migrations.RemoveField(model_name="user", name="groups",),
        migrations.RemoveField(model_name="user", name="is_superuser",),
        migrations.RemoveField(model_name="user", name="user_permissions",),
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.IntegerField(
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="login_id",
            field=models.CharField(default="", max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="user",
            name="phone_number",
            field=models.CharField(default="", max_length=12),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="", max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
