import random
import sqlite3

from User import User


def add_uniq_user(db_name, user):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    if len(cur.execute("SELECT * FROM users").fetchall()) == 0:
        id = user.get_id()
    else:
        id = get_next_id(db_name)
        user.set_id(id)
    data = [(id, user.get_username(), str(user.get_matchs()), str(user.get_victories()))]
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", data)
    con.commit()
    con.close()


def clear_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("DELETE FROM users")
    con.commit()
    if len(cur.execute("SELECT * FROM users").fetchall()) == 0:
        con.close()
        print("Cleared successfully")
    else:
        print("It`s didn`t work. Try again")


def create_db(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE users(id, username, match_counts, victories)")
    cur.close()
    con.commit()
    con.close()


def get_user_data(db_name, user):
    id = user.get_id()
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    data = cur.execute(f"SELECT * FROM users WHERE id = {id}")
    res = data.fetchall()[0]
    con.close()
    return res


def update_db(db_name, user):
    matches = user.get_matchs()
    victories = user.get_victories()
    id = user.get_id()
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(
        f"UPDATE users SET match_counts = {str(matches)}, victories = {str(victories)} WHERE id = {id}"
    )
    con.commit()
    con.close()
    return


def get_max_id(arr: list[tuple]):
    maximum = 0
    for tup in arr:
        maximum = tup[0] if tup[0] > maximum else maximum
    return maximum


def get_next_id(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    data = cur.execute("SELECT id FROM users")
    res = data.fetchall()
    con.commit()
    con.close()
    return get_max_id(res) + 1


#create_db("test.db")

first = User("gay22")
first.plus_match_counts()

second = User("not_gay")
for i in range(25):
    second.plus_match_counts()
    if i % 3 == 0:
        second.plus_victories()

#add_uniq_user("test.db", first)
#add_uniq_user("test.db", second)
third = User("Artyo")
for i in range(54):
    third.plus_match_counts()
    if i % 4:
        third.plus_victories()
#
print(get_user_data("test.db", first))
print(get_user_data("test.db", second))
print("################################")
second.plus_victories()
second.plus_victories()
second.plus_victories()
second.plus_match_counts()
update_db("test.db", second)
print(get_user_data("test.db", first))
print(get_user_data("test.db", second))
print("################################")
update_db("test.db", second)
#add_uniq_user("test.db", third)
print(get_user_data("test.db", first))
print(get_user_data("test.db", second))
print(get_user_data("test.db", third))
print("################################")
third.plus_match_counts()
third.plus_match_counts()
third.plus_match_counts()
third.plus_match_counts()
third.plus_match_counts()
third.plus_match_counts()
third.plus_victories()
first.plus_match_counts()
update_db("test.db", first)
update_db("test.db", second)
update_db("test.db", third)
print(get_user_data("test.db", first))
print(get_user_data("test.db", second))
print(get_user_data("test.db", third))
print("################################")

#clear_db("test.db")


