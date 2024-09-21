#!/usr/bin/python3
"""Module for Borrow model for database representation"""
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from . import Base, BaseModel


class Borrow(BaseModel, Base):
    """Borrow model class with fields"""
    __tablename__ = 'borrows'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    book_id = Column(Integer, ForeignKey('books.id', ondelete='CASCADE'),
                     nullable=False)
    borrow_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)
    book = relationship('Book', backref='borrow_records')
