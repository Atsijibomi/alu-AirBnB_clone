#!/usr/bin/python
"""State class"""

from models.base_model import BaseModel


class User(BaseModel):
	"""State class"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""
