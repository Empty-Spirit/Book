from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR

Base = declarative_base()


class Books(Base):
  __tablename__ = 'collect'
    
  guid = Column(VARCHAR(255), primary_key=True)
  name = Column(VARCHAR(255))
  author = Column(VARCHAR(255))
  last_chapter = Column(VARCHAR(255))
  url = Column(VARCHAR(255))

  def __init__(self, guid, name, author, last_chapter, url):
      self.guid = guid
      self.name = name
      self.author = author
      self.last_chapter = last_chapter
      self.url = url
