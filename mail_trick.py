import sqlite3
from pathlib import Path

from resume_poster import connect


def trick(email: str = ''):
    f = lambda s: s[11:] and [s[0] + w + x for x in f(s[1:]) for w in ('.', '')] or [s]
    return f(email)


def main():
    con = connect('emails.db')
    cur = con.cursor()

    cur.execute('drop table emails')
    cur.execute(
        '''
        create table emails (
            email string primary key,
            status string
        )
        '''
    )
    for email in trick('alexeynaidiuk@gmail.com'):
        print((email,))
        cur.execute('insert into emails (email) values (?)', (email,))
    con.commit()
    print(len(cur.execute('select * from emails').fetchall()))
