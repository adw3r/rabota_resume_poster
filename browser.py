import time
from abc import ABC, abstractmethod

from loguru import logger
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from database import Curriculum


class Controller(ABC):

    @abstractmethod
    def first_step(self, email: str):
        pass

    @abstractmethod
    def second_step(self):
        pass

    @abstractmethod
    def third_step(self):
        pass

    @abstractmethod
    def four_step(self):
        pass


class BrowserController(Controller):
    starting_page = 'https://rabota.ua/jobsearch/cvwelcome'
    mail_xpath = '//div[2]//div[3]/input'
    password_xpath = '//div[2]/div[4]/input'
    first_name_xpath = '//div[2]/div[1]/input'
    second_name_xpath = '//div[2]/div[2]/input'
    submit_button_xpath = '//div[2]/button[text()="ЗАРЕГИСТРИРОВАТЬСЯ"]'
    experience_edit_xpath = '//div[4]//span/a'
    div_button = '//div[2]/div[2]/button'
    iframe_field_xpath = '//html/body'
    phone_number_xpath = '//input[@id="phone_field"]'
    city_field_xpath = '//input[@id="city_field_main"]'
    day_field_xpath = '//input[@id="birth_day_field"]'
    birth_year_field = '//input[@id="birth_year_field"]'
    month_xpath = '//select[@id="birth_month_field"]/option[@value="1"]'
    second_step_xpath = '//div[7]/a[@href="#nextstep"]'  # 2 step
    wanted_position_xpath = '//input[@id="wanted_position_field"]'
    third_step_xpath = '//div[3]/a'
    lastwork_company_field = '//input[@id="lastwork_company_field"]'
    lastwork_position_field = '//input[@id="lastwork_position_field"]'
    startwork_month_field = '//select[@id="startwork_month_field"]//option[@value="0"]'
    startwork_year_field = '//input[@id="startwork_year_field"]'
    until_now_xpath = '//span[@class="f-checkbox-control"]'
    submit_xpath = '//div[2]/a[@href="#submit"]'

    def __init__(self, resume: Curriculum):
        self.driver = Chrome()
        self.resume = resume

    def first_step(self, email: str) -> bool:
        print('first_step')
        result = False
        self.driver.get(self.starting_page)
        try:
            self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(self.resume.firstname)
            self.driver.find_element(By.XPATH, self.second_name_xpath).send_keys(self.resume.lastname)
            self.driver.find_element(By.XPATH, self.mail_xpath).send_keys(email)
            self.driver.find_element(By.XPATH, self.password_xpath).send_keys(self.resume.password)
            self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
            time.sleep(1.5)
            assert 'Этот email уже зарегистрирован.' not in self.driver.page_source
            result = True
        except Exception as error:
            logger.exception(error)
        finally:
            return result
            
    def second_step(self) -> bool:
        print('second step')
        result = False
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains('Разместить '))
            self.driver.find_element(By.XPATH, self.phone_number_xpath).send_keys(self.resume.phone)
            self.driver.find_element(By.XPATH, self.city_field_xpath).send_keys(self.resume.city)
            self.driver.find_element(By.XPATH, self.day_field_xpath).send_keys(self.resume.b_day)
            self.driver.find_element(By.XPATH, self.birth_year_field).send_keys(self.resume.b_year)
            self.driver.find_element(By.XPATH, self.month_xpath).click()
            self.driver.find_element(By.XPATH, self.second_step_xpath).click()
            time.sleep(0.7)
            result = True
        except Exception as error:
            logger.exception(error)
        finally:
            return result
        
    def third_step(self) -> bool:
        print('third_step')
        result = False
        try:
            self.driver.find_element(By.XPATH, self.wanted_position_xpath).send_keys(self.resume.wanted_job)
            self.driver.find_element(By.XPATH, self.wanted_position_xpath).send_keys(Keys.PAGE_DOWN)
            self.driver.find_element(By.XPATH, self.wanted_position_xpath).send_keys(Keys.RETURN)
            self.driver.find_element(By.XPATH, self.third_step_xpath).click()
            self.driver.find_element(By.XPATH, self.lastwork_company_field).send_keys(self.resume.previous_company)
            self.driver.find_element(By.XPATH, self.lastwork_position_field).send_keys(self.resume.wanted_job)
            self.driver.find_element(By.XPATH, self.startwork_month_field).click()
            self.driver.find_element(By.XPATH, self.birth_year_field).send_keys(self.resume.experience_year)
            self.driver.find_element(By.XPATH, self.until_now_xpath).click()
            self.driver.find_element(By.XPATH, self.submit_xpath).click()
            result = True
        except Exception as error:
            logger.exception(error)
        finally:
            return result
        
    def four_step(self) -> bool:
        print('four step')
        result = False
        try:
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, self.experience_edit_xpath)))
            self.driver.find_element(By.XPATH, self.experience_edit_xpath).click()
            frame = self.driver.find_element(By.TAG_NAME, "iframe")
            self.driver.switch_to.frame(frame)
            iframe = self.driver.find_element(By.XPATH, self.iframe_field_xpath)
            iframe.send_keys(self.resume.skills)
            self.driver.switch_to.default_content()
            self.driver.find_element(By.XPATH, self.div_button).click()
            result = True
        except Exception as error:
            logger.exception(error)
        finally:
            return result
