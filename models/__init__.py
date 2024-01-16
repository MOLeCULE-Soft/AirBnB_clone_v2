#!/usr/bin/python3
"""Initialization of AirBnB console"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
