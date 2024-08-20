from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, Integer, CHAR, TEXT, Index

Base = declarative_base()


class Books(Base):
  __tablename__ = 'books'
    
  id = Column(Integer, autoincrement=True, primary_key=True)  
  book_id = Column(CHAR(36), nullable=False, unique=True, comment='书籍ID，使用GUID')  
  book_title = Column(VARCHAR(255), nullable=False, comment='书籍名')  
  author_name = Column(CHAR(36), nullable=False, comment='作者名称')  
  book_description = Column(TEXT, comment='书籍描述')  
  book_url = Column(VARCHAR(255), nullable=False, comment='书籍地址')  
  cover_image_path = Column(VARCHAR(255), comment='封面图路径')  
  chapter_title = Column(VARCHAR(255), comment='最后章节名称')  

  def __init__(self, book_id, book_title, author_name, book_description,book_url, cover_image_path, chapter_title):
      self.book_id = book_id
      self.book_title = book_title
      self.author_name = author_name
      self.book_description = book_description
      self.book_url = book_url
      self.cover_image_path = cover_image_path
      self.chapter_title = chapter_title

class Authors(Base):  
    __tablename__ = 'authors'  
  
    id = Column(Integer, autoincrement=True, primary_key=True)  # 注意：在SQLAlchemy中，通常使用autoincrement=True的简写形式为autoincrement=True（尽管在某些情况下可以省略）  
    author_id = Column(CHAR(36), nullable=False, unique=True, comment='作者ID，使用GUID')  
    author_name = Column(VARCHAR(255), nullable=False, comment='作者名')  
  
    def __init__(self, author_id, author_name):  
        self.author_id = author_id  
        self.author_name = author_name

class Chapters(Base):  
    __tablename__ = 'chapters'  
  
    id = Column(Integer, autoincrement=True, primary_key=True)  
    chapter_id = Column(CHAR(36), nullable=False, unique=True, comment='章节ID，使用GUID')  
    book_id = Column(CHAR(36), nullable=False, comment='书籍ID，关联books表')  
    chapter_title = Column(VARCHAR(255), nullable=False, comment='章节名称')  
    chapter_content = Column(TEXT, comment='章节内容')  
    pre_chapter_id = Column(CHAR(36), nullable=False, comment='上一章书籍ID') 
    last_chapter_id = Column(CHAR(36), nullable=False, comment='下一章书籍ID') 
  
    # 复合索引  
    __table_args__ = (  
        Index('idx_book_chapter', 'book_id', 'chapter_id'),  
    )  
  
    # 如果需要，可以在这里定义与书籍表的关系（假设有一个Books类）  
    # book = relationship("Books", back_populates="chapters")  # 注意：这需要在Books类中也有相应的设置  
  
    def __init__(self, chapter_id, book_id, chapter_title, chapter_content, pre_chapter_id, last_chapter_id):  
        self.chapter_id = chapter_id  
        self.book_id = book_id  
        self.chapter_title = chapter_title  
        self.chapter_content = chapter_content 
        self.pre_chapter_id = pre_chapter_id 
        self.last_chapter_id = last_chapter_id 
