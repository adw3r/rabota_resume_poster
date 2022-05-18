import sqlite3
from pathlib import Path

from resume_poster import connect


def trick(email: str = ''):
    f = lambda s: s[11:] and [s[0] + w + x for x in f(s[1:]) for w in ('.', '')] or [s]
    return f(email)
