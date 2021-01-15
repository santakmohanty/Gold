import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, MetaData
from sqlalchemy import pool

# BASE_DIR = 'src/apps/main/migrations'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 'src/apps '
APPS_PATH = os.path.join(BASE_DIR, '..', '..')
sys.path.append(APPS_PATH)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.


# Important
# Update the below line and import the model by name
from apps.main.models import demo_user_model

from gold import settings

config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)



# SQLALCHEMY_URL = "postgresql+psycopg2://archita:archita@localhost/mirror"
DATABASE_NAME = settings.DATABASES['default']['NAME']
DB_USERNAME = settings.DATABASES['default']['USER']
DB_PASSWORD = settings.DATABASES['default']['PASSWORD']
DB_HOST = settings.DATABASES['default']['HOST']

SQLALCHEMY_URL = "postgresql+psycopg2://" + DB_USERNAME + ":" + DB_PASSWORD + '@' + DB_HOST + '/' + DATABASE_NAME

# SET "alembic.ini" file's sqlalchemy.url to SQLALCHEMY_URL from config.yml
config.set_main_option('sqlalchemy.url', SQLALCHEMY_URL)


def combine_metadata(*args):
    m = MetaData()
    for metadata in args:
        for t in metadata.tables.values():
            t.tometadata(m)
    return m


# IMPORTANT
# put comma seperated model.BaseModel.metadata in combine_metadata() for alembic to make migrations
# demo value is put, replace this with your model
target_metadata = combine_metadata(demo_user_model.BaseModel.metadata)


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url = url, target_metadata = target_metadata, literal_binds = True,
        compare_type = True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix = "sqlalchemy.",
        poolclass = pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection = connection,
            target_metadata = target_metadata,
            compare_type = True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
