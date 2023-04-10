"""
  docstring
"""

import mysql.connector
from decouple import config

db = mysql.connector.connect(
  host=config("host"),
  user= config("user"),
  password= config("password"),
  database=config("database")
)
