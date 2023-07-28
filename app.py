from flask import Flask, request
from models.db import db
from models.person_model import Person
from models.pet_model import Pet

db.create_tables([Person, Pet])

app = Flask(__name__)

@app.route("/people", methods=["POST"])
def create_person():
    request_json = request.get_json()
    # name = request_json.get("name")
    # birthday = request_json.get("birthday")
    # p = Person.create(name=name, birthday=birthday)
    # **{"hola":"mundo", "age":12} = hola="mundo", age=12
    
    p = Person.create(**request_json)
    return p.__dict__.get("__data__"), 201

@app.route("/people", methods=["GET"])
def read_all_person():
    return list(Person.select().dicts()), 200

@app.route("/people/<id>", methods=["GET"])
def read_person(id):
    person = Person.select().where(Person.id==id).get()
    return person.__dict__.get("__data__"), 200

@app.route("/people/<id>", methods=["PUT"])
def update_person(id):
    request_json = request.get_json()
    person = Person.select().where(Person.id==id).get()
    person.name = request_json.get("name")
    person.birthday = request_json.get("birthday")
    person.save()
    return person.__dict__.get("__data__"), 200

@app.route("/people/<id>", methods=["DELETE"])
def delete_person(id):
    person = Person.select().where(Person.id==id).get()
    person.delete_instance()
    return {"id":id}, 200

@app.route("/pets", methods=["GET", "POST"])
def create_read_all_pets():
    if request.method == "GET":
        return list(Pet.select().dicts()), 200
    if request.method == "POST":
        request_json = request.get_json()
        person = Person.select().where(Person.id==request_json.get("owner")).get()
        pet = Pet.create(owner=person, name=request.get_json().get("name"), animal_type=request.get_json().get("animal_type"))
        return pet.__dict__.get("__data__"), 201

@app.route("/pets/<id>", methods=["GET", "PUT", "DELETE"])
def read_update_delete_pets(id):
    if request.method == "GET":
        pass
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        pass

@app.route("/people/<id>/pets", methods=["GET"])
def read_all_pets_of_person(id):
    pets = list(Pet.select().where(Pet.owner==id).dicts())
    return pets, 200
