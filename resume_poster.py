import sqlite3
from pathlib import Path

from loguru import logger
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def connect(file: str):
    con = sqlite3.connect(file)
    return con


class Rabota:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)

    def first_page(self, mail, phone_number, city, wanted_position, first_name, second_name):
        def first_step():
            logger.info(mail)
            starting_page = 'https://rabota.ua/jobsearch/cvwelcome'
            self.driver.get(starting_page)
            mail_xpath = '//div[2]//div[3]/input'
            self.driver.find_element_by_xpath(mail_xpath).send_keys(mail)
            password_xpath = '//div[2]/div[4]/input'
            self.driver.find_element_by_xpath(password_xpath).send_keys(mail.split('@')[0])
            first_name_xpath = '//div[2]/div[1]/input'
            self.driver.find_element_by_xpath(first_name_xpath).send_keys(first_name)
            second_name_xpath = '//div[2]/div[2]/input'
            self.driver.find_element_by_xpath(second_name_xpath).send_keys(second_name)
            submit_button_xpath = '//div[2]/button[text()="ЗАРЕГИСТРИРОВАТЬСЯ"]'
            self.driver.find_element_by_xpath(submit_button_xpath).click()

        def second_step():
            WebDriverWait(self.driver, 40).until(EC.title_contains('Разместить '))
            phone_number_xpath = '//input[@id="phone_field"]'
            self.driver.find_element_by_xpath(phone_number_xpath).send_keys(phone_number)
            city_field_xpath = '//input[@id="city_field_main"]'
            self.driver.find_element_by_xpath(city_field_xpath).send_keys(city)
            day_field_xpath = '//input[@id="birth_day_field"]'
            self.driver.find_element_by_xpath(day_field_xpath).send_keys('01')
            year_field_xpath = '//input[@id="birth_year_field"]'
            self.driver.find_element_by_xpath(year_field_xpath).send_keys('1999')
            month_xpath = '//select[@id="birth_month_field"]/option[@value="1"]'
            self.driver.find_element_by_xpath(month_xpath).click()
            next_step_xpath = '//div[7]/a[@href="#nextstep"]'  # 2 step
            self.driver.find_element_by_xpath(next_step_xpath).click()

        def third_step():
            wanted_position_xpath = '//input[@id="wanted_position_field"]'
            self.driver.find_element_by_xpath(wanted_position_xpath).send_keys(wanted_position)
            time.sleep(0.7)
            self.driver.find_element_by_xpath(wanted_position_xpath).send_keys(Keys.PAGE_DOWN)
            self.driver.find_element_by_xpath(wanted_position_xpath).send_keys(Keys.RETURN)

        def fourth_step():
            next_step_xpath = '//div[3]/a'
            self.driver.find_element_by_xpath(next_step_xpath).click()
            company_field_xpath = '//input[@id="lastwork_company_field"]'
            self.driver.find_element_by_xpath(company_field_xpath).send_keys('noteleF'[::-1])
            position_field_xpath = '//input[@id="lastwork_position_field"]'
            self.driver.find_element_by_xpath(position_field_xpath).send_keys(wanted_position)
            month_field_xpath = '//select[@id="startwork_month_field"]//option[@value="0"]'
            self.driver.find_element_by_xpath(month_field_xpath).click()
            year_field_xpath = '//input[@id="startwork_year_field"]'
            self.driver.find_element_by_xpath(year_field_xpath).send_keys('2021')
            until_now_xpath = '//span[@class="f-checkbox-control"]'
            self.driver.find_element_by_xpath(until_now_xpath).click()
            submit_xpath = '//div[2]/a[@href="#submit"]'
            self.driver.find_element_by_xpath(submit_xpath).click()

        first_step()
        second_step()
        third_step()
        fourth_step()

    def second_page(self, skills_var, image_path):

        def skill():
            experience_edit_xpath = '//div[4]//span/a'
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, experience_edit_xpath)))
            self.driver.find_element_by_xpath(experience_edit_xpath).click()

            frame = self.driver.find_element_by_tag_name("iframe")
            self.driver.switch_to.frame(frame)

            iframe_field_xpath = '//html/body'
            iframe = self.driver.find_element_by_xpath(iframe_field_xpath)
            iframe.send_keys(skills_var)

            self.driver.switch_to.default_content()
            self.driver.find_element_by_xpath('//div[2]/div[2]/button').click()

        # def photo():
        #     a = '//div[2]/div[1]/div[2]/span/a'
        #     WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, a)))
        #     self.driver.find_element_by_xpath(a).click()
        #
        #     image_input_xpath = '//div[1]/div[1]/label/span'
        #     self.driver.find_element_by_xpath(image_input_xpath).click()
        #     autoit.win_wait_active("[CLASS:#32770]", 3)
        #     autoit.control_set_text("[CLASS:#32770]", "Edit1", image_path)
        #     autoit.send("{ENTER}")
        #
        #     slider_xpath = '//*[@id="ui-id-4"]/div[1]/div[2]/input'
        #     WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.XPATH, slider_xpath)))
        #     element = self.driver.find_element_by_xpath(slider_xpath)
        #     ActionChains(self.driver).click_and_hold(element).move_by_offset(-200, 0).release().perform()
        #
        #     save_xpath = '//*[@id="ui-id-4"]/div[2]/a[1]'
        #     self.driver.find_element_by_xpath(save_xpath).click()

        skill()


