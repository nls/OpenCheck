from appengine_django.models import BaseModel
from google.appengine.ext import db
from site_settings.models import Establishment

class Order(BaseModel):
    #user = db.ReferenceProperty(User, required=True)
    ordered_at = db.DateTimeProperty(required=True)
    status = db.StringProperty(required=True, choices=["PENDING", "ACCEPTED", "COMPLETED", "SERVED"])
    completed_at = db.DateTimeProperty()

class MenuCategory(BaseModel):
    title = db.StringProperty(required=True)
    establishment = db.ReferenceProperty(Establishment, required=True)

class MenuItem(BaseModel):
    title = db.StringProperty(required=True)
    price = db.FloatProperty(required=True)
    currency = db.StringProperty(required=True, choices=["MXN", "USD", "RMB"])
    menu_category = db.ReferenceProperty(MenuCategory)

class OrderItem(BaseModel):
    menu_item = db.ReferenceProperty(MenuItem, required=True)
    order = db.ReferenceProperty(Order, required=True)
    price = db.FloatProperty(required=True)
    notes = db.StringProperty()

class EstablishmentRating(BaseModel):
    establishment = db.ReferenceProperty(Establishment, required=True)
    rating = db.RatingProperty(required=True)
    #user = db.ReferenceProperty(User, required=True)
    comment = db.StringProperty()

class OrderNote(BaseModel):
    order = db.ReferenceProperty(Order, required=True)
    note = db.StringProperty(required=True)
    #user = db.ReferenceProperty(User, required=True)

class MenuItemRating(BaseModel):
    menu_item = db.ReferenceProperty(MenuItem, required=True)
    rating = db.RatingProperty(required=True)
    #user = db.ReferenceProperty(User, required=True)
    comment = db.StringProperty()
