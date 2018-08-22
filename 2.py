import MySQLdb


class MysqlSearch():
    def __init__(self):
        self.get_conn()

    # 获取连接
    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host="127.0.0.1",
                port=3306,
                user="gosun",
                passwd="video",
                db="news",
                charset="utf8"
            )
        except MySQLdb.Error as e:
            print('Error : %s' % e)

    # 关闭连接
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error : %s' % e)

    # 获取数据
    def get_one(self):
        sql = 'select * from news where types = %s order by create_at desc;'
        # 找到cursor
        cursor = self.conn.cursor()
        # 执行sql
        cursor.execute(sql, ('百家', ))
        print(cursor.rowcount)
        print(dir(cursor))
        # 拿到结果
        rest = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # 处理数据
        print(rest['title'])
        # 关闭cursor/链接
        cursor.close()
        self.conn.close()


def main():
    obj = MysqlSearch()
    obj.get_one()


if __name__ == '__main__':
    main()






