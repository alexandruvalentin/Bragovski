# Generated by Django 3.2.7 on 2021-10-26 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testimonials', '0003_alter_testimonials_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to=settings.AUTH_USER_MODEL),
        ),
    ]
