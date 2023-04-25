from sqlalchemy import create_engine

HostName = "112.124.58.201"
Port = 3306
UserName = "root"
Password = "VMaqVB7Q"
DataBase = "book"

engine = create_engine("mysql+pymysql://root:VMaqVB7Q@112.124.58.201:3306/book")