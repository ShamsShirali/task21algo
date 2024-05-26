
import time 
import pytest 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
@pytest.fixture 
def driver(): 
    service = Service("chromedriver.exe") 
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(service=service, options=options) 
    driver.maximize_window() 
    yield driver 
    driver.quit() 
     
def test_userinyerface(driver): 
    driver.get("https://userinyerface.com/game.html") 
    time.sleep(10)   
     
    block = driver.find_element(By.CSS_SELECTOR, 'div.cookies') 
    block_height = block.size['height'] 
    assert block_height == 155.2, "Height test fail" 
     
    block_background_color = block.value_of_css_property('background-color') 
    assert block_background_color == "rgba(255, 0, 0, 1)", "Color test fail" 
     
    print(f"Block height: {block_height}px") 
    print(f"Block background color: {block_background_color}") 
     
    logotype = driver.find_element(By.CSS_SELECTOR,'div.logo_icon') 
    logotype_height = logotype.size['height'] 
    assert logotype_height == 175, "Height test fail" 
    logotype_width = logotype.size['width'] 
    assert logotype_width == 300, "Width test fail" 
     
    print(f"Logotype height: {logotype_height}px") 
    print(f"Logotype width: {logotype_width}px") 
     
     
    logotype2 = driver.find_element(By.CSS_SELECTOR,'div.login-form') 
    logotype2_height = logotype2.size['height'] 
    assert logotype2_height == 297, "height test fail" 
    logotype2_width = logotype.size['width'] 
    assert logotype2_width == 436, "width test fail" 
    logotype2_background_color = logotype2.value_of_css_property('background-color') 
    assert logotype2_background_color == "RGBA(0, 0, 0, 0)", "Color test fail" 
     
     
    password = driver.find_element(By.CSS_SELECTOR,'.login-form__field-row') 
    password_height = password.size['height'] 
    assert logotype2_height == 40, "Height test fail" 
    password_width = password.size['width'] 
    assert password_width == 372, "Width test fail" 
     
    email = driver.find_element(By.CSS_SELECTOR,'.align__cell') 
    email_height = email.size['height'] 
    assert email_height == 40, "Height test fail" 
    email_width = email.size['width'] 
    assert email_width == 133.688, "Width test fail" 
    font = email.value_of_css_property('font-family') 
    assert font == "sans-serif", "Font family test fail" 
     
     
    print(f"Logotype2 height: {logotype2_height}px") 
    print(f"Logotype2 width: {logotype2_width}px") 
    print(f"Password height: {password_height}px") 
    print(f"Password width: {password_width}px") 
    print(f"Email height: {email_height}px") 
    print(f"Email width: {email_width}") 
    print(f"Logotype2 background: {logotype2_background_color}") 
    print(f"font: {font}px") 
     
     
     
if name == "__main__": 
    pytest.main()