# -*-coding:utf-8 -*-

'''
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
'''


import mysql.connector
from mysql.connector import errorcode

# DB_NAME = 'ObDb'
TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `open_id` varchar(40) NOT NULL,"
    "  `email` varchar(255) NOT NULL,"
    "  `reg_date` date NOT NULL,"
    "  PRIMARY KEY (`user_id`), UNIQUE KEY `open_id` (`open_id`)"
    ") ENGINE=InnoDB")

TABLES['articles'] = (
    "CREATE TABLE `articles` ("
    "  `article_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `URL` varchar(2048) NOT NULL,"
    "  `open_id` varchar(40) NOT NULL,"
    "  `backup_addr` varchar(100) NOT NULL,"
    "  `start_date` date NOT NULL,"
    "  `status` INT UNSIGNED NOT NULL,"
    "  PRIMARY KEY (`article_id`)"
    ") ENGINE=InnoDB")

class DbOperator:
    def __init__(self):
        # 打开数据库连接
        self.db = mysql.connector.connect(
                    host="localhost",            # 数据库主机地址
                    user="DbOperator",           # 数据库用户名
                    passwd="DoNotAnswer2048!",   # 数据库密码
                    database='ObDb')             # 直接选择特定数据库
        print("db created")

    def __del__(self):
        # 关闭数据库连接
        self.db.close()
        print("db deleted")

    def add_user(self):
        return True
    def find_user(self):
        return True
    def update_user(self):
        return True
    def remove_user(self):
        return True
    def add_article(self):
        return True
    def update_article(self):
        return True
    def remove_article(self):
        return True

    def is_table_exist(self, table_name):
        """Check wanted table exists or not.
        Before operating database, you should check the existence of the table.
        If table doesn't exist, creat it first.

        Args:
            table_name: 'users' or 'articles'

        Returns:
            True/False
        """
        return True
    def create_table(self, table_name, ):
        """Create table.
        If table doesn't exist, creat it.

        Args:
            table_name: 'users' or 'articles'


        Returns:
            True/False
        """



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

    
class DbCreator:
    def __init__(self):
        # 打开数据库连接
        self.db = mysql.connector.connect(
                    host="localhost",            # 数据库主机地址
                    user="DbOperator",           # 数据库用户名
                    passwd="DoNotAnswer2048!",   # 数据库密码
                    database='ObDb')             # 直接选择特定数据库
        print("db created")

    def __del__(self):
        # 关闭数据库连接
        self.db.close()
        print("db deleted")

    def create_table(self):
        cursor = self.db.cursor()        # 使用cursor()方法获取操作游标

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        cursor.close()




if __name__ == "__main__":
    print("start running")
    '''
    worker = DbOperator()
    result = worker.get_record(111)
    print(result)
    '''
    worker = DbCreator()
    worker.create_table()
    print("finish")


# 使用 fetchone() 方法获取一条数据库。

# data = cursor.fetchone()





# s = t[0][1].decode('utf-8')
