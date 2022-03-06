from unicodedata import name
from app import db

from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, Float


class Photo(db.Model):
    __tablename__ = 'Photo'
    key = Column(String(100), primary_key=True, index=True) # build index for photo name, speed up querying
    address = Column(Text)

    def __repr__(self):
        return "<Photo %r>" % self.key


class Cache(db.Model):
    __tablename__ = 'Cache'
    name = Column(String(10), default="local", primary_key=True)
    capacity = Column(Integer, default=30)
    policy = Column(String(10), default="lru")
    
    def __repr__(self):
        return "<Cache %r>" % self.capacity

class Statistics(db.Model):
    __tablename__ = 'Statistics'
    time = Column(String(100), primary_key=True)
    number = Column(Integer)
    size = Column(String(20))
    requests = Column(Integer)
    hitRate = Column(Float)
    missRate = Column(Float)

    def __repr__(self):
        return "<Statistics %r>" % self.time