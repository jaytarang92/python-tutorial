from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = 'http://fakemailgenerator.com'
driver.get(url)
assert "Fake" in driver.title

"""
    to get values of html tags via xpath
    by_id was being weird and this universal
"""
def html_vals(tagtype, txpath):

    if tagtype != "value":
        print 'no value'
        tag = driver.find_element_by_xpath(txpath)
        tag_val = tag.get_attribute('innerHTML')
        print tag_val
    else:
        print 'yes value'
        print txpath
        tag = driver.find_element_by_xpath(txpath)
        tag_val = tag.get_attribute('value')
        print tag_val
        
html_vals('', '//*[@id="cxtEmail"]')
