#!/usr/bin/python3
"""Module for User Model for database representation"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from . import Base, BaseModel


class User(BaseModel, Base):
    """User model class with fields"""
    __tablename__ = 'users'
    email = Column(String(100), nullable=False, unique=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    borrowed_books = relationship('Borrow', backref='user',
                                  cascade='all, delete, delete-orphan',)
