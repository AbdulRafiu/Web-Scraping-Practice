from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver')
browser.get("https://www.bata.com.pk")
input_ = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[1]/nav/div/div/ul/li[9]/form/input')
input_.send_keys("Power")
browser.find_element_by_xpath('//*[@id="nav"]/li[9]/form/button').click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[5]/div/div/div[2]/div/div[1]/div[2]/div/a/h3').click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[5]/div[1]/div/div[3]/div/div[1]/form/div[7]/input').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="CartContainer"]/form/div[2]/button').click()
browser.find_element_by_xpath('/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input').send_keys("ark.1kh@gmail.com")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys("Abdul")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys("Rafiu")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys("Bodla Road")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys("Ranipur")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').clear()
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys("66100")
browser.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys("3003046687")
browser.find_element_by_xpath('//*[@id="continue_button"]').click()
