from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, Integer, CHAR, TEXT

Base = declarative_base()


class Books(Base):
  __tablename__ = 'books'
    
  id = Column(Integer, autoincrement=True, primary_key=True)  
  book_id = Column(CHAR(36), nullable=False, unique=True, comment='书籍ID，使用GUID')  
  book_title = Column(VARCHAR(255), nullable=False, comment='书籍名')  
  author_id = Column(CHAR(36), nullable=False, comment='作者ID，关联author表')  
  book_description = Column(TEXT, comment='书籍描述')  
  book_url = Column(VARCHAR(255), nullable=False, comment='书籍地址')  
  cover_image_path = Column(VARCHAR(255), comment='封面图路径')  
  chapter_title = Column(VARCHAR(255), comment='最后章节名称')  

  def __init__(self, book_id, book_title, author_id, book_description,book_url, cover_image_path, chapter_title):
      self.book_id = book_id
      self.book_title = book_title
      self.author_id = author_id
      self.book_description = book_description
      self.book_url = book_url
      self.cover_image_path = cover_image_path
      self.chapter_title = chapter_title
