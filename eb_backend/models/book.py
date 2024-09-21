#!/usr/bin/python3
"""Module for Book model for database representation"""
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.sql import func

from . import Base, BaseModel, create_tsvector


class Book(BaseModel, Base):
    """Book model class with fields and full-text search vectors"""
    __tablename__ = 'books'
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    publisher = Column(String(100), nullable=False)
    available = Column(Boolean, default=True)
    due_date = Column(DateTime, nullable=True)
    search_vector = create_tsvector('title', 'author', 'publisher', 'category')
