import sqlite3
from pathlib import Path


def trick(email: str = ''):
    f = lambda s: s[11:] and [s[0] + w + x for x in f(s[1:]) for w in ('.', '')] or [s]
    return f(email)


def main():
    emails = trick('alexeynaidiuk1@gmail.com')
    con = sqlite3.connect('emails.db')
    for email in reversed(emails):
        con.execute('insert into emails(email) values (?)', (email,))
        con.commit()

main()