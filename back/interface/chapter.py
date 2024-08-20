# from db import conn
# 使用sqlalchemy连接数据库
from utils import result
from db.engine import engine
from flask import request
from sqlalchemy.orm import sessionmaker
from conf.models import Books, Chapters
from conf.crud import add, update, delete, search, check_only, get_item
from utils.packfunc import getUUid, check_valid_guid

DBSession = sessionmaker(bind=engine)
session = DBSession()

def chapter(app):
    @app.route('/chapter/search')
    def chapter_searchs():
        form = request.args
        chapter_id = form.get('chapter_id')

        if chapter_id:
            sql = f"SELECT * FROM chapters Where chapter_id = '{chapter_id}'"
        else:
            sql = f"SELECT * FROM chapters"

        return search(sql)

    @app.route('/chapter/add', methods=['POST'])
    def chapter_adds():
        data = request.get_json()  
        guid = check_valid_guid(data, 'chapter_id')
        print(guid)
    
        if not guid:  
            guid = getUUid()  # 如果没有提供guid，则生成一个新的  

        if not check_only('chapters', 'chapter_id', guid):  # 注意这里我们使用'book_id'而不是'guid'，因为字段名是book_id  
            return result.error('guid is exist')  # 这里可能需要根据实际情况调整错误信息  
    
        # 验证data中是否包含所有必要的字段  
        required_fields = {'book_id', 'chapter_title', 'chapter_content', 'pre_chapter_id', 'last_chapter_id'}  
        if not required_fields.issubset(data.keys()):  
            return result.error('Missing required fields')  
    
        # 创建Books实例并添加到数据库  
        opera = Chapters(  
            chapter_id = guid,  # 使用book_id而不是guid  
            book_id = data['book_id'],  # 注意字段名是book_title  
            chapter_title = data['chapter_title'],  
            chapter_content = data['chapter_content'],  
            pre_chapter_id = data['pre_chapter_id'],  
            last_chapter_id = data['last_chapter_id'],  
        )  

        return add(opera)  

    # @app.route('/delete', methods=['DELETE'])
    # def deletes():
    #     form = request.args
    #     book_id = form.get('book_id')

    #     if check_only('book_id', book_id):
    #         return result.error('book_id is not exist')

    #     return delete(Books, Books.book_id == book_id)

    # @app.route('/update', methods=['patch'])
    # def updates():
    #     try:
    #         data = request.get_json()

    #         if not check_valid_guid(data, 'book_id'):
    #             return result.error('book_id is missing')

    #         book_id = data['book_id']
    #         book_title = data.get('book_title')  
    #         author_name = data.get('author_name')  
    #         book_description = data.get('book_description')  
    #         cover_image_path = data.get('cover_image_path')  
    #         book_url = data.get('book_url')  
    #         chapter_title = data.get('chapter_title')

    #         if check_only('book_id', data['book_id']):
    #             return result.error('book_id is not exist')

    #         # 查找原有的数据
    #         sql = f"SELECT * FROM books Where book_id = '{book_id}'"
    #         book = get_item(sql)
            
    #         # 未传的数据使用原数据
    #         update_dict = {
    #             'book_title': book_title or book['book_title'],
    #             'author_name': author_name or book['author_name'],
    #             'book_description': book_description or book['book_description'],
    #             'cover_image_path': cover_image_path or book['cover_image_path'],
    #             'book_url': book_url or book['book_url'],
    #             'chapter_title': chapter_title or book['chapter_title'],
    #         }  

    #         return update(Books, Books.book_id == book_id, update_dict)
    #     except Exception as e:
    #         print(f"{e}")
    #         return result.error('')
