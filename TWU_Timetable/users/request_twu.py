from selenium import webdriver

def request(username, password):
	# username = 'heechan.park'
	# password = '@Gmlcks813'
	url = "https://ics.twu.ca/ICS/"
	driver = webdriver.Chrome('./chromedriver')
	driver.get(url)

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




