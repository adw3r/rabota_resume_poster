from loguru import logger

from browser import BrowserController
from database import DataBase, Curriculum


def main():
    db = DataBase('emails.db')
    emails = db.select('select email from emails where status is NULL')
    for email in emails:
        browser = BrowserController(Curriculum())
        if browser.first_step(email[0]):
            if browser.second_step():
                if browser.third_step():
                    if browser.four_step():
                        db.update(f'update emails set status = "posted" where email is {email[0]}')
        else:
            db.update(f'update emails set status = "ошибка в 1 шаге" where email is "{email[0]}"')
        browser.driver.quit()


if __name__ == '__main__':
    main()
