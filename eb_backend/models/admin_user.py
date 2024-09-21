#!/usr/bin/python3
"""Module for AdminUser model for database representation"""
from sqlalchemy import Column, String

from . import Base, BaseModel


class AdminUser(BaseModel, Base):
    """AdminUser model class with fields"""
    __tablename__ = 'admin_users'
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
