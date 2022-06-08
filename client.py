from time import sleep
from string import ascii_lowercase
from random import choice

from loguru import logger

from browser import BrowserController
from database import DataBase, Curriculum


class MainController:
    def __init__(self, browser: BrowserController, email: str):
        self.browser = browser
        self.email = email

    def __call__(self):
        first_step = self.browser.first_step(self.email, sleeping_time=0)
        logger.info(first_step)
        if first_step:
            sleep(2)
            second_step = self.browser.second_step()
            logger.info(second_step)
            if second_step:
                sleep(2)
                third_step = self.browser.third_step()
                logger.info(third_step)
                if third_step:
                    sleep(2)
                    four_step = self.browser.four_step()
                    logger.info(four_step)
                    if four_step:
                        sleep(2)
                        five_step = self.browser.five_step()
                        logger.info(five_step)
                        if five_step:
                            sleep(5)
                            sixth_step = self.browser.sixth_step()
                            logger.info(sixth_step)
                            if sixth_step:
                                sleep(5)
                                seven_step = self.browser.seven_step('https://rabota.ua/ua/company10163779/vacancy9168208')
                                logger.info(seven_step)
        self.browser.driver.quit()


def main():
    while True:
        for _ in range(5):
            browser = BrowserController(Curriculum())
            email = ''.join([choice(ascii_lowercase) for _ in range(10)])
            controller = MainController(browser, f'{email}@vddaz.com')
            controller()
        sleep(60 * 30)


if __name__ == '__main__':
    main()
