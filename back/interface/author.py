# from db import conn
# 使用sqlalchemy连接数据库
from utils import result
from db.engine import engine
from flask import request
from sqlalchemy.orm import sessionmaker
from conf.models import Authors
from conf.crud import add, update, delete, search, check_only, get_item
from utils.packfunc import getUUid, check_valid_guid

DBSession = sessionmaker(bind=engine)
session = DBSession()


def author(app):
    @app.route('/search')
    def searchs():
        form = request.args
        guid = form.get('author_id')

        if guid:
            sql = f"SELECT * FROM books Where author_id = '{guid}'"
        else:
            sql = f"SELECT * FROM books"

        return search(sql)

    @app.route('/add', methods=['POST'])
    def adds():
        data = request.get_json()  
        guid = check_valid_guid(data)  
    
        if not guid:  
            guid = getUUid()  # 如果没有提供guid，则生成一个新的  
    
        if check_only('author_id', guid):  # 注意这里我们使用'book_id'而不是'guid'，因为字段名是book_id  
            return result.error('guid is exist')  # 这里可能需要根据实际情况调整错误信息  
    
        # 验证data中是否包含所有必要的字段  
        required_fields = {'author_id', 'author_name'}  
        if not required_fields.issubset(data.keys()):  
            return result.error('Missing required fields')  
    
        # 创建Books实例并添加到数据库  
        opera = Authors(
            author_id=guid, 
            author_name=data['author_name'],
        )  

        return add(opera)

    # @app.route('/delete')
    # def deletes():
    #     form = request.args
    #     guid = form.get('guid')

    #     if check_only('guid', guid):
    #         return result.error('guid is not exist')

    #     return delete(Books, Books.guid == guid)

    @app.route('/update', methods=['POST'])
    def updates():
        data = request.get_json()

        if 'author_id' not in data or not data['author_id']:
            return result.error('author_id is missing')

        author_id = data['author_id']
        author_name = data.get('author_name') 

        if check_only('author_id', data['author_id']):
            return result.error('author_id is not exist')

        # 查找原有的数据
        sql = f"SELECT * FROM books Where author_id = '{author_id}'"
        book = get_item(sql)
        
        # 未传的数据使用原数据
        update_dict = {
            'author_id': author_id or book['author_id'],
            'author_name': author_name or book['author_name'],
        }  

        return update(Authors, Authors.author_id == author_id, update_dict)
