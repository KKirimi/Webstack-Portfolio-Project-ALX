#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models


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


DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'


def __init__(self, *args, **kwargs):
    """Public instance artributes initialization after creation"""


if kwargs:
    for key, value in kwargs.items():
        if key == 'created_at' or key == 'updated_at':
            setattr(self, key, datetime.strptime(value, self.DATE_TIME_FORMAT))
    else:
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


def __str__(self):
    """Returns a string representation of the object"""
    return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)


def save(self):
    """Updates the 'updated_at' attribute with the current datetime."""
    self.updated_at = datetime.utcnow()


def to_dict(self):
    """Returns a dictionary representation of the object
    Returns:
    dict: A dictionary containing all keys/values of the instance's attributes,
    including 'id', 'created_at', 'updated_at', and '__class__'
    'The created_at' and 'updated_at' values are converted
    to ISO format strings.
    """


obj_dict = self.__dict__.copy()
obj_dict['created_at'] = obj_dict['created_at'].strftime(self.DATE_TIME_FORMAT)
obj_dict['updated_at'] = obj_dict['updated_at'].strftime(self.DATE_TIME_FORMAT)
obj_dict["__class__"] = self.__class__.__name__
return obj_dict
