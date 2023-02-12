#!/usr/bin/env python3
"""Class review"""

from models.base_models import BaseModel

class Review(BaseModel):
    """Representation of class Review"""
    place_id = ""
    user_id = ""
    text = ""
