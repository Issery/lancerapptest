from flask import Flask
from sqlalchemy.engine import create_engine
from flask_sqlalchemy import SQLAlchemy
import pymssql
import config


# encoding utf
import sys
import imp
imp.reload(sys)


app = Flask(__name__)


# 创建数据库引擎
engine = create_engine(config.DB_URI)
print('connected@-----------------------------------------')
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'article' #如果不指定表名，会默认以这个类名的小写为表名
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.Text,nullable = False)

db.create_all()

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)