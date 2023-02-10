import sqlite3
import os

from User import *


# def get_file_dirs(dir):
#     arr = []
#     for file_name in os.listdir(dir):
#         arr += [tuple([file_name, os.stat(f"{dir}/{file_name}").st_size])]
#     return arr
#
#
# def get_names(db_name):
#     new_con = sqlite3.connect(db_name)
#     new_cur = new_con.cursor()
#     res = new_cur.execute("SELECT title FROM file WHERE weight > 80000")
#     arr = [tup[0] for tup in res.fetchall()]
#     new_con.close()
#     return arr


def add_uniq_user(db_name, user):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    data = [(user.get_id(), user.get_username(), user.get_matchs(), user.get_victories())]
    cur.executemany("INSERT INTO users2 VALUES(?, ?, ?, ?)", data)
    con.commit()
    con.close()


def clear_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("DELETE FROM users2")
    con.commit()
    con.close()


def create_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE users2(id, username, match_counts, victories)")
    cur.close()
    con.commit()
    con.close()


def get_user_data(db_name, id):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    data = cur.execute(f"SELECT username, match_counts FROM users2 WHERE id = {id}")
    res = data.fetchall()[0]
    con.close()
    return res


def update_db(db_name, user):
    id = user.get_id()
    matches = user.get_matchs()
    victories = user.get_victories()
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(f"UPDATE users2 SET match_counts = {matches}, victories = {victories} WHERE id = {id}")
    con.commit()
    con.close()
    return


#create_db("test.db")

# first = User("gay")
# first.set_id(11)
# first.plus_match_counts()
#
second = User("not_gay")
second.set_id(12)
for i in range(25):
    second.plus_match_counts()
    if i % 3 == 0:
        second.plus_victories()

update_db("test.db", second)
# add_uniq_user("test.db", first)
# add_uniq_user("test.db", second)

#clear_db("test.db")

print(get_user_data("test.db", 12))