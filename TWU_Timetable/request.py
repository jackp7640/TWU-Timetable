from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrape import scrape
from make_table import make_table


    		

def request(username, password):

	url = "https://ics.twu.ca/ICS/"


	if username and password:

		driver = webdriver.Chrome('./chromedriver')
		driver.get(url)

		element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userName")))

		if driver.find_element_by_id('userName').is_displayed():
			driver.find_element_by_id('userName').send_keys(username)
			driver.find_element_by_id('password').send_keys(password)
			driver.find_element_by_id('siteNavBar_btnLogin').click()
		else:
			driver.find_element_by_id('siteNavBar_loginToggle').click()
			driver.find_element_by_id('userName').send_keys(username)
			driver.find_element_by_id('password').send_keys(password)
			driver.find_element_by_id('siteNavBar_btnLogin').click()

		url = "https://ics.twu.ca/ICS/Registration/Course_Schedule.jnz"
		driver.get(url)
		content = driver.page_source
		f = open("twu_website.html","w+")
		f.write(content)

	else:
		print("ENTER YOUR USERNAME AND PASSWORD")






