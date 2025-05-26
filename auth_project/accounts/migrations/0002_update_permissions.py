from django.db import migrations

def create_custom_permissions(apps, schema_editor):
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from accounts.models import BlogPost

    content_type = ContentType.objects.get_for_model(BlogPost)
    Permission.objects.get_or_create(
        codename='can_publish',
        name='Can Publish Posts',
        content_type=content_type,
    )

class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_custom_permissions),
    ]
