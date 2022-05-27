from time import sleep
from string import ascii_lowercase
from random import choice

from loguru import logger

from browser import BrowserController
from database import DataBase, Curriculum


def main():
    db = DataBase('emails.db')
    emails = db.select('select email from emails where status is NULL')
    for email in emails:
        email_random = ''.join([choice(ascii_lowercase) for _ in range(10)])
        browser = BrowserController(Curriculum())
        first_step = browser.first_step(f'{email_random}@vddaz.com', sleeping_time=10)
        logger.info(first_step)
        if first_step:
            sleep(2)
            second_step = browser.second_step()
            logger.info(second_step)
            if second_step:
                sleep(2)
                third_step = browser.third_step()
                logger.info(third_step)
                if third_step:
                    sleep(2)
                    four_step = browser.four_step()
                    logger.info(four_step)
                    if four_step:
                        sleep(2)
                        five_step = browser.five_step()
                        logger.info(five_step)
                        if five_step:
                            sleep(5)
                            sixth_step = browser.sixth_step()
                            logger.info(sixth_step)
                            # db.update(f'update emails set status = "posted" where email is {email[0]}')
        else:
            logger.debug('error')
            sleep(60)
            # db.update(f'update emails set status = "ошибка в 1 шаге" where email is "{email[0]}"')
        browser.driver.quit()


if __name__ == '__main__':
    main()
