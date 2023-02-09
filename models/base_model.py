#!/usr/bin/python3

import uuid
from datetime import datetime, time, date


class BaseModel:
    """Define the class BaseModel that defines attributes id,
    created_at, updated_at and methods
    """
    
    def __init__(self):
        """Initialize the class BaseModel attributes{id, created_at
        and updated_at}
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a str representation of the class"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")



