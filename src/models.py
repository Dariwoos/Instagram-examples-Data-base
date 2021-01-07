import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250),nullable=False)


class Post(Base):
    __tablename__ = 'posts'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description= Column(String(250) , nullable=True)
    image_url= Column(String(250))
    user_id = Column(Integer, ForeignKey('users.id'))
    useer = relationship (User)
    comment_id = Column(Integer, ForeignKey('comments.id'))
    comments = relationship("Comment", backref="post")
   

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer,primary_key=True)
    length= Column(String(250))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)



class Follwoers(Base):
    __tablename__ = 'Followers'
    id= Column(Integer, primary_key=True)
    Followed = Column(Integer, ForeignKey('users.id'))
    Following = Column(Integer, ForeignKey('users.id'))
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')