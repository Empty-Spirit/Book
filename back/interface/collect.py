# from db import conn
# 使用sqlalchemy连接数据库
from utils import result
from db.engine import engine
from flask import request
from sqlalchemy.orm import sessionmaker
from conf.models import Books
from conf.crud import add, update, delete, search, check_only
from utils.packfunc import getUUid, check_valid_guid

DBSession = sessionmaker(bind=engine)
session = DBSession()


def collect(app):
    @app.route('/search')
    def searchs():
        form = request.args
        guid = form.get('guid')

        if guid:
            sql = f"SELECT * FROM collect Where guid = '{guid}'"
        else:
            sql = f"SELECT * FROM collect"

        return search(sql)

    @app.route('/add', methods=['POST'])
    def adds():
        data = request.get_json()  
        guid = check_valid_guid(data)  
    
        if not guid:  
            guid = getUUid()  # 如果没有提供guid，则生成一个新的  
    
        if check_only('book_id', guid):  # 注意这里我们使用'book_id'而不是'guid'，因为字段名是book_id  
            return result.error('guid is exist')  # 这里可能需要根据实际情况调整错误信息  
    
        # 验证data中是否包含所有必要的字段  
        required_fields = {'book_title', 'author_id', 'book_description', 'book_url', 'cover_image_path', 'chapter_title'}  
        if not required_fields.issubset(data.keys()):  
            return result.error('Missing required fields')  
    
        # 创建Books实例并添加到数据库  
        opera = Books(
            book_id=guid,  # 使用book_id而不是guid  
            book_title=data['book_title'],  # 注意字段名是book_title  
            author_id=data['author_id'],  
            book_description=data['book_description'],  
            book_url=data['book_url'],  
            cover_image_path=data['cover_image_path'],  
            chapter_title=data['chapter_title'],
        )  

        return add(opera)

    @app.route('/delete')
    def deletes():
        form = request.args
        guid = form.get('guid')

        if check_only('guid', guid):
            return result.error('guid is not exist')

        return delete(Books, Books.guid == guid)

    @app.route('/update', methods=['POST'])
    def updates():
        data = request.get_json()
        guid = data['guid']
        name = data['name']
        author = data['author']
        last_chapter = data['last_chapter']
        url = data['url']

        if check_only('guid', data['guid']):
            return result.error('guid is not exist')

        return update(Books, Books.guid == guid, {
            Books.name: name,
            Books.author: author,
            Books.last_chapter: last_chapter,
            Books.url: url,
        })
