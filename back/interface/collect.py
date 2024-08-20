# from db import conn
# 使用sqlalchemy连接数据库
from utils import result
from db.engine import engine
from flask import request
from sqlalchemy.orm import sessionmaker
from conf.models import Books
from conf.crud import add, update, delete, search, check_only, get_item
from utils.packfunc import getUUid, check_valid_guid

DBSession = sessionmaker(bind=engine)
session = DBSession()


def collect(app):
    @app.route('/search')
    def searchs():
        form = request.args
        book_id = form.get('book_id')

        if book_id:
            sql = f"SELECT * FROM books Where book_id = '{book_id}'"
        else:
            sql = f"SELECT * FROM books"

        return search(sql)

    @app.route('/add', methods=['POST'])
    def adds():
        data = request.get_json()  
        guid = check_valid_guid(data, 'book_id')
        print(guid)
    
        if not guid:  
            guid = getUUid()  # 如果没有提供guid，则生成一个新的  

        if not check_only('books', 'book_id', guid):  # 注意这里我们使用'book_id'而不是'guid'，因为字段名是book_id  
            return result.error('guid is exist')  # 这里可能需要根据实际情况调整错误信息  
    
        # 验证data中是否包含所有必要的字段  
        required_fields = {'book_title', 'author_name', 'book_description', 'book_url', 'cover_image_path', 'chapter_title'}  
        if not required_fields.issubset(data.keys()):  
            return result.error('Missing required fields')  
    
        # 创建Books实例并添加到数据库  
        opera = Books(  
            book_id=guid,  # 使用book_id而不是guid  
            book_title=data['book_title'],  # 注意字段名是book_title  
            author_name=data['author_name'],  
            book_description=data['book_description'],  
            book_url=data['book_url'],  
            cover_image_path=data['cover_image_path'],  
            chapter_title=data['chapter_title'],  
        )  

        return add(opera)

    @app.route('/delete', methods=['DELETE'])
    def deletes():
        form = request.args
        book_id = form.get('book_id')

        if check_only('books', 'book_id', book_id):
            return result.error('book_id is not exist')

        return delete(Books, Books.book_id == book_id)

    @app.route('/update', methods=['patch'])
    def updates():
        try:
            data = request.get_json()

            if not check_valid_guid(data, 'book_id'):
                return result.error('book_id is missing')

            book_id = data['book_id']
            book_title = data.get('book_title')  
            author_name = data.get('author_name')  
            book_description = data.get('book_description')  
            cover_image_path = data.get('cover_image_path')  
            book_url = data.get('book_url')  
            chapter_title = data.get('chapter_title')

            if check_only('books', 'book_id', data['book_id']):
                return result.error('book_id is not exist')

            # 查找原有的数据
            sql = f"SELECT * FROM books Where book_id = '{book_id}'"
            book = get_item(sql)
            
            # 未传的数据使用原数据
            update_dict = {
                'book_title': book_title or book['book_title'],
                'author_name': author_name or book['author_name'],
                'book_description': book_description or book['book_description'],
                'cover_image_path': cover_image_path or book['cover_image_path'],
                'book_url': book_url or book['book_url'],
                'chapter_title': chapter_title or book['chapter_title'],
            }  

            return update(Books, Books.book_id == book_id, update_dict)
        except Exception as e:
            print(f"{e}")
            return result.error('')
