from django.db import migrations


class Migration(migrations.Migration):
    # CRITICAL: This allows Postgres to create the index concurrently
    atomic = False 

    dependencies = [
        ('base', '0081_alter_resourcebase_alternate'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            # Updates Django's internal state tracking
            state_operations=[],
            # Runs the background, non-blocking raw SQL execution
            database_operations=[
                migrations.RunSQL(
                    sql='CREATE INDEX CONCURRENTLY base_resourcebase_alternate_idx ON base_resourcebase (alternate);',
                    reverse_sql='DROP INDEX CONCURRENTLY base_resourcebase_alternate_idx;'
                ),
            ],
        ),
    ]
