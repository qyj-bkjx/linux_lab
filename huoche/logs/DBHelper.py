import pymysql
# 连接数据库
# 创建数据库train

class DbHelper:

    def __init__(self):
        # 开启数据库
        self.init()

    def init(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                             user='root',     # 用户名
                             passwd='',   # 密码,
                             port=3306,        # 端口，默认为3306
                             db='train',         # 数据库名称
                             charset='utf8'     # 字符编码
                            )
        self.cursor = self.conn.cursor() # 生成游标对象
        print("连接成功")

    def close(self):
        self.cursor.close()  # 关闭游标
        self.cursor.close()  # 关闭连接
        print("连接断开")

    # 查询多条信息
    def select(self,sql):
        self.cursor.execute(sql)		#执行sql语句
        data = self.cursor.fetchall()	#获取查询结果
        lengthen =len(data)				#获取数据条数
        return lengthen,data

    # 查询一条信息
    def selectOne(self,sql):
        self.cursor.execute(sql)		#执行sql语句
        data = self.cursor.fetchall()	#获取查询结果
        for item in data:
            return item