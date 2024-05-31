import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('dilshod.db')
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            create table if not exists users(
                id integer primary key,
                title varchar not null,
                text varchar ,
                price varchar,
                country varchar ,
                photo varchar)""")

    def add_user(self, title, text, price, country, photo):
        self.cursor.execute("""insert into users
                            (title, text, price, country, photo)
                            values (?, ?, ?, ?, ?)""",
                            (title, text, price, country, photo))
        self.connection.commit()

    def show_users(self):
        users = self.cursor.execute("select * from users")
        return users.fetchall()
    #
    # def get_user(self, first_title, phone_number):
    #     user = self.cursor.execute("select * from users where first_title=? and phone_number=?",
    #                                (first_title, phone_number))
    #     return user.fetchone()



db = Database()
# db.add_user(first_title="Ibrohim",
#             last_title="Muhammedov", email="ibrohim@mail.ru",
#             country="Uzbekistan", text=12,
#             phone_number="+9989777777")
#
# users = db.show_users()
# for user in users:
#     print(user)
#
# # db.update_user(title="Ibrohim", text=12, id=2)
# # db.delete_user(id=1)
#
# user = db.get_user(first_title="Samir", phone_number="+9989112312322")
# print(user)
