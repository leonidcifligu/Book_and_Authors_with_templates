# Generated by Django 2.2 on 2021-04-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_and_authors_app.Book'),
        ),
    ]
