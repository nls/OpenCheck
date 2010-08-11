from appengine_django.models import BaseModel
from google.appengine.ext import db

class Country(BaseModel):
    name = db.StringProperty(required=True)

class State(BaseModel):
    name = db.StringProperty(required=True)
    country = db.ReferenceProperty(Country, required=True)

class City(BaseModel):
    name = db.StringProperty(required=True)
    state = db.ReferenceProperty(State, required=True)

class Address(BaseModel):
    line_1 = db.StringProperty(required=True)
    line_2 = db.StringProperty()
    line_3 = db.StringProperty()
    postal_code = db.StringProperty()
    coordinates = db.GeoPtProperty()
    city = db.ReferenceProperty(City, required=True)

class EstablishmentCategory(BaseModel):
    title = db.StringProperty(required=True)
    description = db.StringProperty()

class Establishment(BaseModel):
    name = db.StringProperty(required=True)
    address = db.ReferenceProperty(Address, required=True)
    phone = db.StringProperty()
    description = db.StringProperty()
    establishment_category = db.ReferenceProperty(EstablishmentCategory)
