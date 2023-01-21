#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
import telebot
from config.definitions import ROOT_DIR


class PdaCheckerBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def setup(self):
        self.driver.get('https://online.transport.wa.gov.au/tso/selfservice/overview.jsf')
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm:userId"]').send_keys('chlollli20')
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm:password"]').send_keys('Myworld0410')
        self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm:loginButton"]').click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="menuForm:menubar_licence"]'))).click()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="form:bookPDA"]'))).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value='//*[@id="id7"]').click()
        sleep(1)

        tomorrow = datetime.date.today()
        tomorrow += datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime("%d/%m/%Y")
        limit_date = '31/12/2038'
        self.driver.find_element(by=By.XPATH, value='//*[@id="fromDateInput"]').send_keys(tomorrow)
        self.driver.find_element(by=By.XPATH, value='//*[@id="toDateInput"]').send_keys(limit_date)
        self.driver.find_element(by=By.XPATH, value='//*[@id="id2-searchBookingContainer:siteList_CAN"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="id2-searchBookingContainer:siteList_KELM"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="id2-searchBookingContainer:siteList_SUC"]').click()
        self.driver.find_element(by=By.XPATH, value='//*[@id="id8"]').click()

    def count_slots(self):
        slots = self.driver.find_elements(by=By.XPATH, value='//*[@id="searchResultRadioLabel"]')
        num_slots = len(slots)
        return num_slots

    def take_screenshot(self):
        available_slots = self.driver.find_element(by=By.XPATH, value='//*[@id="id9"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", available_slots)
        try:
            available_slots.screenshot('avail.png')
        except:
            pass

    def refresh(self):
        token = '5765375699:AAFy0l6bvO0xNkzh5GUrUD3LCpt0dtv4KHo'
        receiver_id = 762166894
        tel_bot = telebot.TeleBot(token)

        num_slots = -1

        while True:
            self.driver.find_element(by=By.XPATH, value='//*[@id="id8"]').click()

            count = bot.count_slots()
            if count == 0 and num_slots == -1:
                num_slots = 0
                tel_bot.send_message(receiver_id, "Starting search...")

            elif num_slots != count:
                num_slots = count
                bot.take_screenshot()
                screen_path = ROOT_DIR + r"/avail.png"
                tel_bot.send_photo(receiver_id,
                                   photo=open(screen_path, 'rb'),
                                   caption='Change in available slots.')

            sleep(int(interval))


interval = input("How often would you like me to refresh the page? Answer in seconds:")
bot = PdaCheckerBot()
bot.setup()
bot.refresh()
