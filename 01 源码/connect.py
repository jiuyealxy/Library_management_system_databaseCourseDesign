# 数据库链接模块
import pymysql

# 数据库链接
def connect():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='050330zzp',
                           database='library_management')
    cursor = conn.cursor()
    return cursor, conn