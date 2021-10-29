from Domain.Models.User.IUserRepository import IUserRepository
from Domain.Models.User.user import User
from Domain.Models.User.user_name import UserName
import MySQLdb


class UserRepository(IUserRepository):
    def save(self, user):
        # データベースへの接続とカーソルの生成
        connection = MySQLdb.connect(
            host='db',
            user='root',
            passwd='password',
            db='mydb')
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO User (id, name)
            VALUES (%s, %s)
        """, (user.id.value, user.name.value))

        # 保存を実行
        connection.commit()

        # 接続を閉じる
        cursor.close()
        connection.close()


# if __name__ == '__main__':
#     repository = UserRepository()
#     user = User(UserName('test'))
#     repository.save(user)
