# Generated by Django 4.1.3 on 2022-11-28 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseball', '0003_club_team_pic_alter_play_team_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team', to='baseball.person'),
        ),
    ]
