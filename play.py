# coding=UTF-8
import argparse
import os
import platform
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from AccountList import AccountList

MABINOGI_URL = "https://tw.beanfun.com/game_zone/"


def main(account_idx):
    driver_path = get_chrome_driver()

    driver = get_driver(driver_path)
    start_new_session(driver)
    login(driver, accounts.getAccount(account_idx))

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fbClose"))
        )
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except Exception:
        pass

    mabi_icon_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "img[src=\"https://tw.images.beanfun.com/uploaded_images/beanfun_tw/game_zone/20130820175530929.jpg\"]"))
    )

    driver.execute_script("arguments[0].click();", mabi_icon_btn)

    game_entry_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fbContent"))
    )
    driver.switch_to.frame(game_entry_iframe)
    account_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ulServiceAccountList"))
    )
    account_btn.click()
    no_more_reminder_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cbxRemoveServiceFriendlyReminder"))
    )

    no_more_reminder_checkbox.click()
    time.sleep(7)
    enter_game_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btnFriendlyReminderOK"))
    )
    enter_game_btn.click()

    time.sleep(100000)
    stop_session(driver)


def get_chrome_driver():
    driver_path = os.path.dirname(os.path.abspath(__file__)) + '/driver/'
    if platform.system() == 'Windows':
        return driver_path + "win32/chromedriver.exe"
    elif platform.system() == 'Darwin':
        return driver_path + "mac64/chromedriver"
    else:
        raise Exception('Not supported os')


def start_new_session(driver):
    driver.get(MABINOGI_URL)


def stop_session(driver):
    driver.close()


def get_driver(driver_path):
    chrome_options = webdriver.ChromeOptions()
    beanfun_extension_path = os.path.dirname(
        os.path.abspath(__file__)) + '/driver/extension/beanfun'
    chrome_options.add_argument("load-extension=" + beanfun_extension_path)
    driver = webdriver.Chrome(driver_path, options=chrome_options)
    return driver


def login(driver, user):
    driver.execute_script("return $('a[id=\"BF_anchorLoginBtn\"]')[0]").click()
    login_routine(driver, user)
    time.sleep(3)


def login_routine(driver, user):
    # Login elements is in iframe, should switch to it
    login_iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ifmForm1"))
    )
    driver.switch_to_frame(login_iframe)
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btn_login"))
    )
    account = driver.find_element_by_id("t_AccountID")
    account.send_keys(user["account"])
    password = driver.find_element_by_id("t_Password")
    password.send_keys(user["password"])
    login_btn.click()


def log_out(driver):
    log_out_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i13"))
    )
    log_out_btn.click()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mabinogi auto login via webpage')

    args = parser.parse_args()

    accounts = AccountList("account.json")

    print(f'選擇欲登入之帳號編號:')
    accounts.display()
    account_idx = input()

    main(account_idx)
