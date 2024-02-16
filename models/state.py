#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        """represent a relationship with the class City"""
        if models.storage_type == "db":
            return self.cities

        else:
            city_list = []
            for city in models.storage.all(city).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
