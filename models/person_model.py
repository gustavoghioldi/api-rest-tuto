from peewee import CharField, DateField, Model
from models.db import db

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.