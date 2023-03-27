
import sqlite3

def get_conn():
    return sqlite3.connect('config.db')


class DB:
    @classmethod
    def exec(cls, sql: str):
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()


    @classmethod
    def insert_name(cls, name):
        sql = f"insert into gamers (name) values ('{name}')"
        print(sql)
        cls.exec(sql)


    @classmethod
    def clean_table(cls):
        cls.exec(f'delete from gamers')



if __name__  == '__main__':
    pass