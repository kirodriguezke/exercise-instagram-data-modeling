import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
   
    id = Column(Integer, primary_key=True)
    first_name = Column(String(60))
    last_name = Column(String(100))
    nickname = Column(String(30), nullable=False, unique= True)
    email = Column(String(100), nullable=False, unique= True)
    password = Column(String(25), nullable=False)
    gender = Column(String(10), nullable=False)

    
    followers = relationship("Followers")
    like = relationship("Likes")
    comment = relationship("Comments")

class Posts(Base):
    __tablename__ = 'posts'
   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text = Column(String(10000), nullable=False)
    image = Column(String(350), nullable=False)
    
    
    user = relationship("Users")
    comments = relationship("Comments")
    likes = relationship("Likes")


class Comments(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    text = Column(String(10000), nullable=False)
    

    user = relationship("Users")
    post = relationship("Posts")
    

class Followers(Base):
    __tablename__ = 'followers'
   
    id = Column(Integer, primary_key=True)
    user_id_from = Column(Integer, ForeignKey('users.id'))
    user_id_to = Column(Integer, ForeignKey('users.id'))

    user = relationship("Users")


class Likes(Base):
    __tablename__ = 'likes'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    user = relationship("Users")
    post = relationship("Posts")
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')