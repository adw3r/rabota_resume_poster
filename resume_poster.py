import time

from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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
