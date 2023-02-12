#!/usr/bin/python3
"""A base class with common methods/attributes for other classes"""

import uuid
from datetime import datetime, time, date


class BaseModel:
    """Define the class BaseModel that defines attributes id,
    created_at, updated_at and methods
    """
    def __init__(self, *args, **kwargs):
        """Initialize the class BaseModel attributes{id, created_at
        and updated_at}
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """Returns a str representation of the class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update the updated_at attr"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance"""
        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
