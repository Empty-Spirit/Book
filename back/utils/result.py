from flask import jsonify
# from utils import rsaFunc

def success(data):
    resData = {
        "resCode": 200, # 非0即错误 1
        "data": data,# 数据位置，一般为数组
        "message": ''
    }
    return jsonify(resData)

def error(err):
    resData = {
        "resCode": 400, # 非0即错误 1
        "data": [],# 数据位置，一般为数组
        "message": err
    }
    return jsonify(resData)