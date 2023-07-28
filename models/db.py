import os
from peewee import SqliteDatabase, PostgresqlDatabase
#db = SqliteDatabase('db.sqlite')
db = PostgresqlDatabase(os.environ.get("DB_NAME"), user=os.environ.get("BD_USER"), password=os.environ.get("BD_PASSWORD"),
                        host=os.environ.get("BD_HOST"), port=5432)