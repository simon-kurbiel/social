from .database import Base
from sqlalchemy import Column, Integer, String,Boolean,TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    title = Column(String(50), nullable=False)
    content=Column(String(144), nullable=False)
    published=Column(Boolean, server_default='1',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    user_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    owner = relationship("User")
    
    
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(100),nullable=False, unique=True)
    password=Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    


# on 9:42