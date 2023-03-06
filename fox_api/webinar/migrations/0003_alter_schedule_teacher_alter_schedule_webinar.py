# Generated by Django 4.1.7 on 2023-03-05 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0002_remove_teacher_webinars_remove_webinar_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webinars', to='webinar.teacher'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='webinar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='webinar.webinar'),
        ),
    ]
