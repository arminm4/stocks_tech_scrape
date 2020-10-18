from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://tsetmc.com/Loader.aspx?ParTree=15131F')
assert 'TSETMC' in driver.title
elem = driver.find_element_by_id('main')
print(elem.text) 
driver.close()
