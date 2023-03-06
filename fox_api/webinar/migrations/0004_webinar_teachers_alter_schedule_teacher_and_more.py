# Generated by Django 4.1.7 on 2023-03-05 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webinar', '0003_alter_schedule_teacher_alter_schedule_webinar'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='teachers',
            field=models.ManyToManyField(through='webinar.Schedule', to='webinar.teacher'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webinar.teacher'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='webinar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webinar.webinar'),
        ),
    ]
