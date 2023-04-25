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

        if guid and (not check_only('guid', guid)):
            return result.error('guid is exist')
        
        opera = Books(guid=guid or getUUid(), name=data['name'], author=data['author'], last_chapter=data['last_chapter'], url=data['url'])

        return add(opera)
    
    @app.route('/delete')
    def deletes():
        form = request.args
        guid = form.get('guid')

        if check_only('guid', guid):
            return result.error('guid is not exist')

        return delete(Books, Books.guid==guid)
            
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
