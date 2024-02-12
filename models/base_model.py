import uuid
from datetime import datetime


class BaseModel:

    """BaseModel class serves as the base for other classes in the application.


Attributes:
id (str): A unique identifier for each instance generated using uuid.uuid4().
created-at (datetime): The datetime when the instance is created.
updated_at (datetime): The datetime when the instance is last updated.

Methods:
__init__: Initializes a new instance of the BaseModel class.
__str__: Returns a string representation of the object.
save: Updates the 'updated_at'attribute with the current datetime
to_dict: Returns a dictionary representation of the object.
"""


def __init__(self):
    """Initializes a new instance of the BaseModel class."""
    self.id = str(uuid.uuid4())  # Generate a unique ID for the instance as str
    self.created_at = datetime.now()  # Record creation time
    self.updated_at = datetime.now()  # Record last update time


def __str__(self):
    """Returns a string representation of the object"""
    return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)


def save(self):
    """Updates the 'updated_at' attribute with the current datetime."""
    self.updated_at = datetime.now()


def to_dict(self):
    """Returns a dictionary representation of the object
    Returns:
    dict: A dictionary containing all keys/values of the instance's attributes,
    including 'id', 'created_at', 'updated_at', and '__class__'
    'The created_at' and 'updated_at' values are converted
    to ISO format strings.
    """
    obj_dict = self.__dict__.copy()
    obj_dict['__class__'] = self.__class__.__name__  # Add class name to dict
    obj_dict['created_at'] = self.created_at.isoformat()  # Convert t to ISO
    obj_dict['updated_at'] = self.updated_at.isoformat()  # Convert t to ISO
    return obj_dict
