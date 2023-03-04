import mysql.connector


class Core:

    def __init__(self) -> None:
        self.__dbConnection()
        self.__createTable()

    def __dbConnection(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost",
                database = "chatdb",
                user = "root",
                password = "root"
            )
        except Exception as err:
            print(err)
        else:
            print("Ma'lumotlar bazasiga ulandi.")
    
    def __createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = '''CREATE TABLE IF NOT EXISTS user (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(32) NOT NULL UNIQUE,
                    password VARCHAR(32) NOT NULL,
                    delete_date DATETIME NULL
                )'''
                cursor.execute(sql)

        except Exception as err:
            print(err)
        else:
            print("Jadval yasaldi.")

    def createUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                sql = f'''
                INSERT INTO user (username, password) VALUES
                    ('{username}', '{password}')
                '''
                cursor.execute(sql)

        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print("User yasaldi.")

    def getAllUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                SELECT username, password FROM user
                '''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            print("Malumotlar olindi.")
            return result

    def updateUser(self, username, password, newusername):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                UPDATE user 
                    SET username = '{newusername}'
                    WHERE username = "{username}" AND password = '{password}';
                '''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            print("Malumot o'zgardi.")
            self.conn.commit()

    def getUser(self, username):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                SELECT username, password FROM user
                WHERE username = '{username}'
                '''
                cursor.execute(query)
                result = cursor.fetchone()
        except Exception as err:
            print(err)
        else:
            print("Malumotlar olindi.")
            return result

    def deleteUser(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                UPDATE user 
                    SET delete_date = NOW()
                    WHERE username = "{username}" AND password = '{password}';
                '''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            print("Malumot o'chirildi.")
            self.conn.commit()

    def getActiveUsers(self):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                SELECT username, password FROM user
                WHERE delete_date IS NULL
                '''
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            print("Malumotlar olindi.")
            return result

    def deleteUser2(self, username, password):
        try:
            with self.conn.cursor() as cursor:
                query = f'''
                DELETE FROM user 
                WHERE username = '{username}' AND password = '{password}';
                '''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            print("Malumot o'chirildi.")
            self.conn.commit()

d = Core()
# d.deleteUser('terror', 'open')
# d.deleteUser2('user12', 'simochil')
print(d.getAllUsers())

# github
