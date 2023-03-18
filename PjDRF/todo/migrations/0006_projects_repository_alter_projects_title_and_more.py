# Generated by Django 4.1.3 on 2023-02-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_proj'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='repository',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='body',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_complete',
            field=models.BooleanField(default=True, verbose_name='Завершено'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='proj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todo.projects'),
            preserve_default=False,
        ),
    ]