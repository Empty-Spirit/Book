from db.engine import engine
from sqlalchemy.orm import sessionmaker
from utils import result
import pandas as pd
import json


DBSession = sessionmaker(bind=engine)
session = DBSession()

def check_only(fields, value):
  try:
    sql = f"SELECT * FROM collect WHERE {fields} = '{value}'"
    df = pd.read_sql_query(sql, engine)
    res = df.to_json(orient="records", force_ascii=False)
    list = json.loads(res)
    if not len(list):
      return True
    else:
      return False
  except:
    return False

def add(item):
  try:
    session.add(item)
    session.commit()
    session.close()
    return result.success('success')
  except:
    return result.error('failed to add item')

def update(model, filter, sql):
  res = session.query(model).filter(filter).update(sql)
  session.commit()
  session.close()
  if res:
    return result.success('success')
  else:
    return result.error('failed to update item')

def delete(model, filter):
  res = session.query(model).filter(filter).delete()
  session.commit()
  session.close()
  if res:
    return result.success('success')
  else:
    return result.error('failed to delete item')

def search(sql):
  try:
    df = pd.read_sql_query(sql, engine)
    res = df.to_json(orient="records", force_ascii=False)
    list = json.loads(res)
    return result.success(list)
  except:
    return result.error('failed to request')