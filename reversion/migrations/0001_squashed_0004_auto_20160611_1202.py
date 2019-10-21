# Generated by Django 1.9.7 on 2016-06-06 13:22
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(db_index=True, help_text='The date and time this revision was created.', verbose_name='date created')),
                ('comment', models.TextField(blank=True, help_text='A text comment on this revision.', verbose_name='comment')),
                ('user', models.ForeignKey(blank=True, help_text='The user who created this revision.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                "ordering": ("-pk",)
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.CharField(help_text='Primary key of the model under version control.', max_length=191)),
                ('format', models.CharField(help_text='The serialization format used by this model.', max_length=255)),
                ('serialized_data', models.TextField(help_text='The serialized form of this version of the model.')),
                ('object_repr', models.TextField(help_text='A string representation of the object.')),
                ('content_type', models.ForeignKey(help_text='Content type of the model under version control.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('revision', models.ForeignKey(help_text='The revision that contains this version.', on_delete=django.db.models.deletion.CASCADE, to='reversion.Revision')),
                ('db', models.CharField(help_text='The database the model under version control is stored in.', max_length=191)),
            ],
            options={
                "ordering": ("-pk",)
            },
        ),
        migrations.AlterUniqueTogether(
            name='version',
            unique_together=set([('db', 'content_type', 'object_id', 'revision')]),
        ),
    ]
