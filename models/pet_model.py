from peewee import ForeignKeyField, CharField, Model
from models.db import db
from models.person_model import Person

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db