import selenium
from selenium import webdriver

driver = webdriver.Chrome()

def test_selenium ():
    # driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

test_selenium()

#
# if __name__ == '__main__':
#     pytest.main()


