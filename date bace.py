import sqlite3


class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_point INTEGER
        )
        """
        self.cur.execute(query)
        self.con.commit()

    def get(self, que='SELECT * FROM score ORDER BY score_point DESC'):
        return self.cur.execute(que).fetchall()

    def insert(self, name, score):
        que = f"""INSERT INTO score (name, score_point) VALUES ('{name}', {score})"""
        self.cur.execute(que)
        self.con.commit()

    def __del__(self):
        self.con.close()


db = DataBase('score.sqlite3')
# db.insert('Puppies', 10)
# db.insert("Kittens", 15)
# db.insert('Pig', 3)
list = db.get()

for i in list:
    print(i)