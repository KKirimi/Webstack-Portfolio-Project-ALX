#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    """BaseModel class serves as the base for other classes in the application.


Attributes:
id (str): A unique identifier for each instance generated using uuid.uuid4().
created_at (datetime): The datetime when the instance is created.
updated_at (datetime): The datetime when the instance is last updated.

Methods:
__init__: Initializes a new instance of the BaseModel class.
__str__: Returns a string representation of the object.
save: Updates the 'updated_at'attribute with the current datetime
to_dict: Returns a dictionary representation of the object.
"""


def __init__(self, *args, **kwargs):
    """Public instance artributes initialization after creation"""


if kwargs:
    for key, value in kwargs.items():
        if key != "__class__":
            setattr(self, key, value)
        if kwargs.get("created_at", None) and type(self.created_at) is str:
            self.created_at = datetime.strptime(kwargs["created_at"])
        else:
            self.created_at = datetime.utcnow()
        if kwargs.get("updated_at", None) and type(self.updated_at) is str:
            self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.updated_at = datetime.utcnow()
        if kwargs.get("id", None) is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at


def __str__(self):
    """Returns a string representation of the object"""
    return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)


def save(self):
    """Updates the 'updated_at' attribute with the current datetime."""
    self.updated_at = datetime.utcnow()
    models.storage.new(self)
    models.storage.save()


def to_dict(self):
    """Returns a dictionary representation of the object
    Returns:
    dict: A dictionary containing all keys/values of the instance's attributes,
    including 'id', 'created_at', 'updated_at', and '__class__'
    'The created_at' and 'updated_at' values are converted
    to ISO format strings.
    """


obj_dict = self.__dict__.copy()
if "created_at" in obj_dict:
    obj_dict['created_at'] = obj_dict['created_at'].strftime(time)
if "updated_at" in obj_dict:
    obj_dict['updated_at'] = obj_dict['updated_at'].strftime(time)
obj_dict["__class__"] = self.__class__.__name__
return obj_dict
