import sqlite3
from typing import List


class DataBase:
    def __init__(self, path: str):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def select(self, query: str) -> List[tuple]:
        self.cur.execute(query)
        return self.cur.fetchall()

    def update(self, query: str):
        self.cur.execute(query)
        self.con.commit()


class Curriculum:
    firstname: str
    lastname: str
    email: str
    password: str
    phone: str
    city: str
    b_day: str
    b_month: str
    b_year: str
    wanted_job: str
    previous_company: str
    experience: str
    experience_year: str
    skills: str
    about: str

    def __init__(self):
        self.__dict__ = {
                'firstname': 'Alexey',
                'lastname': 'Naidiuk',
                'email': '',
                'password': 'Zxcasdqwe123',
                'phone': '505718633',
                'city': 'Киев',
                'b_day': '1',
                'b_month': 'декабрь',
                'b_year': '1999',
                'wanted_job': 'python developer',
                'previous_company': 'Conslux',
                'experience': 'февраль',
                'experience_year': '2021',
                'skills': open('skills.txt').read(),
                'about': open('about.txt').read()
            }
