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
        print("db connection created")

    def __del__(self):
        # 关闭数据库连接
        self.db.close()
        print("db connection deleted")

    def add_user(self, user):
        """Register new user.
        Add user info to database.

        Args:
            user: A tuple of user info like : (open_id, email)

        Returns:
            success or not: True/False
        """
        cursor = self.db.cursor()
        insert_new_user = (
                "INSERT INTO users (open_id, email, reg_date) "
                "VALUES (%s, %s, NOW())")
        cursor.execute(insert_new_user, user)

        # Commit the changes
        self.db.commit() 
        cursor.close()
        return True

    def find_user(self, open_id):
        """Get user info.
        Get user info from database. If user dosn't exist,
        return False and empty dict.

        Args:
            open_id: str offered by wechat

        Returns:
            success: True/False
            result: a dict of {'user_id','open_id','email','reg_date'}
        """
        success = True
        cursor = self.db.cursor()
        query = ("SELECT user_id, email, reg_date FROM users "
                "WHERE open_id = %s")
        cursor.execute(query, (open_id,))
        result = {}
        for (user_id, email, reg_date) in cursor:
            result['user_id'] = user_id
            result['open_id'] = open_id
            result['email'] = email
            result['reg_date'] = reg_date
        cursor.close()
        if len(result) == 0:
            success = False
        return success, result

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
        cursor.execute(query, (id,))
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
        print("db connection created")

    def __del__(self):
        # 关闭数据库连接
        self.db.close()
        print("db connection deleted")

    def create_table(self):
        """Create table.
        If table doesn't exist, creat it.

        Args:
            nothing
        Returns:
            nothing
        """
        cursor = self.db.cursor()        # 获取操作游标
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
    
    worker = DbOperator()
    # result = worker.add_user(("test_user1","test1@email.com"))






    
    print("find exist user:")
    success, result = worker.find_user("test_user1")
    print(success)
    print(result)
    print("find invalid user:")
    success, result = worker.find_user("nobody")
    print(success)
    print(result)
    
    print("finish")

    '''# 创建数据表是一次性操作，此后不再需要执行
    worker = DbCreator()
    worker.create_table()
    print("create tables finish")
    '''
    


# 使用 fetchone() 方法获取一条数据库。

# data = cursor.fetchone()





# s = t[0][1].decode('utf-8')
