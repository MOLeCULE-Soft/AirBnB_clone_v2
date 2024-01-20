#!/usr/bin/python3
"""State class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import storage


class State(BaseModel, Base):
    """State class implementation"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        return [val for key, val in storage.all()
                if key.split('.')[0] == 'City'
                and val.state_id == self.id]
