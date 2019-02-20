import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password,
                                          autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_deleted_users(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select login, deleted from users where users_id = 249 and deleted = 1")
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()
