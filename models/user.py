#!/usr/bin/env python3
"""Class User inheriting from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Class user inheriting from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
