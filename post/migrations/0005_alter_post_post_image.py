# Generated by Django 4.1.1 on 2023-03-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0004_post_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_image",
            field=models.ImageField(blank=True, null=True, upload_to="photo/"),
        ),
    ]
