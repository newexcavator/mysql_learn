import MySQLdb


def get_conn(self):
    """ 获取连接 """
    try:
        self.con = MySQLdb.connect(
            host="localhost",
            port="3306",
            user="gosun",
            passwd="video",
            db="news",
            charset="utf8"
        )
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0], e.args[1]))
    return self.con

cursor = get_conn().cursor()
