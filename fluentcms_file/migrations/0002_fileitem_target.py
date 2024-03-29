from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fluentcms_file", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fileitem",
            name="target",
            field=models.CharField(
                default=b"",
                max_length=100,
                verbose_name="target",
                blank=True,
                choices=[
                    (b"", "same window"),
                    (b"_blank", "new window"),
                    (b"_parent", "parent window"),
                    (b"_top", "topmost frame"),
                ],
            ),
        ),
    ]
