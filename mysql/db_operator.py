# -*-coding:utf-8 -*-

'''
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
'''


import mysql.connector


class DbOperator:
  
    def __init__(self):
        # 打开数据库连接
        self.db = mysql.connector.connect(
                    host="localhost",            # 数据库主机地址
                    user="DbOperator",           # 数据库用户名
                    passwd="DoNotAnswer2048!",   # 数据库密码
                    database='ObDb')             # 直接选择特定数据库
        # print(self.db)

    def __del__(self):
        # 关闭数据库连接
        self.db.close()
        print("db del")

    def get_record(self, id):

        cursor = self.db.cursor()        # 使用cursor()方法获取操作游标

        query = "SELECT * FROM test WHERE id = %s ;" # 无论什么类型的数据，占位符都使用%s
         
        # 使用execute方法执行SQL语句
        cursor.execute(query, (id, ))
        result = cursor.fetchall()


        '''
        for (first_name, last_name, hire_date) in cursor:
            print("{}, {} was hired on {:%d %b %Y}".format(
                last_name, first_name, hire_date))
        '''

        print(result)
        print(type(result))
        cursor.close()

        return True

    def update_user(self):
        return True


if __name__ == "__main__":
    print("start running")
    worker = DbOperator()
    result = worker.get_record(111)
    print(result)
    print("finish")


# 使用 fetchone() 方法获取一条数据库。

# data = cursor.fetchone()





# s = t[0][1].decode('utf-8')
